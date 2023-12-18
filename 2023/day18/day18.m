% GNU Octave, version 8.4.0
%
% --- Day 18: Lavaduct Lagoon ---
% https://adventofcode.com/2023/day/18
%
% https://github.com/AJPfleger
%
% call like 'octave day18.m input.txt'

disp('--- Day 18: Lavaduct Lagoon ---')

format long

args = argv();
filename = args{1}

fid = fopen(filename,'rt');
rawInput = textscan(fid,'%s','delimiter', '\n');
fclose(fid);

rawInput = rawInput{1};


%% Part 1 --------------------------------------------------------

instructions = [];
for r = 1:numel(rawInput)
    ss = strsplit(rawInput{r});
    instructions(end+1,:) = [double(ss{1}), str2num(ss{2})];
end

allPos = ins2pos(instructions);

resultPart1 = getarea(allPos)


%% Part 2 --------------------------------------------------------

instructions = [];
for r = 1:numel(rawInput)
    ss = strsplit(rawInput{r});
    instructions(end+1,:) = [str2num(ss{3}(8)), hex2dec(ss{3}(3:7))];
end

allPos = ins2pos(instructions);

resultPart2 = getarea(allPos)
