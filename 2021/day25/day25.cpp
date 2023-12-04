// --- Day 25: Sea Cucumber ---
// https://adventofcode.com/2021/day/25
//
// https://github.com/AJPfleger
//
// g++ day25.cpp -o day25 -std=c++11 -O3

#include <fstream>
#include <iostream>
#include <vector>

/// Convert the input file to a cave map
///
/// @param filename File to parse
std::vector<std::string> parseFile(const std::string filename) {
    std::vector<std::string> caveMap;
    std::ifstream infile(filename);
    std::string line;

    while (infile >> line) {
        caveMap.push_back(line);
    }

    return caveMap;
}

/// Print the cave
///
/// @param caveMap Cave to print
void printCaveMap(const std::vector<std::string>& caveMap) {
    std::cout << "╔";
    for (int i = 0; i < caveMap[0].size(); i++) {
        std::cout << "═";
    }
    std::cout << "╗\n";

    for (auto row : caveMap) {
        std::cout << "║" << row << "║\n";
    }

    std::cout << "╚";
    for (int i = 0; i < caveMap[0].size(); i++) {
        std::cout << "═";
    }
    std::cout << "╝";

    std::cout << std::endl;

    return;
}

/// Tries to move all cucumbers first east then south.
/// Returns true if any cucumber moved.
///
/// @param caveMap Current state of the cave
/// @param caveMapStep Proposed step (buffer)
bool move(std::vector<std::string>& caveMap,
          std::vector<std::string>& caveMapStep) {
    const int nRows = caveMap.size();
    const int nCols = caveMap[0].size();

    bool anyMovement = false;

    caveMapStep = caveMap;

    // move east
    for (int row = 0; row < nRows; row++) {
        for (int col = 0; col < nCols; col++) {
            if (caveMap[row][col] == '>' && caveMap[row][(col + 1) % nCols] == '.') {
                anyMovement = true;
                caveMapStep[row][col] = '.';
                caveMapStep[row][(col + 1) % nCols] = '>';
            }
        }
    }

    caveMap = caveMapStep;

    // move south
    for (int row = 0; row < nRows; row++) {
        for (int col = 0; col < nCols; col++) {
            if (caveMap[row][col] == 'v' && caveMap[(row + 1) % nRows][col] == '.') {
                anyMovement = true;
                caveMapStep[row][col] = '.';
                caveMapStep[(row + 1) % nRows][col] = 'v';
            }
        }
    }

    std::swap(caveMap, caveMapStep);

    return anyMovement;
}

int main(int argc, char* argv[]) {
    std::cout << "--- Day 25: Sea Cucumber ---" << std::endl;

    const std::string filename = argc > 1 ? argv[1] : "input.txt";

    auto caveMap = parseFile(filename);
    auto caveMapStep = caveMap;

    printCaveMap(caveMap);

    int stepCount = 0;
    // We assume, that we can do at least 1 step
    bool anyMovement = true;
    while (anyMovement) {
        anyMovement = move(caveMap, caveMapStep);
        stepCount++;
    }

    printCaveMap(caveMap);

    std::cout << "Part1: Steps: " << stepCount << std::endl;
    std::cout << "Part2: Collect all other stars." << std::endl;

    return 0;
}
