function res = analysepatterns(allPatterns, smudgeDifference)
% ANALYSEPATTERNS  Evaluates all patterns and calculates the reflection values
%
%   res = ANALYSEPATTERNS(allPatterns, smudgeDifference) returns the result for the day
%
%   smudgeDifference:
%       default = 0
%       set to the difference between 2 symbols, that could be smudged

    if nargin == 1
      smudgeDifference = 0;
    end


    rReflections = [];
    cReflections = [];
    for p = 1:numel(allPatterns)
        pattern = allPatterns{p};

        [R,C] = size(pattern);
        for r = 1:R-1
            dr = min(r-1, R-(r+1));

            range1 = r-dr : r;
            range2 = r+1+dr : -1 : r+1;

            d = abs(pattern(range1,:) - pattern(range2,:));
            d = sum(d(:));
            if  d == abs(smudgeDifference)
                rReflections(end+1) = r;
                break
            end
        end

        for c = 1:C-1
            dc = min(c-1, C-(c+1));

            range1 = c-dc : c;
            range2 = c+1+dc : -1 : c+1;

            d = abs(pattern(:,range1) - pattern(:,range2));
            d = sum(d(:));
            if d == abs(smudgeDifference)
                cReflections(end+1) = c;
                break
            end
        end

    end

    res = 100*sum(rReflections) + sum(cReflections);
end
