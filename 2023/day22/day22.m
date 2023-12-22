% GNU Octave, version 8.4.0
%
% --- Day 22: Sand Slabs ---
% https://adventofcode.com/2023/day/22
%
% https://github.com/AJPfleger
%
% call like 'octave day22.m input.txt'

disp('--- Day 22: Sand Slabs ---')

args = argv();
filename = args{1}

rawInput = dlmread(filename,[',','~']);
nBricks = size(rawInput,1);

cor = rawInput;

if any((cor(:,4:6) - cor(:,1:3)) < 0)
    "some blocks pointing in the wrong direction"
    return
end

cor = sortrows(cor,[3,1]);

%% Settle bricks -------------------------------------------------

tic
r = 0;
while r < nBricks
    r = r + 1;

    if cor(r,3) == 1
        continue
    end

    brick = cor(r,:);
    supported = false;
    z = brick(3)-1;
    zbricks = cor(cor(:,6) == z,:);
    for rcheck = 1:size(zbricks,1)
        if all(brick(1:2) <= zbricks(rcheck,4:5)) && all(zbricks(rcheck,1:2) <= brick(4:5))
            supported = true;
            break
        end
    end

    if ~supported
        cor(r,3) = cor(r,3)-1;
        cor(r,6) = cor(r,6)-1;
        r = r-1;
    end
end
toc

cor = sortrows(cor,[3,1]);
corStable = cor;


%% Part 1 --------------------------------------------------------

tic
countSafe = [];
for rm = 1:size(corStable,1)

    cor = corStable;
    za = cor(rm,6) + 1;
    cor(rm,:) = [];

    movement = false;

    bricksAbove = cor(cor(:,3) == za,:);
    for r = 1:size(bricksAbove,1)

        brick = bricksAbove(r,:);

        supported = false;
        z = brick(3)-1;

        zbricks = cor(cor(:,6) == z,:);
        for rcheck = 1:size(zbricks,1)
            if all(brick(1:2) <= zbricks(rcheck,4:5)) && all(zbricks(rcheck,1:2) <= brick(4:5))
                supported = true;
                break
            end
        end

        if ~supported
            movement = true;
            break
        end
    end

    countSafe(end+1) = ~movement;
end
toc

resultPart1 = sum(countSafe)


%% Part 2 --------------------------------------------------------

tic
fallingBricks = 0;
for b = 1:size(corStable,1)
    cor = corStable;
    cor(b,:) = [];

    for r = 1:nBricks-1

        if cor(r,3) == 1
            continue
        end

        brick = cor(r,:);
        supported = false;
        z = brick(3)-1;
        zbricks = cor(cor(:,6) == z,:);
        for rcheck = 1:size(zbricks,1)
            if all(brick(1:2) <= zbricks(rcheck,4:5)) && all(zbricks(rcheck,1:2) <= brick(4:5))
                supported = true;
                break
            end
        end

        if ~supported
            fallingBricks = fallingBricks + 1;
            cor(r,:) = NaN;
        end
    end
end
toc

resultPart2 = sum(fallingBricks)
