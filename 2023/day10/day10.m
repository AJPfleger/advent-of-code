% GNU Octave, version 8.4.0
%
% --- Day 10: Pipe Maze ---
% https://adventofcode.com/2023/day/10
%
% https://github.com/AJPfleger
%
% call like 'octave day10.m input.txt'

disp('--- Day 10: Pipe Maze ---')

args = argv();
filename = args{1}

fid = fopen(filename,'rt');
rawInput = textscan(fid,'%s','delimiter', '\n');
fclose(fid);

rawInput = rawInput{1};
R = numel(rawInput)+2;
C = numel(rawInput{1})+2;
sizeRC = [R,C];

Map = NaN(sizeRC);
for l = 1:numel(rawInput)
    line = rawInput{l};
    Map(l+1,2:end-1) = double(line);
end

dF = double('F');
d7 = double('7');
dL = double('L');
dJ = double('J');
dH = double('-');
dV = double('|');
dS = double('S');

% Replace empty spaces
Map(Map == double('.')) = NaN;

% Remove unconnected pipes
lS = Map == dS;
sumOld = -1;
sumNew = sum(isnan(Map(:)));
while sumOld ~= sumNew
    sumOld = sumNew;

    lF = Map == dF;
    l7 = Map == d7;
    lL = Map == dL;
    lJ = Map == dJ;
    lH = Map == dH;
    lV = Map == dV;
    l0 = isnan(Map);

    m = NaN(R-2,C-2);

    rRange = 2:R-1;
    cRange = 2:C-1;

    l1 = lL | lJ | lV | lS;
    l2 = lJ | l7 | lH | lS;
    l = lF(rRange,cRange) & l1(rRange+1,cRange) & l2(rRange,cRange+1);
    m(l~=0) = dF;

    l1 = lL | lJ | lV | lS;
    l2 = lL | lF | lH | lS;
    l = l7(rRange,cRange) & l1(rRange+1,cRange) & l2(rRange,cRange-1);
    m(l~=0) = d7;

    l1 = lF | l7 | lV | lS;
    l2 = lJ | l7 | lH | lS;
    l = lL(rRange,cRange) & l1(rRange-1,cRange) & l2(rRange,cRange+1);
    m(l~=0) = dL;

    l1 = lF | l7 | lV | lS;
    l2 = lL | lF | lH | lS;
    l = lJ(rRange,cRange) & l1(rRange-1,cRange) & l2(rRange,cRange-1);
    m(l~=0) = dJ;

    l1 = lF | l7 | lV | lS;
    l2 = lJ | lL | lV | lS;
    l = lV(rRange,cRange) & l1(rRange-1,cRange) & l2(rRange+1,cRange);
    m(l~=0) = dV;

    l1 = lF | lL | lH | lS;
    l2 = lJ | l7 | lH | lS;
    l = lH(rRange,cRange) & l1(rRange,cRange-1) & l2(rRange,cRange+1);
    m(l~=0) = dH;

    Map(rRange,cRange) = m;
    Map(lS) = dS;

    sumNew = sum(isnan(Map(:)));
end

mapping = [];
for r = 2:R-1
    for c = 2:C-1
        if ~isnan(Map(r,c))

            switch Map(r,c)
                case dF
                    shiftRC = [1,0,0,1];
                case d7
                    shiftRC = [1,0,0,-1];
                case dL
                    shiftRC = [-1,0,0,1];
                case dJ
                    shiftRC = [-1,0,0,-1];
                case dH
                    shiftRC = [0,-1,0,1];
                case dV
                    shiftRC = [-1,0,1,0];
                otherwise
                    % TODO get S from input
                    shiftRC = [1,0,1,0];
                    startIdx = sub2ind(sizeRC,r,c);
            end

            mapping(end+1,:) = [r,c,r,c,r,c] + [0,0,shiftRC];
        end
    end
end

mappingIdx = [sub2ind(sizeRC,mapping(:,1),mapping(:,2)), sub2ind(sizeRC,mapping(:,3),mapping(:,4)), sub2ind(sizeRC,mapping(:,5),mapping(:,6))];


%% Part 1 --------------------------------------------------------
% Walk starting from point S along the pipe and collect all pipe positions

pathIdx = startIdx;
keepWalking = true;
while keepWalking
    posIdx = mappingIdx(mappingIdx(:,1) == pathIdx(end),:);

    if ~any(pathIdx == posIdx(2))
        pathIdx(end+1) = posIdx(2);
    elseif~any(pathIdx == posIdx(3))
        pathIdx(end+1) = posIdx(3);
    else
        break;
    end
end

resultPart1 = numel(pathIdx)/2


%% Part 2 --------------------------------------------------------
% 1.  Take path from the walk before to idetify, which pipe segments
%     don't belong to the main pipe (in case of multiple loops)
% 2.  Flood the map and mark positions outside the pipe with Inf
% 3.  Collect all vertices from the remaing pipe.
% 4.  Check for all remaining undefined positions if they are inside,
%     using a winding number approach:
% 4.a Calculate for each position the sum of angles to all vertices.
%     If that sum ist ~0, then the point is not included.
% 4.b Flood again with a new seed. This should be faster than computing
%     all angles, espcially for larger areas.

% Remove inner loops
for i = 1:size(mappingIdx,1)
    posIdx = mappingIdx(i,:);
    if ~any(pathIdx == posIdx(1))
        Map(posIdx(1)) = NaN;
    end
end

% Flooding
Map([1,end],:) = Inf;
Map(:,[1,end]) = Inf;

changed = true;
while changed
    changed = false;
    nanIdx = find(isnan(Map));
    for i = 1:numel(nanIdx)
        [r2,c2] = ind2sub(sizeRC,nanIdx(i));
        if  (isinf(Map(r2-1,c2)) || isinf(Map(r2,c2-1)) || isinf(Map(r2+1,c2)) || isinf(Map(r2,c2+1)))
            Map(r2,c2) = Inf;
            changed = true;
            % "skipped a lookup -> Inf"
        end
    end
end

% prepare vertices
lF = Map == dF;
l7 = Map == d7;
lL = Map == dL;
lJ = Map == dJ;
lVert = lF | l7 | lL | lJ | lS;

% get vertices in order
vert = [];
for p = 1:numel(pathIdx)
    if lVert(pathIdx(p))
        vert(end+1) = pathIdx(p);
    end
end
vert(end+1) = vert(1);
[r,c] = ind2sub(sizeRC,vert.');
vert = [vert.',r,c];
sizeVert = size(vert(:,1));

for r = 2:R-1
    for c = 2:C-1

        if isnan(Map(r,c))
            P0 = [r, c];
            phi = zeros(sizeVert);
            for p = 1:size(vert,1)-1
                P1 = vert(p,2:3);
                P2 = vert(p+1,2:3);

                v1 = P1 - P0;
                v2 = P2 - P0;

                % det([v1;v2]) is cross product in 2D
                phi(p) = atan2d(det([v1;v2]),dot(v1,v2));
            end

            if abs(sum(phi)) < 1e-7
                Map(r,c) = Inf;
            else
                Map(r,c) = 0;
            end

            % More flooding
            changed = true;
            while changed
                changed = false;
                nanIdx = find(isnan(Map));
                for i = 1:numel(nanIdx)
                    [r2,c2] = ind2sub(sizeRC,nanIdx(i));
                    if  (isinf(Map(r2-1,c2)) || isinf(Map(r2,c2-1)) || isinf(Map(r2+1,c2)) || isinf(Map(r2,c2+1)))
                        Map(r2,c2) = Inf;
                        changed = true;
                        % "skipped a lookup -> Inf"
                    elseif ((Map(r2-1,c2) == 0) || (Map(r2,c2-1) == 0) || (Map(r2+1,c2) == 0) || (Map(r2,c2+1)) == 0)
                        Map(r2,c2) = 0;
                        changed = true;
                        % "skipped a lookup -> 0"
                    end
                end
            end
        end
    end
end
printpipemap(Map)

resultPart2 = sum(Map(:) == 0)
