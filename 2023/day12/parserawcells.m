function [springs, broken] = parserawcells(rawInput, unfolds)
% PARSERAWCELLS

    if nargin == 1
      unfolds = 1;
    end

    springs = {};
    broken = {};
    for l = 1:numel(rawInput)
        line = rawInput{l};

        sep = find(line == ' ');

        springs{end+1} = strjoin(repmat({line(1:sep-1)}, 1, unfolds),'?')
        broken{end+1} =  repmat(str2num(line(sep+1:end)), 1, unfolds);
    end
end
