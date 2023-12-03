% GNU Octave, version 8.4.0
%
% --- Day 2: Cube Conundrum ---
% https://adventofcode.com/2023/day/2
%
% https://github.com/AJPfleger
%
% call like 'octave day02.m input.txt'

disp('--- Day 2: Cube Conundrum ---')

args = argv();
filename = args{1}

fid = fopen(filename,'rt');
rawInput = textscan(fid,'%s','delimiter', '\n');
fclose(fid);

rawInput = rawInput{1};
nGames = numel(rawInput)

%only 12 red cubes, 13 green cubes, and 14 blue cubes
colorsFull = {'red', 'green', 'blue'};
colors = {'r','g','b'};
nColors = numel(colors);
colorsMaxCubes = [12, 13, 14];

v = logical(ones(nGames,1));
minCubes = zeros(nGames, numel(colors));
for iGame = 1:nGames
    game = rawInput{iGame};
    % remove 'Game n:'
    game = textscan(game,'%s','delimiter',':');
    game = game{1}{2};

    % Replace colors
    for c = 1:nColors
        game = strrep(game,colorsFull{c},colors{c});
    end

    gameRev = reverse(game);

    gameRevCells = textscan(gameRev,'%s','delimiter',';');
    gameRevCells = gameRevCells{1};

    for iDraw = 1:numel(gameRevCells)
        draw = textscan(gameRevCells{iDraw},'%s','delimiter',',');
        draw = cell2mat(draw);

        for iCube = 1:numel(draw)
            cxn = draw{iCube};
            nCubes = reverse(cxn(3:end));
            nCubes = str2num(nCubes);

            for c = 1:nColors
                % part 1
                if cxn(1) == colors{c} && nCubes > colorsMaxCubes(c)
                    v(iGame) = 0;
                    % part 1 could have a break conditions if run separately
                end

                % part 2
                if cxn(1) == colors{c} && nCubes > minCubes(iGame,c)
                    minCubes(iGame,c) = nCubes;
                end
            end
        end
    end
end

gamesList = 1:nGames;
resultPart1 = sum(gamesList(v))

minProducts = ones(size(minCubes(:,1)));
for c = 1:nColors
    minProducts = minProducts .* minCubes(:,c);
end
resultPart2 = sum(minProducts)
