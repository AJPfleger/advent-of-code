function endPositions = getendpositions(layout, nSteps)

    dO = double("O");
    dD = double(".");

    sLayout = size(layout);
    R = sLayout(1);
    C = sLayout(2);

    layout(layout == double('S')) = dO;

    [r,c] = ind2sub(sLayout, layout == dO);
    oList = [r,c];

    for s = 1:nSteps
        oListNew = [];

        for o = 1:size(oList,1)
            % do all 4 directions directly, because it is faster than
            % a beautiful loop

            rx = oList(o,1);
            cx = oList(o,2);

            c = cx;
            r = rx + 1;
            if r >= 1 && r <= R && layout(r,c) == dD
                layout(r,c) = dO;
                oListNew(end+1,:) = [r,c];
            end

            r = rx - 1;
            if r >= 1 && r <= R && layout(r,c) == dD
                layout(r,c) = dO;
                oListNew(end+1,:) = [r,c];
            end

            r = rx;
            c = cx + 1;
            if c >= 1 && c <= C && layout(r,c) == dD
                layout(r,c) = dO;
                oListNew(end+1,:) = [r,c];
            end

            c = cx - 1;
            if c >= 1 && c <= C && layout(r,c) == dD
                layout(r,c) = dO;
                oListNew(end+1,:) = [r,c];
            end
        end

        oList = oListNew;
    end

    lO = layout == dO;
    checkboardmatrix = (1:R)' + (1:C) + mod(nSteps,2) + 1;
    checkboardmatrix = logical(mod(checkboardmatrix,2));
    endPositions = lO & checkboardmatrix;

end
