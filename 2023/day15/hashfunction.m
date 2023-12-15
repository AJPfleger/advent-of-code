function hash = hashfunction(str)
% HASHFUNCTION  Hashes a string
%
%   hash = HASHSTRING(str) returns the hashed string
%
%    Determine the ASCII code for the current character of the string.
%    Increase the current value by the ASCII code you just determined.
%    Set the current value to itself multiplied by 17.
%    Set the current value to the remainder of dividing itself by 256.
%
%    str = double(str);
%    h = 0;
%    for n = 1:numel(str)
%        h = mod((h + str(n)) * 17, 256);
%    end

    % optimise but doesn't work on long strings
    str = double(str) .* (17 .^ [numel(str):-1:1]);
    hash = mod(sum(str),256);

end
