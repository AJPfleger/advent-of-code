% GNU Octave, version 8.4.0
%
% --- Day 8: Haunted Wasteland ---
% https://adventofcode.com/2023/day/8
%
% https://github.com/AJPfleger
%
% call like 'octave day08.m input.txt'

disp('--- Day 8: Haunted Wasteland ---')

format long

args = argv();
filename = args{1}

fid = fopen(filename,'rt');
rawInput = textscan(fid,'%s','delimiter', '\n');
fclose(fid);

rawInput = rawInput{1};

directions = [];
for c = 1:numel(rawInput{1})
    if rawInput{1}(c) == 'L'
        directions(end+1) = 2;
    else
        directions(end+1) = 3;
    end
end

Map = [];
for l = 3:numel(rawInput)
    line = rawInput{l};
    Map(end+1,:) = [hashString(line(1:3)), hashString(line(8:10)), hashString(line(13:15)), hashString(line(3))];
end

hashAAA = hashString("AAA");
hashZZZ = hashString("ZZZ");
hashA = hashString("A");
hashZ = hashString("Z");


%% Part 1 --------------------------------------------------------

steps = 0;
currentMapping = Map(Map(:,1) == hashAAA,:);
while currentMapping(1) ~= hashZZZ
    modStep = mod(steps,numel(directions)) + 1;
    dest = currentMapping(directions(modStep));
    currentMapping = Map(Map(:,1) == dest,:);

    steps = steps + 1;
end

resultPart1 = steps


%% Part 2 --------------------------------------------------------

mappingStarts = Map(Map(:,4) == hashA,:);
finalStates = [];
for t = 1:size(mappingStarts,1)
    steps = 0;
    currentMapping = mappingStarts(t,:);
    while any(currentMapping(:,4) ~= hashZ)
        modStep = mod(steps,numel(directions)) + 1;
        dest = currentMapping(:,directions(modStep));
        lMap = false(size(Map(:,1)));
        for l = 1:numel(dest)
            lMap = lMap | Map(:,1) == dest(l);
        end

        currentMapping = Map(lMap,:);
        steps = steps + 1;

    end

    finalStates(end+1,:) = [currentMapping,steps];
end

% Analysing the steps, we can figure out that there is a periodicity.
% Best thing: There is no offset. So we can just look for the least common multiple
leastCommonMultiple = 1;
for s = 1:size(finalStates,1)
    leastCommonMultiple = lcm(leastCommonMultiple,finalStates(s,5));
end

resultPart2 = leastCommonMultiple
