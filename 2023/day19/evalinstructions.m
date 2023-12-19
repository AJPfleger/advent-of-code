function xmas = evalinstructions(ins, insMap, xmas)

    str = "str = evalc('ins{insMap.in}'); disp(str(7:end));";

    while true
        str = evalc(str);
        if str(1) == 'A'
            return
        elseif str(1) == 'R'
            xmas = xmas * 0;
            return
        end
    end
end