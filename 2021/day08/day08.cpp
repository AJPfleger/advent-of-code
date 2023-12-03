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

/// parseAndCount1478
///
/// counts only the numbers 1, 4, 7, and 8 in the "output values"
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

int main(int argc, char* argv[]) {
    std::cout << "--- Day 8: Seven Segment Search ---" << std::endl;

    const std::string filename = argc > 1 ? argv[1] : "input.txt";

    {
        const int n1478 = parseAndCount1478(filename);
        std::cout << "Part1: Count 1, 4, 7, and 8 = " << n1478 << std::endl;
    }

    // TODO Part2 would need some PetaByte of memory using this approach. Better
    // intersect cubes mathematically

    return 0;
}
