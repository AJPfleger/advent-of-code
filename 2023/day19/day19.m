% GNU Octave, version 8.4.0
%
% --- Day 19: Aplenty ---
% https://adventofcode.com/2023/day/19
%
% https://github.com/AJPfleger
%
% call like 'octave day19.m input.txt'

disp('--- Day 19: Aplenty ---')

args = argv();
filename = args{1}

fid = fopen(filename,'rt');
rawInput = textscan(fid,'%s','delimiter', '\n');
fclose(fid);

rawInput = rawInput{1};
R = numel(rawInput);

% split instructions and xmas
insRaw = {};
xmas = [];
for i = 1:R
    line = rawInput{i};
    if numel(line) == 0
        r = i + 1;
        break
    end

    insRaw{end+1} = line;
end
for i = r:R
    line = rawInput{i};
    ss = strsplit(line(2:end-1),',');
    singleXmas = [];
    for x = 1:4
        singleXmas(end+1) = str2num(ss{x}(3:end));
    end

    xmas(end+1,:) = singleXmas;
end

% parse instructions
ins = {};
insMap = struct();
for i = 1:numel(insRaw)
    line = insRaw{i};
    commas = find(line == ',');
    rest = line(commas(end)+1:end);
    line = line(1:commas(end));

    line = strrep(line,'{x','{if xmas(1)');
    line = strrep(line,',x',',elseif xmas(1)');
    line = strrep(line,'{m','{if xmas(2)');
    line = strrep(line,',m',',elseif xmas(2)');
    line = strrep(line,'{a','{if xmas(3)');
    line = strrep(line,',a',',elseif xmas(3)');
    line = strrep(line,'{s','{if xmas(4)');
    line = strrep(line,',s',',elseif xmas(4)');

    line = strrep(line,':A,','; disp(''A''); ');
    line = strrep(line,':R,','; xmas=xmas*0; disp(''R''); ');

    if rest(1) == 'A'
        rest = ' else; disp(''A''); end;';
    elseif rest(1) == 'R';
        rest = ' else; xmas=xmas*0; disp(''R''); end;';
    else
        rest = strcat(' else; str = evalc(''ins{insMap.',rest,'''); disp(str(7:end)); end;');
    end

    ss = strsplit(line,'{');
    key = ss(1){1};
    insMap.(key) = i;
    insTemp = ss(2){1};

    insTemp = strrep(insTemp,':','; str = evalc(''ins{insMap.');%}); end;
    insTemp = strrep(insTemp,',','}''); disp(str(7:end));');

    ins{end+1} = strcat(insTemp(1:end-1),rest);
end


%% Part 1 --------------------------------------------------------

for x = 1:size(xmas,1)
    xmasEvs(end+1,:) = evalinstructions(ins,insMap,xmas(x,:));
end

resultPart1 = sum(xmasEvs(:))


%% Part 2 --------------------------------------------------------

% would take 12,000 years when testing like this in all 4 dimensions
%tic
%count = 0;
%for x = 1:4000
%    if evalinstructions(ins,insMap,[x,1,1,1]) > 0
%        count = count + 1;
%    end
%end
%toc
%resultPart2 = count
