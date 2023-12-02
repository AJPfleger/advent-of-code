// --- Day 6: Lanternfish ---
// https://adventofcode.com/2021/day/6
//
// https://github.com/AJPfleger
//
// g++ day06.cpp -o day06 -std=c++11 -O3

#include <fstream>
#include <iostream>
#include <numeric>

/// parseFile
///
/// @param filename File to parse
std::vector<int> parseFile(const std::string filename) {
    std::ifstream infile(filename);
    std::string fishList;
    infile >> fishList;

    std::vector<int> fish;
    std::string s = "";

    for (auto c : fishList) {
        if (isdigit(c)) {
            s += c;
        } else {
            fish.push_back(std::stoi(s));
            s = "";
        }
    }
    fish.push_back(std::stoi(s));

    return fish;
}

/// sortFish
///
/// @param fish A vector containing the age of each fish
/// @param ageMax The max age of a fish (newborn)
std::vector<long long> sortFish(const std::vector<int>& fish,
                                const int ageMax = 9) {
    std::vector<long long> ageCount(ageMax, 0);

    for (auto f : fish) {
        ++ageCount[f];
    }

    return ageCount;
}

/// waitOneDay
///
/// @param ageCount How many fish of each age are present
/// @param ageReset The age after giving birth
/// @param ageNewborn The age of a newborn
void waitOneDay(std::vector<long long>& ageCount, const int ageReset = 7,
                const int ageNewborn = 9) {
    const int ageMax = ageCount.size();
    const long long birthFish = ageCount[0];

    for (int age = 1; age < ageMax; age++) {
        ageCount[age - 1] = ageCount[age];
    }

    ageCount[ageReset - 1] += birthFish;
    ageCount[ageNewborn - 1] = birthFish;

    return;
}

int main(int argc, char* argv[]) {
    std::cout << "--- Day 6: Lanternfish ---" << std::endl;

    const std::string filename = argc > 1 ? argv[1] : "input.txt";
    const int waitTime = argc > 2 ? atoi(argv[2]) : 256;

    const std::vector<int> fish = parseFile(filename);
    std::cout << "Start with " << fish.size() << " lanternfish" << std::endl;

    std::vector<long long> ageCount = sortFish(fish);

    for (int day = 0; day < waitTime; day++) {
        waitOneDay(ageCount);
        std::cout << "Day " << day + 1 << ":  \tThere are now "
                  << std::accumulate(ageCount.begin(), ageCount.end(), 0LL)
                  << " lanternfish" << std::endl;
    }

    return 0;
}
