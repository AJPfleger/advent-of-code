% GNU Octave, version 8.4.0
%
% --- Day 11: Cosmic Expansion ---
% https://adventofcode.com/2023/day/11
%
% https://github.com/AJPfleger
%
% call like 'octave day11.m input.txt'

disp('--- Day 11: Cosmic Expansion ---')

format long

args = argv();
filename = args{1}

fid = fopen(filename,'rt');
rawInput = textscan(fid,'%s','delimiter', '\n');
fclose(fid);

rawInput = rawInput{1};

universe = [];
for l = 1:numel(rawInput)
    universe(end+1,:) = double(rawInput{l});
end

uniSize = size(universe);
galaxiesIdx = find(universe == double('#'));
[rGalaxiesRaw,cGalaxiesRaw] = ind2sub(uniSize,galaxiesIdx);

rEmpty = [];
cEmpty = [];
for r = 1:uniSize(1)
    if ~any(universe(r,:) == double('#'))
        rEmpty(end+1) = r;
    end
end
for c = 1:uniSize(2)
    if ~any(universe(:,c) == double('#'))
        cEmpty(end+1) = c;
    end
end


%% Part 1 --------------------------------------------------------
expansionFactor = 2

rGalaxies = rGalaxiesRaw;
cGalaxies  = cGalaxiesRaw;
for r = rEmpty(end:-1:1)
    rGalaxies = rGalaxies + int64(rGalaxies > r) .* (expansionFactor-1);
end
for c = cEmpty(end:-1:1)
    cGalaxies  = cGalaxies  + int64(cGalaxies  > c) .* (expansionFactor-1);
end

galaxiesCoordinates = [rGalaxies ,cGalaxies ];

dists = [];
for g = 1:size(galaxiesCoordinates,1)-1
    diffs = abs(galaxiesCoordinates(g+1:end,:) - galaxiesCoordinates(g,:));
    dists = [dists;sum(diffs,2)];
end

resultPart1 = sum(dists)


%% Part 2 --------------------------------------------------------
expansionFactor = 1000000

rGalaxies = rGalaxiesRaw;
cGalaxies  = cGalaxiesRaw;
for r = rEmpty(end:-1:1)
    rGalaxies = rGalaxies + int64(rGalaxies > r) .* (expansionFactor-1);
end
for c = cEmpty(end:-1:1)
    cGalaxies  = cGalaxies  + int64(cGalaxies  > c) .* (expansionFactor-1);
end

galaxiesCoordinates = [rGalaxies ,cGalaxies ];

dists = [];
for g = 1:size(galaxiesCoordinates,1)-1
    diffs = abs(galaxiesCoordinates(g+1:end,:) - galaxiesCoordinates(g,:));
    dists = [dists;sum(diffs,2)];
end

resultPart2 = sum(dists)
