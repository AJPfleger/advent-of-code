% GNU Octave, version 8.4.0
%
% --- Day 3: Gear Ratios ---
% https://adventofcode.com/2023/day/3
%
% https://github.com/AJPfleger
%
% call like 'octave day03.m input.txt'

disp('--- Day 3: Gear Ratios ---')

format long % to get the proper formated output

args = argv();
filename = args{1}

fid = fopen(filename,'rt');
rawInput = textscan(fid,'%s','delimiter', '\n');
fclose(fid);

rawInput = rawInput{1};
nCols = numel(rawInput);
nRows = numel(rawInput{1});

schematic = zeros([nRows+2, nCols+2]);
for s = 1:numel(schematic)
    schemtaic(s) = '.';
end

for r = 1:nRows
    schematic (r+1,2:end-1) = double(rawInput{r});
end

dotASCII = double('.');
zeroASCII = double('0');
gearASCII = double('*');

lSchematicEmpty = schematic == dotASCII;
lSchematicDigits = schematic >= zeroASCII & (schematic <= zeroASCII + 9);
lSchematicSymbols = ~lSchematicEmpty & ~lSchematicDigits;
lSchematicPossibleGear = schematic == gearASCII;


%% Part 1 --------------------------------------------------------

%generate adjecent symbols
adjecentToSymbols = false(size(schematic));
for rShift = -1:1
    for cShift = -1:1
        adjecentToSymbols((2:end-1)+rShift, (2:end-1)+cShift) = adjecentToSymbols((2:end-1)+rShift, (2:end-1)+cShift) | lSchematicSymbols(2:end-1,2:end-1);
    end
end

partNumbers = [];
for r = 2:nRows+1
    currentNumber = [];
    isPart = 0;
    for c = 2:nCols+2
        if lSchematicDigits(r,c)
            currentNumber(end+1) = schematic(r,c);
            isPart = isPart | adjecentToSymbols(r,c);
        elseif numel(currentNumber) > 0
            if isPart
                partNumbers(end+1) = str2num(char(currentNumber));
            end
            currentNumber = [];
            isPart = 0;
        end
    end
end

resultPart1 = sum(partNumbers(:))


%% Part 2 --------------------------------------------------------

gearTable = [];
for r = 2:nRows+1

    gearList = [];
    currentNumber = [];
    lNumberAdjecent = false(size(schematic));
    for c = 2:nCols+2

        if lSchematicDigits(r,c)

            lNumberAdjecent(r-1:r+1,c-1:c+1) = 1;
            currentNumber(end+1) = schematic(r,c);

        elseif numel(currentNumber) > 0
            gearList = find(lNumberAdjecent & lSchematicPossibleGear);
            if numel(gearList) ~= 0
                for gl = 1:size(gearList,1)
                    gearTable(end+1,:) = [gearList(gl,:), str2num(char(currentNumber))];
                end
            end

            currentNumber = [];
            gearList = [];
            lNumberAdjecent = false(size(schematic));
        end
    end
end

gearRatios = [];
checkedGears = [];
for gt = 1:size(gearTable,1)
    currentGear = gearTable(gt,1);

    % do not double-check
    if ismember(currentGear,checkedGears,'rows')
        continue
    end
    checkedGears(end+1,:) = currentGear;

    lCurrentGearAll = ismember(gearTable(:,1),currentGear,'rows');

    if sum(lCurrentGearAll) ~= 2
        continue
    end

    gearRatios(end+1) = prod(gearTable(:,2)(lCurrentGearAll));
end

resultPart2 = sum(gearRatios(:))
