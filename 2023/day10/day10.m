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
N = numel(rawInput)+2
Map = NaN(numel(rawInput)+2, numel(rawInput{1})+2);
for l = 1:numel(rawInput)
    line = rawInput{l};
    Map(l+1,2:end-1) = double(line);
end


%% Part 1 --------------------------------------------------------

% remove empty spaces
Map(Map == double('.')) = NaN;

% remove unconnected pipes
lS = Map == double('S');
sumOld = -1;
sumNew = sum(isnan(Map(:)));

"***** start replacement *****"

sumOld = -1
sumNew = sum(isnan(Map(:)))
while sumOld ~= sumNew
    sumOld = sumNew;

    lF = Map == double('F');
    l7 = Map == double('7');
    lL = Map == double('L');
    lJ = Map == double('J');
    lH = Map == double('-');
    lV = Map == double('|');
    l0 = isnan(Map);

    m = NaN(N-2,N-2);

    d = 2:N-1;

    l1 = lL + lJ + lV + lS;
    l2 = lJ + l7 + lH + lS;
    l1(d+1,d) .+ l2(d,d+1);
    l = lF(d,d) .* (l1(d+1,d) .* l2(d,d+1));
    m(l~=0) = double('F');

    l1 = lL + lJ + lV + lS;
    l2 = lL + lF + lH + lS;
    l1(d+1,d) .+ l2(d,d+1);
    l = l7(d,d) .* (l1(d+1,d) .* l2(d,d-1));
    m(l~=0) = double('7');

    l1 = lF + l7 + lV + lS;
    l2 = lJ + l7 + lH + lS;
    l1(d+1,d) .+ l2(d,d+1);
    l = lL(d,d) .* (l1(d-1,d) .* l2(d,d+1));
    m(l~=0) = double('L');

    l1 = lF + l7 + lV + lS;
    l2 = lL + lF + lH + lS;
    l1(d+1,d) .+ l2(d,d+1);
    l = lJ(d,d) .* (l1(d-1,d) .* l2(d,d-1));
    m(l~=0) = double('J');

    l1 = lF + l7 + lV + lS;
    l2 = lJ + lL + lV + lS;
    l1(d+1,d) .+ l2(d,d+1);
    l = lV(d,d) .* (l1(d-1,d) .* l2(d+1,d));
    m(l~=0) = double('|');

    l1 = lF + lL + lH + lS;
    l2 = lJ + l7 + lH + lS;
    l1(d+1,d) .+ l2(d,d+1);
    l = lH(d,d) .* (l1(d,d-1) .* l2(d,d+1));
    m(l~=0) = double('-');


    Map(d,d) = m;
    Map(lS) = double('S');

    sumNew = sum(isnan(Map(:)));
    Map;
end

resultPart1max = sum(!isnan(Map(:)))/2

mapping = []

for r = 2:N-1
    for c = 2:N-1
        if ~isnan(Map(r,c))

            switch Map(r,c)
                case double('F')
                    r1 = 1;
                    c1 = 0;
                    r2 = 0;
                    c2 = 1;
                case double('7')
                    r1 = 1;
                    c1 = 0;
                    r2 = 0;
                    c2 = -1;
                case double('L')
                    r1 = -1;
                    c1 = 0;
                    r2 = 0;
                    c2 = 1;
                case double('J')
                    r1 = -1;
                    c1 = 0;
                    r2 = 0;
                    c2 = -1;
                case double('-')
                    r1 = 0;
                    c1 = -1;
                    r2 = 0;
                    c2 = 1;
                case double('|')
                    r1 = -1;
                    c1 = 0;
                    r2 = 1;
                    c2 = 0;
                otherwise
                    disp('####### S ######')
                    r1 = 1;
                    c1 = 0;
                    r2 = NaN;
                    c2 = NaN;
                    start = r * 1000 + c;


            end
            mapping(end+1,:) = [r,c,r+r1,c+c1,r+r2,c+c2];
        end
    end
end

mapping = mapping(:,1:2:5) * 1000 + mapping(:,2:2:6);

%walk
path = start;
keepWalking = true;
while keepWalking
    pos = mapping(mapping(:,1) == path(end),:);

    if ~any(path == pos(2))
        path(end+1) = pos(2);
    elseif~any(path == pos(3))
        path(end+1) = pos(3);
    else
        break;
    end
end
path;
resultPart1 = numel(path)/2


%% Part 2 --------------------------------------------------------

%remove inner loops
removeCount = 0
for i = 1:size(mapping,1)
    pos = mapping(i,:);
    if ~any(path == pos(1))
        r = idivide(pos(1),int32(1000));
        c = mod(pos(1),1000);
        Map(r,c) = NaN;
        removeCount = removeCount + 1;
    end
end


Map([1,end],:) = Inf;
Map(:,[1,end]) = Inf;


changed = true;
while changed
    changed = false;
    for r = 2:N-1
        for c = 2:N-1
            if isnan(Map(r,c)) && (isinf(Map(r-1,c)) || isinf(Map(r,c-1)) || isinf(Map(r+1,c)) || isinf(Map(r,c+1)))
                Map(r,c) = Inf;
                changed = true;
            end
        end
    end
end


%% winding number
lF = Map == double('F');
l7 = Map == double('7');
lL = Map == double('L');
lJ = Map == double('J');
lVert = lF + l7 + lL + lJ + lS

% get vertices in order
vert = [];
for p = 1:numel(path)
    r = idivide(path(p),int32(1000));
    c = mod(path(p),1000);
    if lVert(r,c)
        vert(end+1,:) = [path(p),r,c];
    end
end
vert(end+1,:) = vert(1,:);



for r = 2:N-1
    for c = 2:N-1
        if isnan(Map(r,c))
            phi = 0;
            P0 = [r, c];
            for p = 1:size(vert,1)-1
                P1 = vert(p,2:3);
                P2 = vert(p+1,2:3);

                v1 = P1 - P0;
                v2 = P2 - P0;

%                x = cross(v1,v2);
                x = det([v1;v2]);
                cx = sign(x) * norm(x);
                theta = atan2d(cx,dot(v1,v2));
                phi = phi + theta;

            end
            [P0, phi]
            if abs(phi) < 1e-7
                "not"
                Map(r,c) = Inf;
            else
                Map(r,c) = 0;
            end

            changed = true;
            while changed
                changed = false;
                for r2 = 2:N-1
                    for c2 = 2:N-1
                        if isnan(Map(r2,c2)) && (isinf(Map(r2-1,c2)) || isinf(Map(r2,c2-1)) || isinf(Map(r2+1,c2)) || isinf(Map(r2,c2+1)))
                            Map(r2,c2) = Inf;
                            changed = true;
                            "skipped a lookup -> Inf"
                        elseif isnan(Map(r2,c2)) && ((Map(r2-1,c2) == 0) || (Map(r2,c2-1) == 0) || (Map(r2+1,c2) == 0) || (Map(r2,c2+1)) == 0)
                            Map(r2,c2) = 0;
                            changed = true;
                            "skipped a lookup -> 0"
                        end
                    end
                end
            end
        end
    end
end
printpipemap(Map)

resultPart2 = sum(Map(:) == 0)
