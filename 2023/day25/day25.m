% GNU Octave, version 8.4.0
%
% --- Day 25: Snowverload ---
% https://adventofcode.com/2023/day/25
%
% https://github.com/AJPfleger
%
% call like 'octave day25.m input.txt'

disp('--- Day 25: Snowverload ---')

args = argv();
filename = args{1}

fid = fopen(filename,'rt');
rawInput = textscan(fid,'%s','delimiter', '\n');
fclose(fid);

rawInput = rawInput{1};

edgesRaw = [];
for r = 1:size(rawInput,1);
    ss = strsplit(rawInput{r},' ');
    node1 = hashstring(ss{1}(1:3));

    for n2 = 2:numel(ss)
        edgesRaw(end+1,:) = [node1, hashstring(ss{n2}(1:3))];
    end
end

nEdges = size(edgesRaw,1)
nNodes = numel(unique(edgesRaw(:)))

edgesRaw = [edgesRaw,(1:nEdges)'];

%% Karger's Algorithm
attempt = 0;
while true
    edges = edgesRaw;
    attempt = attempt + 1
    while numel(unique(edges(:,1:2)(:))) > 2
        % merge nodes
        r = randi(size(edges,1));
        edges(edges == edges(r,1)) = edges(r,2);

        % remove self-edges
        edges(edges(:,1) == edges(:,2),:) = [];
    end

    if size(edges,1) == 3
        break
    end
end

cuts = edges(:,3);

edges = edgesRaw;
edges(cuts,:) = [];

con = edges(1,1);
while numel(con) > 0
    for c = 1:numel(con)
        edges(edges == con(c)) = 0;
    end
    % remove self-edges
    edges(edges(:,1) == edges(:,2),:) = [];

    con = [edges(edges(:,1) == 0,2); edges(edges(:,2) == 0,1)];
end

setsize = numel(unique(edges(:,1:2)(:)))

resultPart1 = setsize * (nNodes - setsize)

resultPart2 = "Today, there is no part 2."
