% GNU Octave, version 8.4.0
%
% --- Day 4: Scratchcards ---
% https://adventofcode.com/2023/day/4
%
% https://github.com/AJPfleger
%
% call like 'octave day04.m input.txt'

disp('--- Day 4: Scratchcards ---')

args = argv();
filename = args{1}

rawInput = dlmread(filename);
delimiter = find(rawInput(1,:) == 0);
winningNumbers = rawInput(:,3:delimiter(2)-1);
myNumbers = rawInput(:,delimiter(2)+1:end);


%% Part 1 --------------------------------------------------------

countWinning = zeros(size(myNumbers(:,1)));
for mn = 1:size(myNumbers,2)
    countWinning = countWinning + sum(winningNumbers == myNumbers(:,mn),2);
end

resultPart1 = sum(2.^(countWinning(countWinning > 0)-1))


%% Part 2 --------------------------------------------------------

nCopies = ones(size(countWinning));
for cw = 1:numel(countWinning)-1
    wins = countWinning(cw);
    nCopies(cw+1:cw+wins) = nCopies(cw+1:cw+wins) + nCopies(cw);
end

resultPart2 = sum(copies(1:numel(countWinning)))
