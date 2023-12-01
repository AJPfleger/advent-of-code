function str = replacenumbers(str)
% REPLACENUMBERS  Converts number words in strings to digits
%   S = REPLACENUMBERS(S) returns the modified string
%   To avoid problems with overlapping words, each number word is
%   duplicated and has the corresponding numeral enclosed.
%   Works only for numbers 1:9

    str = strrep(str,'one','one1one');
    str = strrep(str,'two','two2two');
    str = strrep(str,'three','three3three');
    str = strrep(str,'four','four4four');
    str = strrep(str,'five','five5five');
    str = strrep(str,'six','six6six');
    str = strrep(str,'seven','seven7seven');
    str = strrep(str,'eight','eight8eight');
    str = strrep(str,'nine','nine9nine');
end