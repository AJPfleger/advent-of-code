function allPos = ins2pos(instructions)

    allPos = [1,1];
    for i = 1:size(instructions,1)
        switch instructions(i,1)
            % part 1
            case double('R')
                direction = [0,1];
            case double('D')
                direction = [1,0];
            case double('L')
                direction = [0,-1];
            case double('U')
                direction = [-1,0];

            % part 2
            case 0
                direction = [0,1];
            case 1
                direction = [1,0];
            case 2
                direction = [0,-1];
            case 3
                direction = [-1,0];

            otherwise
                "ERROR wrong direction"
        end

        allPos(end+1,:) = allPos(end,:) + direction * instructions(i,2);
    end
end
