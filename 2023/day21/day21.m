% GNU Octave, version 8.4.0
%
% --- Day 21: Step Counter ---
% https://adventofcode.com/2023/day/21
%
% https://github.com/AJPfleger
%
% call like 'octave day21.m input.txt'

disp('--- Day 21: Step Counter ---')

args = argv();
filename = args{1}

fid = fopen(filename,'rt');
rawInput = textscan(fid,'%s','delimiter', '\n');
fclose(fid);

rawInput = rawInput{1};
R = numel(rawInput);
C = numel(rawInput{1});

dO = double("O");
dD = double(".");

layout = [];
for i = 1:R
    layout(end+1,:) = double(rawInput{i});
end

sLayout = size(layout);


%% Part 1 --------------------------------------------------------

nSteps = 64;
layout(layout == double('S')) = dO;

[r,c] = ind2sub(sLayout, layout == dO);
oList = [r,c]

for s = 1:nSteps
    oListNew = [];

    for o = 1:size(oList,1)
        % do all 4 directions directly, because it is faster than
        % a beautiful loop

        rx = oList(o,1);
        cx = oList(o,2);

        c = cx;
        r = rx + 1;
        if r >= 1 && r <= R && layout(r,c) == dD
            layout(r,c) = dO;
            oListNew(end+1,:) = [r,c];
        end

        r = rx - 1;
        if r >= 1 && r <= R && layout(r,c) == dD
            layout(r,c) = dO;
            oListNew(end+1,:) = [r,c];
        end

        r = rx;
        c = cx + 1;
        if c >= 1 && c <= C && layout(r,c) == dD
            layout(r,c) = dO;
            oListNew(end+1,:) = [r,c];
        end

        c = cx - 1;
        if c >= 1 && c <= C && layout(r,c) == dD
            layout(r,c) = dO;
            oListNew(end+1,:) = [r,c];
        end
    end

    oList = oListNew;
end

lO = layout == dO;
checkboardmatrix = (1:R)' + (1:C) + mod(nSteps,2) + 1;
checkboardmatrix = logical(mod(checkboardmatrix,2));
endSteps = lO & checkboardmatrix;

resultPart1 = sum(endSteps(:))


%% Part 2 --------------------------------------------------------
% Needs some more thinking
