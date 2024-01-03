% GNU Octave, version 8.4.0
%
% --- Day 12: Hot Springs ---
% https://adventofcode.com/2023/day/12
%
% https://github.com/AJPfleger
%
% call like 'octave day12py.m input.txt'

disp('--- Day 12: Hot Springs ---')

format long

args = argv();
filename = args{1}

fid = fopen(filename,'rt');
rawInput = textscan(fid,'%s','delimiter', '\n');
fclose(fid);

rawInput = rawInput{1};


%% Part 1 --------------------------------------------------------

[allSprings, allBroken] = parserawcells(rawInput);

C = 0;
for s = 1:numel(allSprings)
    C2 = countpossibilitiespy(allSprings{s}, allBroken{s});
    C = C + C2;
end

resultPart1 = C


%% Part 2 --------------------------------------------------------

% Part 2 is still too slow even with memoization and takes longer
% than days(?). I tried to proof the concept in

%unfolds = 5
%[allSprings, allBroken] = parserawcells(rawInput, unfolds);
%
%C = 0
%for s = 1:numel(allSprings)
%    C2 = countpossibilitiespy(allSprings{s}, allBroken{s})
%    C = C + C2;
%end
%
%resultPart2 = C
