function printpipemap(Map)

    Map(isnan(Map)) = double('n');
    Map(isinf(Map)) = double('1');

    for r = 1:size(Map,1)
        str = '';
        for c = 1:size(Map,2)
            switch Map(r,c)
                case double('F')
                    str = strcat(str,'┏');
                case double('7')
                    str = strcat(str,'┓');
                case double('L')
                    str = strcat(str,'┗');
                case double('J')
                    str = strcat(str,'┛');
                case double('-')
                    str = strcat(str,'━');
                case double('|')
                    str = strcat(str,'┃');
                case 0
                    str = strcat(str,'░');
                case double('n')
                    str = strcat(str,'N');
                case double('1');
                    str = strcat(str,'█');
                case double('S');
                    str = strcat(str,'S');
                otherwise
                    "ERROR wrong character"
            end
        end
        str
    end
end
