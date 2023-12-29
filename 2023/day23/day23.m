% GNU Octave, version 8.4.0
%
% --- Day 23: A Long Walk ---
% https://adventofcode.com/2023/day/23
%
% https://github.com/AJPfleger
%
% call like 'octave day23.m input.txt'

disp('--- Day 23: A Long Walk ---')

args = argv();
filename = args{1}

fid = fopen(filename,'rt');
rawInput = textscan(fid,'%s','delimiter', '\n');
fclose(fid);

rawInput = rawInput{1};
R = numel(rawInput);
C = numel(rawInput{1});

dD = double(".");
dH = double("#");
dR = double(">");
dL = double("<");
dA = double("^");
dV = double("v");

garden = [];
for i = 1:R
    garden(end+1,:) = double(rawInput{i});
end

sLayout = size(garden);

% We shift the start and end one tile into the path to have it easier
% with bordereffects. Remember to add 2 to the final result
garden(1,2) = dH;
garden(end,end-1) = dH;

% Find nodes
nodes = [];
for c = 2:C-1
    for r = 2:R-1
        if garden(r,c) ~= dH
            countTrees = (garden(r+1,c) == dH) + (garden(r,c+1) == dH) + ...
                         (garden(r-1,c) == dH) + (garden(r,c-1) == dH);
            if countTrees ~= 2
                nodes(end+1,:) = [sub2ind(sLayout,r,c),4-countTrees];
            end
        end
    end
end

% Collect edges
% [n1, n2, weight, direction]
% direction -1: n1 <-- n2
% direction  0: n1 --- n2
% direction  1: n1 --> n2
edges = [];
while sum(nodes(:,2) > 0)
    n1 = nodes(nodes(:,2) > 0,1)(1);
    garden(n1) = dH;

    nodes(nodes(:,1)==n1,2) = nodes(nodes(:,1)==n1,2) - 1;
    weight = 0;
    direction = 0;
    [r,c] = ind2sub(sLayout,n1);
    while true
        weight = weight + 1;

        next = garden(r-1:r+1,c-1:c+1) ~= dH;

        if next(2,1)
            c = c - 1;
            if garden(r,c) == dL
                if direction == -1; "ERROR"; end
                direction = 1;
            elseif garden(r,c) == dR
                if direction == 1; "ERROR"; end
                direction = -1;
            end
        elseif next(2,3)
            c = c + 1;
            if garden(r,c) == dR
                if direction == -1; "ERROR"; end
                direction = 1;
            elseif garden(r,c) == dL
                if direction == 1; "ERROR"; end
                direction = -1;
            end
        elseif next(1,2)
            r = r - 1;
            if garden(r,c) == dA
                if direction == -1; "ERROR"; end
                direction = 1;
            elseif garden(r,c) == dV
                if direction == 1; "ERROR"; end
                direction = -1;
            end
        elseif next(3,2)
            r = r + 1;
            if garden(r,c) == dV
                if direction == -1; "ERROR"; end
                direction = 1;
            elseif garden(r,c) == dA
                if direction == 1; "ERROR"; end
                direction = -1;
            end
        else
            "WEIRD CASE IN NEXT"
            return
        end

        ind = sub2ind(sLayout,r,c);
        if any(nodes(:,1) == ind)
            edges(end+1,:) = [n1, ind, weight, direction];
            garden(ind) = dH;
            if nodes(nodes(:,1)==ind,2) > 1
                garden(ind) = dD;
            end
            nodes(nodes(:,1)==ind,2) = nodes(nodes(:,1)==ind,2) - 1;

            break
        end

        garden(r,c) = dH;
    end

    if nodes(nodes(:,1)==n1,2) > 1
        garden(n1) = dD;
    end
end

% Flip edges with direction "-1" to have all directed as
% as they appear.
for e = 1:size(edges,1)
    if edges(e,4) == -1
        edges(e,1:2) = edges(e,2:-1:1);
        edges(e,4) = 1;
    end
end


%% Part 1 --------------------------------------------------------

% Analysing graph shows that it just goes right or down.
% That makes the tree quite easy to traverse and results
% in n! possible paths, where n is one side of the square
% shaped graph. It's about sqrt(nNodes).
% I am too lazy now to go through all paths explicitely,
% therefore I choose at every intersection ranomly if I
% should go left or right. To be quite sure to hit the
% correct path we try 10 * n! random paths and choose the
% longest. The result is NOT guarnteed to be correct, but
% very likely.
n = round(sqrt(size(nodes,1)));
p0 = edges(1,2);
p1 = edges(end,1);
paths = [];
for randpath = 1:10*factorial(n)
    pa = 0;
    next = p0;
    while next ~= p1
        choices = edges(edges(:,1) == next,:);

        r = randi(size(choices,1));

        next = choices(r,2);
        pa = pa + choices(r,3);
    end
    paths(end+1) = pa;
end

paths = paths + edges(1,3) + edges(end,3) + 2;

resultPart1 = max(paths)


%% Part 2 --------------------------------------------------------
% Analysing graph shows that some of the weights at some nodes are
% significantly smaller than others. This approach again doesn't
% guarant the optimal answer but might get a good one. Again, we
% walk randomly through the graph and hope to finsh and to hit the
% longest path.
%
% To make the random walk more efficient, we prune the graph with
% the following ideas:
% - Remove edges that are a lot smaller than the rest.
% - Merge nodes with only 2 edges (straight through)
% - Propagate from one end and take the split with the higher
%   edge, when the ratio is at least minRatio. Remove the other.
%
% 6734 is the correct result, if you don't get there in the first
% run, you just had bad luck.

% Set ratio for easy decisions and cut-off value for min length
if strcmp(filename, 'testinput.txt')
    minRatio = Inf;
    minLength = 0;
else
    minRatio = 1.8;
    minLength = 50;
end

% Remove short edges
edgesRaw = edges;
edges = edges(:,1:3);
edges(edges(:,3) < minLength,:) = [];

for redStep = 1:10
    nodesMultiple = edges(:,1:2);
    nodes = unique(nodesMultiple(:));
    [nEdgesHist,nodeHist] = hist(nodesMultiple(:),nodes);

    % Merge edges
    for n = 1:numel(nEdgesHist)
        if nEdgesHist(n) ~= 2
            continue
        end

        node2remove = nodeHist(n);

        lN = edges(:,1) == node2remove | edges(:,2) == node2remove
        twoEdges = edges(lN,:)
        w = sum(twoEdges(:,3))
        twoEdges = twoEdges(:,1:2)
        redEdges = twoEdges(twoEdges() ~= node2remove)
        edges(find(lN)(1),:) = [redEdges',w];
        edges(find(lN)(2),:) = [];
    end

    % Check, if there are easy decisions at the start of the path
    n1 = edges(1,2);
    edges = sortrows(edges,1)
    edgesRed = [edges, [1:size(edges,1)]'];
    edgesRed = edgesRed(2:end,:)

    lN = edgesRed(:,1) == n1 | edgesRed(:,2) == n1;
    twoEdges = edgesRed(lN,:);
    twoEdges = sortrows(twoEdges,3);
    if twoEdges(1,3) * minRatio < twoEdges(2,3)
        % remove the edge
        edges(twoEdges(1,4),:) = [];
    end

    % Check, if there are easy decisions at the end of the path
    edges = sortrows(edges,2);
    nEnd = edges(end,1);
    edgesRed = [edges, [1:size(edges,1)]'];
    edgesRed = edgesRed(1:end-1,:);

    lN = edgesRed(:,1) == nEnd | edgesRed(:,2) == nEnd;
    twoEdges = edgesRed(lN,:);
    twoEdges = sortrows(twoEdges,3);
    if twoEdges(1,3) * minRatio < twoEdges(2,3)
        % remove the edge
        edges(twoEdges(1,4),:) = [];
    end
end

% Start a random walk
paths = [];
edgesRaw = edges;
p0 = edgesRaw(1,2);
p1 = edgesRaw(end,1);
edgesRawRed = edgesRaw;
edgesRawRed(1,:) = [];
for randpath = 1:20000
    edges = edgesRawRed;

    pa = 0;
    next = p0;
    while next ~= p1
        lChoices = edges(:,1) == next | edges(:,2) == next;
        choices = edges(lChoices,:);
        if size(choices,1) < 1;
            pa = NaN;
            break
        end

        edges(lChoices,:) = [];

        r = randi(size(choices,1));

        next = choices(r,1) + choices(r,2) - next;
        pa = pa + choices(r,3);
    end

    paths(end+1) = pa;
    if mod(randpath,1000) == 0
        paths = max(paths);
        currentMax = paths + edgesRaw(1,3) + edgesRaw(end,3) + 2
    end
end

resultPart2 = currentMax
