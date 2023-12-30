% GNU Octave, version 8.4.0
%
% --- Day 21: Step Counter ---
% https://adventofcode.com/2023/day/21
%
% https://github.com/AJPfleger
%
% call like 'octave day21.m input.txt'

disp('--- Day 21: Step Counter ---')

format long

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

nSteps = 64
endPositions = getendpositions(layout, nSteps);

resultPart1 = sum(endPositions(:))


%% Part 2 --------------------------------------------------------
% Analysing the input data we can find a periodicity of 131. It is
% the time we need to reach from one center 4 new centers.
% We use a 5x5 copy of the layout to analyse the border and center
% regions. In the end we use a mathematical expression to get the
% final step count.
% This does not work with arbitrary inputs!

nSteps = 26501365
period = 131

lay2 = layout;
lay2(lay2 == double('S')) = double('.');

layout5x5 = [lay2, lay2, lay2, lay2, lay2; ...
          lay2, lay2, lay2, lay2, lay2; ...
          lay2, lay2, layout, lay2, lay2; ...
          lay2, lay2, lay2, lay2, lay2; ...
          lay2, lay2, lay2, lay2, lay2];

slayout5x5 = size(layout5x5);
R = slayout5x5(1);
C = slayout5x5(2);

nSteps5x5 = 2*period + mod(nSteps,period);
endPositions = getendpositions(layout5x5, nSteps5x5);

R5 = R/5;
C5 = C/5;
shards = NaN(5);
for r = 0:4
    for c = 0:4
        endPositionsTmp = endPositions(r*R5+[1:R5],c*C5+[1:C5]);
        shards(r+1,c+1) = sum(endPositionsTmp(:));
    end
end

arrows = shards((end+1)/2,1) + shards((end+1)/2,end) + shards(1,(end+1)/2) + shards(end,(end+1)/2);
smallCorners = shards((end+1)/2-1,1) + shards((end+1)/2-1,end) + shards((end+1)/2+1,1) + shards((end+1)/2+1,end);
largeCorners = shards((end+1)/2-1,2) + shards((end+1)/2-1,end-1) + shards((end+1)/2+1,2) + shards((end+1)/2+1,end-1);
full = [shards((end+1)/2,(end+1)/2), shards((end+1)/2+1,(end+1)/2)];

countSteps = 0;
modSteps = floor(nSteps/period);
evenOddOffset = mod(modSteps,2) + 1;
getFull = @(n) full(mod(n+evenOddOffset,2)+1);
countSteps = countSteps + getFull(1);
for n = 2:modSteps
    countSteps = countSteps + (n-1) * 4 * getFull(n);
end

countSteps = countSteps + arrows;
countSteps = countSteps + modSteps * smallCorners;
countSteps = countSteps + (modSteps-1) * largeCorners;

resultPart2 = countSteps
