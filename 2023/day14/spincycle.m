function pf = spincycle(pf)

% north, then west, then south, then east.

    dO = double('O');
    dE = double('.');

    [R,C] = size(pf);

    %north
    movement = true;
    while movement
        movement = false;
        for r = 2:R
            for c = find(pf(r,:) == dO)

                if pf(r-1,c) == dE
                    movement = true;
                    pf(r-1,c) = dO;
                    pf(r,c) = dE;
                end
            end
        end
    end

    %west
    movement = true;
    while movement
        movement = false;
        for c = 2:C
            for r = find(pf(:,c) == dO).'
                if pf(r,c-1) == dE
                    movement = true;
                    pf(r,c-1) = dO;
                    pf(r,c) = dE;
                end
            end
        end
    end

    %south
    movement = true;
    while movement
        movement = false;
        for r = R-1:-1:1
            for c = find(pf(r,:) == dO)

                if pf(r+1,c) == dE
                    movement = true;
                    pf(r+1,c) = dO;
                    pf(r,c) = dE;
                end
            end
        end
    end

    %east
    movement = true;
    while movement
        movement = false;
        for c = C-1:-1:1
            for r = find(pf(:,c) == dO).'

                if pf(r,c+1) == dE
                    movement = true;
                    pf(r,c+1) = dO;
                    pf(r,c) = dE;
                end
            end
        end
    end
end
