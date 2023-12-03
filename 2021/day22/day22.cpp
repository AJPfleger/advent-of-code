// --- Day 22: Reactor Reboot ---
// https://adventofcode.com/2021/day/22
//
// https://github.com/AJPfleger
//
// g++ day22.cpp -o day22 -std=c++17 -O3

#include <fstream>
#include <iostream>
#include <map>
#include <sstream>
#include <vector>

/// parseFile
///
/// creates a vector of all covered positions as "(x,y)"
/// @param filename File to parse
/// @param cutOff A symmetric cutOff, that excludes over shooting ranges
std::vector<std::tuple<bool, std::vector<int>>> parseFile(
        const std::string filename, const int cutOff = 50) {
    std::vector<std::tuple<bool, std::vector<int>>> parsedSteps;
    std::ifstream infile(filename);
    std::string modeStr, ranges;

    // infile = "on x=10..12,y=10..12,z=10..12"
    while (infile >> modeStr >> ranges) {
        bool mode;
        if (modeStr == "on") {
            mode = true;
        } else if (modeStr == "off") {
            mode = false;
        } else {
            throw std::runtime_error("Only modes 'on' and 'off' are allowed.");
        }

        std::string s = "";
        std::vector<int> xyzLimits;
        for (auto c : ranges) {
            if (isdigit(c) || c == '-') {
                s += c;
            } else if (s.size() != 0) {
                xyzLimits.push_back(std::stoi(s));
                s = "";
            }
        }
        xyzLimits.push_back(std::stoi(s));

        bool outOfBounds = false;
        for (auto& limit : xyzLimits) {
            if (limit < -cutOff || cutOff < limit) {
                outOfBounds = true;
                break;
            }
        }

        if (!outOfBounds) {
            parsedSteps.push_back(std::make_tuple(mode, xyzLimits));
        }
    }

    return parsedSteps;
}

/// executeStep
///
/// creates a vector of all covered positions as "(x,y)"
/// @param step Instruction including the mode and the ranges for the cuboid
/// @param cubes Map containing the coordinates of all turned on switches
template <typename T>
void executeStep(const std::tuple<bool, std::vector<T>>& step,
                 std::map<std::string, char>& cubes) {
    const auto [turnOn, ranges] = step;

    for (int x = ranges[0]; x <= ranges[1]; x++) {
        for (int y = ranges[2]; y <= ranges[3]; y++) {
            for (int z = ranges[4]; z <= ranges[5]; z++) {
                std::stringstream pos;
                pos << "(" << x << "," << y << "," << z << ")";

                // Not the best to have the if in the nested loop, but performance is
                // still fine, and it is more readable
                if (turnOn) {
                    cubes[pos.str()] = '0';
                } else {
                    cubes.erase(pos.str());
                }
            }
        }
    }

    return;
}

int main(int argc, char* argv[]) {
    std::cout << "--- Day 22: Reactor Reboot ---" << std::endl;

    const std::string filename = argc > 1 ? argv[1] : "input.txt";

    auto allSteps = parseFile(filename, 50);

    std::map<std::string, char> onlineCubes;

    for (auto step : allSteps) {
        executeStep(step, onlineCubes);
    }

    std::cout << "Part1: Cubes turned on: " << onlineCubes.size() << std::endl;

    // TODO Part2 would need some PetaByte of memory using this approach. Better
    // intersect cubes mathematically

    return 0;
}
