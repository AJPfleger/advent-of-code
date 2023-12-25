function hash = hashstring(str)
% HASHSTRING  Creates a simple bijective hash of a string
%
%   hash = HASHSTRING(str) returns the hashed string
%
%   "A" -> 65
%   "AA" -> 65065
%   "AAZA" -> 65090065065

    hash = sum(double(str) .* (1000 .^(0:numel(str)-1)));
end
