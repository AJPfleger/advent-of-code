% GNU Octave, version 8.4.0
%
% --- Day 6: Wait For It ---
% https://adventofcode.com/2023/day/6
%
% https://github.com/AJPfleger
%
% call like 'octave day06.m input.txt'

disp('--- Day 6: Wait For It ---')

format long

args = argv();
filename = args{1}

fid = fopen(filename,'rt');
rawInput = textscan(fid,'%s','delimiter', '\n');
fclose(fid);

rawInput = rawInput{1};

timeStr = rawInput{1}(6:end);
distStr = rawInput{2}(10:end);


%% Part 1 --------------------------------------------------------

times = str2num(timeStr);
dists = str2num(distStr);
win = [];
for race = 1:numel(times)

    possTimes = 0:times(race);
    possDists = possTimes .* possTimes(end:-1:1); % t * v

    win(end+1) = sum(possDists > dists(race));
end

resultPart1 = prod(win)


%% Part 2 --------------------------------------------------------

times = str2num(timeStr(~isspace(timeStr)));
dists = str2num(distStr(~isspace(distStr)));
win = [];
for race = 1:numel(times)

    possTimes = 0:times(race);
    possDists = possTimes .* possTimes(end:-1:1); % t * v

    win(end+1) = sum(possDists > dists(race));
end
resultPart2 = prod(win)


