% GNU Octave, version 8.4.0
%
% --- Day 13: Point of Incidence ---
% https://adventofcode.com/2023/day/13
%
% https://github.com/AJPfleger
%
% call like 'octave day13.m input.txt'

disp('--- Day 13: Point of Incidence ---')

args = argv();
filename = args{1}


fid = fopen(filename,'rt');
rawInput = textscan(fid,'%s','delimiter', '\n');
fclose(fid);

rawInput = rawInput{1};
rawInput{end+1} = ''; % needed in next loop for write-out

pattern = [];
allPatterns = {};
for i = 1:numel(rawInput)

    if numel(rawInput{i}) == 0
        allPatterns{end+1} = pattern;
        pattern = [];
    else
        pattern(end+1,:) = double(rawInput{i});
    end
end


%% Part 1 --------------------------------------------------------
resultPart1 = analysepatterns(allPatterns)


%% Part 2 --------------------------------------------------------
smudgeDifference = double('.') - double('#');
resultPart2 = analysepatterns(allPatterns, smudgeDifference)
