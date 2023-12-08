// --- Day 10: Syntax Scoring ---
// https://adventofcode.com/2021/day/10
//
// https://github.com/AJPfleger
//
// g++ day10.cpp -o day10 -std=c++11 -O3

#include <fstream>
#include <iostream>
#include <map>
#include <sstream>
#include <vector>

/// Reduces a vector and returns a score for the corruption.
/// If the line is not corrupted, it returns 0
/// @param line Vector to match and analyse
int valueLineNum(std::vector<int>& line) {
    // reduce vector
    int oldSize = -1;
    while (oldSize != line.size()) {
        oldSize = line.size();
        for (int i = 0; i < line.size() - 1; i++) {
            if (line[i] + line[i + 1] == 0 && line[i] > 0) {
                line.erase(line.begin() + i, line.begin() + i + 2);
                break;
            }
        }
    }

    for (auto c : line) {
        if (c < 0) {
            return -c;
        }
    }

    return 0;
}

/// Converts an input file to a vector of vectors, converting the chars to
/// values. Closing characters always get a minus sign
/// @param filename File to parse
/// @param r ): 3 points.
/// @param s ]: 57 points.
/// @param t }: 1197 points.
/// @param u >: 25137 points.
std::vector<std::vector<int>> convertFile(const std::string filename,
                                          const int r = 3, const int s = 57,
                                          const int t = 1197,
                                          const int u = 25137) {
    std::vector<std::vector<int>> convFile;
    std::ifstream infile(filename);
    std::string line;

    while (infile >> line) {
        std::vector<int> convLine;
        for (auto c : line) {
            switch (c) {
                case '(':
                    convLine.push_back(r);
                    break;
                case ')':
                    convLine.push_back(-r);
                    break;
                case '[':
                    convLine.push_back(s);
                    break;
                case ']':
                    convLine.push_back(-s);
                    break;
                case '{':
                    convLine.push_back(t);
                    break;
                case '}':
                    convLine.push_back(-t);
                    break;
                case '<':
                    convLine.push_back(u);
                    break;
                case '>':
                    convLine.push_back(-u);
                    break;
                default:
                    std::cout << "ERROR wrong character: '" << c << "'" << std::endl;
            }
        }
        convFile.push_back(convLine);
    }

    return convFile;
}

int main(int argc, char* argv[]) {
    std::cout << "--- Day 10: Syntax Scoring ---" << std::endl;

    const std::string filename = argc > 1 ? argv[1] : "input.txt";

    {
        int sumErrors = 0;
        const auto convFile = convertFile(filename);
        for (auto line : convFile) {
            sumErrors += valueLineNum(line);
        }

        std::cout << "Part 1: Total syntax error score = " << sumErrors
                  << std::endl;
    }
    {
        std::vector<long> scoresVec;
        const auto convFile = convertFile(filename, 1, 2, 3, 4);
        for (auto line : convFile) {
            if (valueLineNum(line) == 0) {
                std::reverse(line.begin(), line.end());

                long score = 0;
                for (auto c : line) {
                    score *= 5;
                    score += c;
                }
                scoresVec.push_back(score);
            }
        }
        std::sort(scoresVec.begin(), scoresVec.end());

        std::cout << "Part 2: Total syntax error score = "
                  << scoresVec[scoresVec.size() / 2] << std::endl;
    }

    return 0;
}
