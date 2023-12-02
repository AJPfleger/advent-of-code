// --- Day 5: Hydrothermal Venture ---
// https://adventofcode.com/2021/day/5
//
// https://github.com/AJPfleger
//
// g++ day05.cpp -o day05 -std=c++17 -O3

#include <fstream>
#include <iostream>
#include <map>
#include <sstream>
#include <vector>

/// xyPairToInts
///
/// @param xyPair Like 123,456
std::tuple<int, int> xyPairToInts(const std::string xyPair) {
    int x, y;
    std::string s = "";

    for (auto c : xyPair) {
        if (isdigit(c)) {
            s += c;
        } else {
            x = std::stoi(s);
            s = "";
        }
    }
    y = std::stoi(s);

    return std::make_tuple(x, y);
}

/// fileToPositions
///
/// creates a vector of all covered positions as "(x,y)"
/// @param positions Vector containing the positions
/// @param filename File to parse
/// @param onlyOrtho Only looks at horizontal and vertical lines
void fileToPositions(std::vector<std::string>& positions,
                     const std::string filename, const bool onlyOrtho = true) {
    std::ifstream infile(filename);
    std::string x0y0, _, x1y1;

    // infile = "1,12 -> 123,1234"
    while (infile >> x0y0 >> _ >> x1y1) {
        // extract ranges
        auto [x0, y0] = xyPairToInts(x0y0);
        auto [x1, y1] = xyPairToInts(x1y1);

        if (onlyOrtho && x0 != x1 && y0 != y1) {
            continue;
        }

        const int xRange = x1 - x0;
        const int yRange = y1 - y0;
        const int steps = std::max(std::abs(xRange), std::abs(yRange));
        const int dx = xRange ? xRange / steps : 0;
        const int dy = yRange ? yRange / steps : 0;
        int x = x0;
        int y = y0;

        for (int _s = 0; _s <= steps; _s++) {
            std::stringstream pos;
            pos << "(" << x << "," << y << ")";
            positions.push_back(pos.str());

            x += dx;
            y += dy;
        }
    }

    return;
}

int main(int argc, char* argv[]) {
    std::cout << "--- Day 5: Hydrothermal Venture ---" << std::endl;

    const std::string filename = argc > 1 ? argv[1] : "input.txt";

    auto detectOverlap = [](auto m) { return m.second > 1; };

    {
        std::vector<std::string> positions;
        fileToPositions(positions, filename, true);

        std::map<std::string, int> coveredPositions;

        for (auto pos : positions) {
            if (coveredPositions.count(pos)) {
                ++coveredPositions[pos];
            } else {
                coveredPositions[pos] = 1;
            }
        }

        int overlaps = std::count_if(coveredPositions.begin(),
                                     coveredPositions.end(), detectOverlap);

        std::cout << "Part1: Overlaps: " << overlaps << std::endl;
    }
    {
        std::vector<std::string> positions;
        fileToPositions(positions, filename, false);

        std::map<std::string, int> coveredPositions;

        for (auto pos : positions) {
            if (coveredPositions.count(pos)) {
                ++coveredPositions[pos];
            } else {
                coveredPositions[pos] = 1;
            }
        }

        int overlaps = std::count_if(coveredPositions.begin(),
                                     coveredPositions.end(), detectOverlap);

        std::cout << "Part2: Overlaps: " << overlaps << std::endl;
    }

    return 0;
}
