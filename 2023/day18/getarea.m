function totalArea = getarea(allPos)

    % The area can be calculated as a sum of triangles over
    % the whole polygon. We take therefore the crossproduct
    % between 2 following corners and divide by 2, to get the
    % triangle.
    % This method gets the number of enclosed squares. When
    % thinking of solid state physics, we could look at every
    % trench position as a single circle. Therefore each square
    % contributes 4 * 1/4 circles. Inside the polygon, we will
    % not encounter any problems, but at the edges and corners
    % we only look partially at those circles. We add the rest
    % later.

    % area = [];
    % for p = 1:size(allPos,1)-1
    %     P1 = allPos(p,:);
    %     P2 = allPos(p+1,:);
    %
    %     % det seems not numerically stable. But stable enough.
    %     % area(end+1) = det([P2;P1])/2;
    %     area(end+1) = (- P1(1)*P2(2) + P2(1)*P1(2))/2;
    % end

    area = (- allPos(1:end-1,1) .* allPos(2:end,2) + allPos(2:end,1) .* allPos(1:end-1,2))/2;

    % Edges are only considered as a half by the area calcualtion.
    % Therefore, we need to add half the amount of edges to the area.
    % We are still excluding cornerpoints.
    edges = allPos(1:end-1,:) - allPos(2:end,:);
    edges = abs(sum(edges,2)) - 1;

    % Corners can have three different modes:
    % - Convex -> 3/4
    % - Concave -> 1/4
    % - Straight (fake corner) -> same as edge: 1/2
    allPos(end+1,:) = allPos(2,:);
    vectors = diff(allPos);
    corners = [];
    for p = 1:size(vectors,1)-1
        d = det([vectors(p+1,:);vectors(p,:)]);

        if d > 0
            cval = 3;
        elseif d < 0;
            cval = 1;
        else
            cval = 2;
        end

        corners(end+1) = cval;
    end

    totalArea = sum(area) + sum(edges)/2 + sum(corners)/4;
end
