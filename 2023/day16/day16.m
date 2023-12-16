% GNU Octave, version 8.4.0
%
% --- Day 16: The Floor Will Be Lava ---
% https://adventofcode.com/2023/day/16
%
% https://github.com/AJPfleger
%
% call like 'octave day16.m input.txt'

disp('--- Day 16: The Floor Will Be Lava ---')

args = argv();
filename = args{1}

fid = fopen(filename,'rt');
rawInput = textscan(fid,'%s','delimiter', '\n');
fclose(fid);

rawInput = rawInput{1};

R = numel(rawInput);

layout = [];
for i = 1:R
    layout(end+1,:) = double(rawInput{i});
end


%% Part 1 --------------------------------------------------------

start = [1,0,0,1,NaN];
resultPart1 = propagatelight(layout, start)


%% Part 2 --------------------------------------------------------

startingConfigs = [];
for s = 1:R
    startingConfigs(end+1,:) = [s,0,0,1,NaN];
    startingConfigs(end+1,:) = [s,R+1,0,-1,NaN];
    startingConfigs(end+1,:) = [0,s,1,0,NaN];
    startingConfigs(end+1,:) = [R+1,s,-1,0,NaN];
end

energized = [];
for s = 1:size(startingConfigs,1)
    start = startingConfigs(s,:);
    energized(end+1) = propagatelight(layout, start);
end

resultPart2 = max(energized)
