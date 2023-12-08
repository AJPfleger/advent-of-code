function hash = hashString(str)
% HASHSTRING  Creates a simple hash of a string
%
%   hash = HASHSTRING(str) returns the hashed string
%
%   "A" -> 65
%   "AA" -> 6565
%   "AAZA" -> 65906565

    hash = sum(double(str) .* (100 .^(0:numel(str)-1)));
end
