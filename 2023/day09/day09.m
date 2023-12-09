% GNU Octave, version 8.4.0
%
% --- Day 9: Mirage Maintenance ---
% https://adventofcode.com/2023/day/9
%
% https://github.com/AJPfleger
%
% call like 'octave day09.m input.txt'

disp('--- Day 9: Mirage Maintenance ---')

args = argv();
filename = args{1}

format long

rawInput = dlmread(filename);

finalValues = zeros(size(rawInput(:,1:2)));
for l = 1:size(rawInput,1)

    line = [rawInput(l,:); fliplr(rawInput(l,:))];
    lineEnds = line(:,end);

    while sum(line(:) != 0) ~=0
        line = diff(line,1,2);
        lineEnds(:,end+1) = line(:,end);
    end
    finalValues(l,:) = sum(lineEnds.');
end

finalSums = sum(finalValues);

resultPart1 = finalSums(1)
resultPart2 = finalSums(2)
