// --- Day 8: Seven Segment Search ---
// https://adventofcode.com/2021/day/08
//
// https://github.com/AJPfleger
//
// g++ day08.cpp -o day08 -std=c++11 -O3

#include <fstream>
#include <iostream>
#include <map>
#include <sstream>
#include <vector>

#include <math.h>

/// parseAndCount1478
/// counts only the numbers 1, 4, 7, and 8 in the "output values"
///
/// @param filename File to parse
int parseAndCount1478(const std::string filename) {
    int n1478 = 0;

    std::ifstream infile(filename);
    std::string str;

    int lastDigits = 0;
    while (infile >> str) {
        --lastDigits;
        if (str == "|") {
            lastDigits = 5;
        }
        if (lastDigits > 0 && (str.size() == 2 || str.size() == 3 ||
                               str.size() == 4 || str.size() == 7)) {
            ++n1478;
        }
    }

    return n1478;
}

/// finished
/// Checks if the last n digits are valid
///
/// @tparam N Total number of digits
/// @tparam lastN Number of digits for output
///
/// @param digits Entry to check
/// @param lastN Check if the lastN digits are filled
template <int N = 14, int lastN = 4>
bool finished(const std::vector<int>& digits) {
    for (int n = N - lastN; n < N; n++) {
        if (digits[n] < 0 || 9 < digits[n]) {
            return false;
        }
    }
    return true;
}

/// finalise
/// converts the last n digits into an integer
///
/// @tparam N Total number of digits
/// @tparam lastN Number of digits for output
///
/// @param digits Entry to convert
/// @param lastN The lastN digits are the output
template <int N = 14, int lastN = 4>
int finalise(const std::vector<int>& digits) {
    int outputValue = 0;

    for (int i = 0; i < lastN; i++) {
        outputValue += digits[N - 1 - i] * std::pow(10, i);
    }

    return outputValue;
}

/// countOverlaps
/// Counts how many segments of the refStr are in the testStr. An empty refStr
/// results in "0" overlaps.
///
/// @param testStr String to test
/// @param refStr Reference string
int countOverlaps(const std::string& testStr, const std::string& refStr) {
    if (!refStr.size()) {
        return 0;
    }

    int overlaps = 0;
    for (auto c : refStr) {
        //        if (testStr.contains(c)) // C++23
        //        {
        //            ++overlaps;
        //        }
        if (testStr.find(c) != std::string::npos) {
            ++overlaps;
        }
    }

    return overlaps;
}

/// setDigit
/// Sets the deciphered digit in the digit vector and the map
///
/// @param line Line (Encoded digits)
/// @param digits Digits vector
/// @param mDigits Digits map
/// @param n n-th digit
/// @param d Decoded digit
void setDigit(const std::vector<std::string>& line, std::vector<int>& digits,
              std::map<int, std::string>& mDigits, const int n, const int d) {
    digits[n] = d;
    mDigits[d] = line[n];
    return;
}

/// getOutput
/// Tries to decipher the whole line and returns the final last n digits
/// converted to an integer
///
/// @tparam N Total number of digits
/// @tparam lastN Number of digits for output
///
/// @param line Line to analyse
/// @param lastN The lastN digits are the output
template <int N = 14, int lastN = 4>
int getOutput(std::vector<std::string>& line) {
    std::vector<int> digits(N, -1);
    std::map<int, std::string> mDigits;

    // initialise map
    for (int d = 0; d <= 9; d++) {
        mDigits[d] = "";
    }

    // trivial digits 1, 4, 7, 8
    for (int n = 0; n < N; n++) {
        if (line[n].size() == 2) {
            setDigit(line, digits, mDigits, n, 1);
        } else if (line[n].size() == 3) {
            setDigit(line, digits, mDigits, n, 7);
        } else if (line[n].size() == 4) {
            setDigit(line, digits, mDigits, n, 4);
        } else if (line[n].size() == 7) {
            setDigit(line, digits, mDigits, n, 8);
        }
    }

    if (finished<N, lastN>(digits)) {
        return finalise<N, lastN>(digits);
    }

    // more complex substitutions
    // 3 is size5 with 1 or 7 overlap
    // 9 is size6 with 4 overlap
    // 6 is size6 without 1 or 7 overlap
    for (int n = 0; n < N; n++) {
        if (line[n].size() == 5) {
            if (countOverlaps(line[n], mDigits[1]) == 2 ||
                countOverlaps(line[n], mDigits[7]) == 3) {
                setDigit(line, digits, mDigits, n, 3);
            }
        } else if (line[n].size() == 6) {
            if (countOverlaps(line[n], mDigits[4]) == 4) {
                setDigit(line, digits, mDigits, n, 9);
            } else if (countOverlaps(line[n], mDigits[1]) != 2 ||
                       countOverlaps(line[n], mDigits[7]) != 3) {
                setDigit(line, digits, mDigits, n, 6);
            }
        }
    }

    if (finished<N, lastN>(digits)) {
        return finalise<N, lastN>(digits);
    }

    // more complex substitutions
    for (int n = 0; n < N; n++) {
        if (line[n].size() == 5) {
            if (countOverlaps(line[n], mDigits[1]) == 2 ||
                countOverlaps(line[n], mDigits[7]) == 3) {
                setDigit(line, digits, mDigits, n, 3);
            }
        } else if (line[n].size() == 6) {
            if (countOverlaps(line[n], mDigits[4]) == 4) {
                setDigit(line, digits, mDigits, n, 9);
            } else if (countOverlaps(line[n], mDigits[1]) != 2 ||
                       countOverlaps(line[n], mDigits[7]) != 3) {
                setDigit(line, digits, mDigits, n, 6);
            }
        }
    }

    if (finished<N, lastN>(digits)) {
        return finalise<N, lastN>(digits);
    }

    // get 0, 2, 5
    for (int n = 0; n < N; n++) {
        if (line[n].size() == 5) {
            if (countOverlaps(line[n], mDigits[3]) != 5 &&
                countOverlaps(line[n], mDigits[6]) == 4 &&
                countOverlaps(line[n], mDigits[9]) == 5) {
                setDigit(line, digits, mDigits, n, 2);
            } else if (countOverlaps(line[n], mDigits[6]) == 5 &&
                       countOverlaps(line[n], mDigits[9]) == 5) {
                setDigit(line, digits, mDigits, n, 5);
            }
        } else if (line[n].size() == 6) {
            if (countOverlaps(line[n], mDigits[6]) == 5 &&
                countOverlaps(line[n], mDigits[9]) == 5) {
                setDigit(line, digits, mDigits, n, 0);
            }
        }
    }

    if (finished<N, lastN>(digits)) {
        return finalise<N, lastN>(digits);
    }

    // other attempt for 2
    for (int n = 0; n < N; n++) {
        if (line[n].size() == 5) {
            if (countOverlaps(line[n], mDigits[3]) != 5 &&
                countOverlaps(line[n], mDigits[5]) != 5) {
                setDigit(line, digits, mDigits, n, 2);
            }
        }
    }

    if (finished<N, lastN>(digits)) {
        return finalise<N, lastN>(digits);
    }

    for (const auto& d : mDigits) {
        std::cout << d.first << " " << d.second << "\n";
    }

    throw std::runtime_error("Couldn't figure out all necessary digits.");
}

/// parseFile
///
/// @tparam N Total number of digits
///
/// @param filename File to parse
template <int N = 14>
std::vector<std::vector<std::string>> parseFile(const std::string filename) {
    std::vector<std::vector<std::string>> allLines;
    std::vector<std::string> singleLine(N);

    std::ifstream infile(filename);
    std::string str;

    int position = 0;
    while (infile >> str) {
        if (str == "|") {
            continue;
        }

        singleLine[position] = str;
        ++position;

        if (position == N) {
            position = 0;
            allLines.push_back(singleLine);
        }
    }

    return allLines;
}

int main(int argc, char* argv[]) {
    std::cout << "--- Day 8: Seven Segment Search ---" << std::endl;

    const std::string filename = argc > 1 ? argv[1] : "input.txt";

    {
        const int n1478 = parseAndCount1478(filename);
        std::cout << "Part1: Count 1, 4, 7, and 8 = " << n1478 << std::endl;
    }

    {
        constexpr int N = 14;
        constexpr int lastN = 4;

        auto allLines = parseFile<N>(filename);

        std::vector<int> outputValues;
        for (auto line : allLines) {
            outputValues.push_back(getOutput<N, lastN>(line));
        }

        std::cout << "Part2: The sum of all output values is "
                  << std::accumulate(outputValues.begin(), outputValues.end(), 0)
                  << std::endl;
    }

    return 0;
}
