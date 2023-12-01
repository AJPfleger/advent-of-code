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
raw_input = textscan(fid,'%s');
fclose(fid);

raw_input = raw_input{1};

v = zeros(size(raw_input));
for i = 1:numel(raw_input)
    thisline = raw_input{i};

    if interpret_text
        thisline = replace_numbers(thisline);
    end

    number_positions = isstrprop(thisline,'digit');
    number_string = thisline(number_positions);
    two_digit_number = strcat(number_string(1), number_string(end));
    v(i) = str2num(two_digit_number);
end

result = sum(v(:))


% Define function here instead of using a separate file
function str = replace_numbers(str)
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