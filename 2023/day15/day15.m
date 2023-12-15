% GNU Octave, version 8.4.0
%
% --- Day 15: Lens Library ---
% https://adventofcode.com/2023/day/15
%
% https://github.com/AJPfleger
%
% call like 'octave day15.m input.txt'

disp('--- Day 15: Lens Library ---')

args = argv();
filename = args{1};

fid = fopen(filename,'rt');
rawInput = textscan(fid,'%s','delimiter', ',');
fclose(fid);

rawInput = rawInput{1};
R = numel(rawInput);


%% Part 1 --------------------------------------------------------

stepsHashed = zeros(R,1);
for s = 1:R
    stepsHashed(s) = hashfunction(rawInput{s});
end

resultPart1 = sum(stepsHashed)


%% Part 2 --------------------------------------------------------
% I couldn't find an ordered dictionary/map in MATLAB octave, so I
% wrote it myself. Each box contains an array
% [hashstring(key), value; ...]
% with a bijective hashstring() function

allBoxes = cell(256,1);
for s = 1:R
    step = rawInput{s};

    if step(end) ~= '-' % mode '='
        equ = find(step == '=');
        lab = step(1:equ-1);
        n = str2num(step(equ+1));

        box = hashfunction(lab)+1;
        hlab = hashstring(lab);

        if numel(allBoxes{box}) == 0
            allBoxes{box} = [hlab, n];
        elseif any(allBoxes{box}(:,1) == hlab)
            allBoxes{box}(allBoxes{box}(:,1) == hlab,2) = n;
        else
            allBoxes{box}(end+1,:) = [hlab, n];
        end
    else % mode '-'
        lab = step(1:end-1);
        box = hashfunction(lab) + 1;

        if numel(allBoxes{box}) ~= 0
            hlab = hashstring(lab);
            allBoxes{box}(allBoxes{box}(:,1) == hlab,:) = [];
        end
    end
end

s = [];
for box = 1:numel(allBoxes)

    if numel(allBoxes{box}) == 0
        continue
    end

    b = allBoxes{box}(:,2);

    s(end+1) = box * sum(b(:,1) .* [1:numel(b)].');
end

resultPart2 = sum(s)
