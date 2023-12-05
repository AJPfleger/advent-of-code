% GNU Octave, version 8.4.0
%
% --- Day 5: If You Give A Seed A Fertilizer ---
% https://adventofcode.com/2023/day/5
%
% https://github.com/AJPfleger
%
% call like 'octave day05.m input.txt'

disp('--- Day 5: If You Give A Seed A Fertilizer ---')

format long

args = argv();
filename = args{1}

fid = fopen(filename,'rt');
rawInput = textscan(fid,'%s','delimiter', '\n\n');
fclose(fid);

rawInput = rawInput{1};

seedList = str2num(rawInput{1}(8:end));

mapAll = [];
for c = 3:numel(rawInput)
    if ~isstrprop(rawInput{c}(:),'digit')
        mapAll(end+1,:) = NaN(1,3);
        continue
    elseif isempty(rawInput{c})
        continue
    else
        mapAll(end+1,:) = str2num(rawInput{c});
        rawInput{c}(:);
    end
end


%% Part 1

location = seedList;
for s = 1:numel(seedList)
    foundStep = false(1);
    for m = 1:size(mapAll,1)
        if foundStep
            if isnan(mapAll(m,1))
                foundStep = false(1);
            end
            continue
        end

        if mapAll(m,2) <= location(s) && location(s) < mapAll(m,2) + mapAll(m,3)
            location(s) = mapAll(m,1) + location(s) - mapAll(m,2);
            foundStep = true(1);
        end
    end
end


resultPart1 = min(location)

%% Part 2

seedRanges = reshape(seedList,[2,numel(seedList)/2]).';
seedRangesExpl = [seedRanges(:,1), seedRanges(:,1)+seedRanges(:,2) - 1];
seedRangesExpl
seedRangesExpl = sortrows(seedRangesExpl);

mapExpl = [mapAll(:,1), mapAll(:,1)+mapAll(:,3)-1, mapAll(:,2), mapAll(:,2)+mapAll(:,3)-1];
mapExpl(end+1,:) = NaN(size(mapExpl(end,:)));

a2b = [];
mapCell = {seedRangesExpl};
for m = 2:size(mapExpl,1)
    if isnan(mapExpl(m,:))
        mapCell{end+1} = sortrows(a2b);
        a2b = [];
    else
        a2b(end+1,:) = mapExpl(m,:);
    end
end

%data ready parsed
sInFull = mapCell{1}(:,1:2);

for step = 1:numel(mapCell)-1
    sOut = mapCell{step+1};
    sNew = [];
    iterIn = 1;
    while iterIn <= size(sInFull,1)

        sIn = sInFull(iterIn,:);
        iterIn = iterIn + 1;

        lsOut = (sIn(1) <= sOut) .* (sOut < sIn(2));

        lSeedFullyInside = logical((sOut(:,3) <= sIn(1)) .* (sIn(2) <= (sOut(:,4))));
        if any(lSeedFullyInside)
            sOutline = sOut(lSeedFullyInside,:);
            deltaStart = sIn(1) - sOutline(3);
            len = sIn(2) - sIn(1);
            sOutline = sOutline + deltaStart;
            sOutline(2) = sOutline(1) + len;
            sOutline(4) = sOutline(3) + len;
            sNew(end+1,:) = sOutline;
            continue
        end

        %split and append
        lSeedOverFlows = logical((sOut(:,3) <= sIn(1)) .* (sIn(1) <= (sOut(:,4))));
        if any(lSeedOverFlows)
            sOutline = sOut(lSeedOverFlows,:);
            deltaStart = sIn(1) - sOutline(3);
            len = sOutline(4) - sIn(1);
            sOutline = sOutline + deltaStart;
            sOutline(2) = sOutline(1) + len;
            sOutline(4) = sOutline(3) + len;
            sNew(end+1,:) = sOutline;
            sInFull(end+1,:) = [sOutline(4)+1,sIn(2)];
            continue
        end

        %seed enters a mapped area
        lSeedUnderFlows = logical((sOut(:,3) <= sIn(2)) .* (sIn(2) <= (sOut(:,4))));
        if any(lSeedUnderFlows)
            sOutline = sOut(lSeedUnderFlows,:);
            % deltaStart = 0;%sIn(1) - sOutline(3);
            len = sIn(2) - sOutline(3);
            % sOutline = sOutline + deltaStart;
            sOutline(2) = sOutline(1) + len;
            sOutline(4) = sOutline(3) + len;
            sNew(end+1,:) = sOutline;
            sInFull(end+1,:) = [sIn(1),sOutline(3)-1];
            continue
        end

        % "seed outside"
        sNew(end+1,:) = [sIn,sIn];
    end

    sNew;
    sInFull = sNew(:,1:2);
end

resultPart2 = min(sInFull(:,1))


% For testing purposes
% go backwards
loc = resultPart2;
locNew = NaN;
for step = numel(mapCell):-1:2
    currentCell = mapCell{step};
    for k = 1:size(currentCell,1)
        if currentCell(k,1) <= loc && loc <= currentCell(k,2)
            locNew = currentCell(k,3) + loc - currentCell(k,1);
        end
    end
    if ~isnan(locNew)
        loc = locNew;
    end
    locNew = NaN;
end

seed = loc
foundSeed = false;
for k = 1:size(seedRangesExpl,1)
    if seedRangesExpl(k,1) <= seed && seed <= seedRangesExpl(k,2)
        foundSeed = true
        disp("Found seed")
        seed
        break
    end
end

if foundSeed
    "The seed is real :)"
else
    "ERROR That seed does not exist"
end
