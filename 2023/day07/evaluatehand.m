function hand = evaluatehand(handRaw, JisForJoker)
% EVALUATEHAND  Converts a raw hand (4K8J9 314) into a vector giving points to
%   each card. Then it gives the whole hand a scoring. It let's switch between
%   Jacks and Jokers.
%
%   hand = EVALUATEHAND(handRaw, JisForJoker) returns the parsed and evaluated hand
%
%   hand(1:5)   card values
%   hand(6)     hand score
%   hand(7)     bid

    % convert letters to values
    hand = [];
    for c = 1:5
        card = handRaw(c);

        if card == 'A'
            hand(end+1) = 14;
        elseif card == 'K'
            hand(end+1) = 13;
        elseif card == 'Q'
            hand(end+1) = 12;
        elseif card == 'J'
            if JisForJoker
                hand(end+1) = 1;
            else
                hand(end+1) = 11;
            end
        elseif card == 'T'
            hand(end+1) = 10;
        else
            hand(end+1) = str2num(card);
        end
    end

    % calculate score
    catVec = [];

    if JisForJoker
        % try to substitute J with any other occuring card
        jRange = unique(hand);
    else
        % use J as it is
        jRange = 11;
    end

    for j = jRange
        handTest = hand;
        handTest(hand == 1) = j;
        [counts,~] = hist(handTest,unique(handTest));

        if sum(counts ~= 0) == 1 % hist() with 1 bin is weird
            % 7   Five of a kind, where all five cards have the same label: AAAAA
            catVec(end+1) = 7;
        elseif numel(counts) == 2
            % 6 Four of a kind, where four cards have the same label and one card
            %   has a different label: AA8AA
            % 5 Full house, where three cards have the same label, and the remaining
            %   two cards share a different label: 23332
            if max(counts) == 4
                catVec(end+1) = 6;
            else
                catVec(end+1) = 5;
            end
        elseif numel(counts) == 3
            % 4 Three of a kind, where three cards have the same label, and the
            %   remaining two cards are each different from any other card in the
            %   hand: TTT98
            % 3 Two pair, where two cards share one label, two other cards share a
            %   second label, and the remaining card has a third label: 23432
            if max(counts) == 3
                catVec(end+1) = 4;
            else
                catVec(end+1) = 3;
            end
        elseif numel(counts) == 4
            % 2 One pair, where two cards share one label, and the other three cards
            %   have a different label from the pair and each other: A23A4
            catVec(end+1) = 2;
        elseif numel(counts) == 5
            % 1   High card, where all cards' labels are distinct: 23456
            catVec(end+1) = 1;
        else
            disp('ERROR in unique binning')
        end
    end
    hand(end+1) = max(catVec);
    hand(end+1) = str2num(handRaw(7:end));
end
