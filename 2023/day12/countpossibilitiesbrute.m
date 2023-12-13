function C = countpossibilitiesbrute(springsStr, broken)
% COUNTPOSSIBILITIESBRUTE

    springsStr = strcat('.',springsStr);
    springsStr = strcat(springsStr,'.');

    lH = springsStr == '#';
    lQ = springsStr == '?';

    if sum(lH) + sum(lQ) == sum(broken)
        % only one combination possible
        C = 1;
        return
    end

    possibleRaw = nchoosek(find(lQ),sum(broken) - sum(lH));
    possible = unique(possibleRaw, 'rows');

    C = 0;
    for p = 1:size(possible,1)
        s2 = springsStr;
        s2(lQ) = '.';
        s2(possible(p,:)) = '#';

        % find groups
        ss = strsplit(s2,'.');

        % check if right number of segments
        if numel(ss) - 2 == numel(broken) && all(cellfun('length',ss)(2:end-1) == broken)
            C = C + 1;
        end
    end
end
