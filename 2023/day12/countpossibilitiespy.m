function C = countpossibilitiespy(springsStr, broken)

    persistent memcp
    if isempty(memcp)
        memcp = memoize(@countpossibilitiespy);
%        memcp.CacheSize = 1000000000000;
    end

    B = broken(1);

    C = 0;
    if numel(broken) > 1
        while numel(springsStr) >= sum(broken) + numel(broken) - 1

            if isempty(strfind(springsStr(1:B), '.')) && springsStr(B+1) ~= '#'
                C = C + memcp(springsStr(B+2:end), broken(2:end));
            end

            if springsStr(1) == '#'
                break
            end

            springsStr = springsStr(2:end);
        end

    else
        nss = numel(springsStr);
        for p = 1:nss - B + 1

            if isempty(strfind(springsStr(1:B), '.')) && isempty(strfind(springsStr(B+1:end), '#'))
                C = C + 1;
            end

            if springsStr(1) == '#'
                break
            end

            springsStr = springsStr(2:end);
        end
    end
end
