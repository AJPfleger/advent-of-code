% GNU Octave, version 8.4.0
%
% --- Day 12: Hot Springs ---
% https://adventofcode.com/2023/day/12
%
% https://github.com/AJPfleger
%
% call like 'octave day12.m input.txt'

disp('--- Day 12: Hot Springs ---')

args = argv();
filename = args{1}

fid = fopen(filename,'rt');
rawInput = textscan(fid,'%s','delimiter', '\n');
fclose(fid);

rawInput = rawInput{1};


%% Part 1 --------------------------------------------------------

[springs, broken] = parserawcells(rawInput)

tic
C = 0;
for l = 1:numel(rawInput)
    % C = C + countpossibilitiesbrute(springs{l},broken{l});
    C = C + countpossibilities(springs{l},broken{l});
end

resultPart1 = C
toc


%% Part 2 --------------------------------------------------------
unfolds = 5

[springs, broken] = parserawcells(rawInput, unfolds)

tic
C = 0;
for l = 1:numel(rawInput)
    % C = C + countpossibilitiesbrute(springs{l},broken{l});
    % C = C + countpossibilities(springs{l},broken{l});
end

resultPart2 = C
"algorithm is still too slow."
toc
