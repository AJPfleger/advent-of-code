function strRev = reverse(str)
% REVERSE  Reverses a string. This MATLAB function is missing in Octave
%   S = REPLACENUMBERS(S) returns the reversed string
%   This implementation is probably not optimal

    strRev = str;
    for c = 1:numel(str)
        strRev(end-c+1) = str(c);
    end
end