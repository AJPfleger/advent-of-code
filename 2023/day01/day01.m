% GNU Octave, version 8.4.0
%
% --- Day 1: Trebuchet?! ---
% https://adventofcode.com/2023/day/1
%
% https://github.com/AJPfleger
%
% call like `octave day01.m input.txt true`

disp('--- Day 1: Trebuchet?! ---')

args = argv();
filename = args{1}
if numel(args) > 1 && strcmp(args{2},'true'); interpret_text = true; else; interpret_text = false; end
interpret_text

fid = fopen(filename,'rt');
rawInput = textscan(fid,'%s');
fclose(fid);

rawInput = rawInput{1};

v = zeros(size(rawInput));
for iLine = 1:numel(rawInput)
    thisline = rawInput{iLine};

    if interpret_text
        thisline = replacenumbers(thisline);
    end

    number_positions = isstrprop(thisline,'digit');
    number_string = thisline(number_positions);
    two_digit_number = strcat(number_string(1), number_string(end));
    v(iLine) = str2num(two_digit_number);
end

result = sum(v(:))
