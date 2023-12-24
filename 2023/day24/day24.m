% GNU Octave, version 8.4.0
%
% --- Day 24: Never Tell Me The Odds ---
% https://adventofcode.com/2023/day/24
%
% https://github.com/AJPfleger
%
% call like 'octave day24.m input.txt'

disp('--- Day 24: Never Tell Me The Odds ---')

format long

args = argv();
filename = args{1}

rawInput = dlmread(filename,[',','@']);


%% Part 1 --------------------------------------------------------

if strcmp(filename, 'testinput.txt')
    area = [7,27]
else
    area = [200000000000000, 400000000000000]
end

pxy = rawInput(:,1:2);
vxy = rawInput(:,4:5);

% find intersections
intersects = 0;
for f = 1:size(pxy,1)
    A = pxy(f,:);
    v = vxy(f,:);
    for f2 = f+1:size(pxy,1)
        B = pxy(f2,:);
        w = vxy(f2,:);

        vXw = v(1)*w(2) - w(1)*v(2);

        % "parallel"
        if vXw == 0
            continue
        end

        AB = A - B;

        lambda = (w(1)*AB(2) - AB(1)*w(2)) / vXw;
        kappa = (v(1)*AB(2) - AB(1)*v(2)) / vXw;

        % "intersects in past"
        if lambda < 0 || kappa < 0
            continue
        end

        P = A + lambda * v;

        if all(P >= area(1)) && all(P <= area(2))
            intersects = intersects + 1;
        end
    end
end

resultPart1 = intersects


%% Part 2 --------------------------------------------------------

% WIP
