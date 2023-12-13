function C = countpossibilities(springsStr, broken)
% COUNTPOSSIBILITIES

    % remove leading and tailing '.'
    springsStr = springsStr(find(springsStr!='.')(1):find(springsStr!='.')(end));

    % string too short
    if numel(springsStr) < sum(broken) + numel(broken) - 1
        C = 0;
        return
    end

    % places for last springs
    if numel(broken) == 1
        C = 0;

        if numel(springsStr) < broken
            return
        end

        if numel(springsStr) == broken
            if ~any(springsStr == '.')
                C = 1;
            end
            return
        end

        for s = 1:numel(springsStr)-broken+1
            if ~any(springsStr(1:s-1) == '#') && ~any(springsStr(s:s+broken-1) == '.') && ~any(springsStr(s+broken:end) == '#')
                C = C + 1;
            end
        end

        return
    end

    C = 0;
    b = broken(1);
    for s = 1:numel(springsStr) - sum(broken) - numel(broken) + 2

        % skipped a fixed point
        if any(springsStr(1:s-1) == '#')
            break
        end

        % first b segments cannot be broken, try next step
        if any(springsStr(s:b+s-1) == '.')
            continue
        end

        % skips a fixed point
        if springsStr(b+s) == '#'
            continue
        end

        C = C + countpossibilities(springsStr(s+b+1:end), broken(2:end)); % reduced problem
    end
end
