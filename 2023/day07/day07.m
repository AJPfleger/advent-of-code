% GNU Octave, version 8.4.0
%
% --- Day 7: Camel Cards ---
% https://adventofcode.com/2023/day/7
%
% https://github.com/AJPfleger
%
% call like 'octave day07.m input.txt'

disp('--- Day 7: Camel Cards ---')

format long

args = argv();
filename = args{1}

fid = fopen(filename,'rt');
rawInput = textscan(fid,'%s','delimiter', '\n');
fclose(fid);

rawInput = rawInput{1};

%% Part 1 --------------------------------------------------------

JisForJoker = false;
allHands = [];
for h = 1:numel(rawInput)
    allHands(end+1,:) = evaluatehand(rawInput{h},JisForJoker);
end

allHands = sortrows(allHands,[6,1:5]);

resultPart1 = sum(allHands(:,end).' .* (1:numel(allHands(:,end))))


%% Part 2 --------------------------------------------------------

JisForJoker = true;
allHands = [];
for h = 1:numel(rawInput)
    allHands(end+1,:) = evaluatehand(rawInput{h},JisForJoker);
end

allHands = sortrows(allHands,[6,1:5]);

resultPart2 = sum(allHands(:,end).' .* (1:numel(allHands(:,end))))
