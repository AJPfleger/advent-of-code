% GNU Octave, version 8.4.0
%
% --- Day 14: Parabolic Reflector Dish ---
% https://adventofcode.com/2023/day/14
%
% https://github.com/AJPfleger
%
% call like 'octave day14.m input.txt'

disp('--- Day 14: Parabolic Reflector Dish ---')

args = argv();
filename = args{1}

fid = fopen(filename,'rt');
rawInput = textscan(fid,'%s','delimiter', '\n');
fclose(fid);

rawInput = rawInput{1};
R = numel(rawInput);


%% Part 1 --------------------------------------------------------

pf = [];
for i = 1:R
    pf(end+1,:) = double(rawInput{i});
end

movement = true;
while movement
    movement = false;
    for r = 2:R
        for c = find(pf(r,:) == double('O'))

            if pf(r-1,c) == double('.')
                movement = true;
                pf(r-1,c) = double('O');
                pf(r,c) = double('.');
            end
        end
    end
end

lO = pf == double('O');
resultPart1 = sum(sum(lO,2) .* [R:-1:1].')


%% Part 2 --------------------------------------------------------

cycles = 1000000000;

pf = [];
for i = 1:R
    pf(end+1,:) = double(rawInput{i});
end

positions = []
for i = 1:cycles
    pf = spincycle(pf);

    posCurrent = find(pf == double('O')).';
    positions;

    if size(positions,1) > 1 && any(all(positions == posCurrent,2))
        all(positions == posCurrent,2);
        offset = find(all(positions == posCurrent,2));
        period = i - offset;
        break
    else
        positions(end+1,:) = posCurrent;
    end
end

posFinal = mod(cycles - offset,period);
rocks = zeros(size(pf));
rocks(positions(offset+posFinal,:)) = double('O');

lO = rocks == double('O');
resultPart2 = sum(sum(lO,2) .* [R:-1:1].')
