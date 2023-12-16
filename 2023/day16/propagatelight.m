function energized = propagatelight(layout, pos)

    % pos = [r, c, vr, vc, ind]
    %   v = [1 0]
    %   ^ = [-1 0]
    %   > = [0 1]
    %   < = [0 -1]

    sLayout = size(layout);
    [R, C] = size(layout);

    dm1 = double('\');
    dm2 = double('/');
    dsh = double('-');
    dsv = double('|');

    crossings = zeros(numel(layout),4);
    energized = zeros(numel(layout),1);

    for i = 1:100000
        % get new position
        pos(:,1:2) = pos(:,1:2) + pos(:,3:4);

        % remove beams that left
        l = pos(:,1) > R | pos(:,2) > C | pos(:,1) < 1 | pos(:,2) < 1;
        pos(l,:) = [];

        % update index
        pos(:,5) = sub2ind(sLayout,pos(:,1),pos(:,2));

        % fill lightmap
        rmPos = [];
        for d = 1:size(pos,1)
            % get idx
            ind = pos(d,5);

            if sum(pos(d,3:4)) > 0
                xc = [pos(d,3:4),0,0];
            else
                xc = [0,0,-pos(d,3:4)];
            end

            if crossings(ind,logical(xc)) > 0
                rmPos(end+1) = d;
                continue
            end
            crossings(ind,:) = crossings(ind,:) + xc;
            energized(ind) = 1;
        end
        pos(rmPos,:) = [];

        if numel(pos) == 0
            break
        end

        % get next positions
        ind = pos(:,5);
        lm1 = layout(ind) == dm1;
        lm2 = layout(ind) == dm2;
        lsh = layout(ind) == dsh;
        lsv = layout(ind) == dsv;

        pos(lm1,3:4) = pos(lm1,4:-1:3);
        pos(lm2,3:4) = -pos(lm2,4:-1:3);

        for d = 1:size(pos,1);
            if lsv(d) && pos(d,4) ~= 0
                pos(d,3:4) = pos(d,4:-1:3);
                pos(end+1,:) = pos(d,:);
                pos(end,3:4) = -pos(end,3:4);
            elseif lsh(d) && pos(d,3) ~= 0
                pos(d,3:4) = pos(d,4:-1:3);
                pos(end+1,:) = pos(d,:);
                pos(end,3:4) = -pos(end,3:4);
            end
        end
    end

    energized = sum(energized);
end
