function mapChar = printpipemap(Map)
% PRINTPIPTEMAP
%
%   mapChar = PRINTPIPTEMAP(Map) returns a char with the map

    Map(isnan(Map)) = double('n');
    Map(isinf(Map)) = double('1');

    mapChar = newline;
    for r = 1:size(Map,1)
        for c = 1:size(Map,2)
            switch Map(r,c)
                case double('F')
                    mapChar = strcat(mapChar,'┏');
                case double('7')
                    mapChar = strcat(mapChar,'┓');
                case double('L')
                    mapChar = strcat(mapChar,'┗');
                case double('J')
                    mapChar = strcat(mapChar,'┛');
                case double('-')
                    mapChar = strcat(mapChar,'━');
                case double('|')
                    mapChar = strcat(mapChar,'┃');
                case 0
                    mapChar = strcat(mapChar,'░');
                case double('n')
                    mapChar = strcat(mapChar,'N');
                case double('1');
                    mapChar = strcat(mapChar,'█');
                case double('S');
                    mapChar = strcat(mapChar,'S');
                otherwise
                    "ERROR wrong character"
            end
        end
        mapChar = strcat(mapChar,newline);
    end
    mapChar = strcat(mapChar,newline);
end
