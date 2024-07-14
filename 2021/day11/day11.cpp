// --- Day 11: Dumbo Octopus ---
// https://adventofcode.com/2021/day/11
//
// https://github.com/AJPfleger
//
// g++ day11.cpp -o day11 -std=c++11 -O3

#include <fstream>
#include <iostream>
#include <vector>

struct Octopus {
    int energy;
    bool flashed;
};

using CaveRow = std::vector<Octopus>;
using Cave = std::vector<std::vector<Octopus>>;

/// Reads in the file and populates the cave
void initialiseCave(Cave& cave, const std::string filename) {

  std::ifstream infile(filename);
  std::string line;

  while (std::getline(infile, line)) {
    CaveRow caveRow;
    for (char ch : line) {
      Octopus octopus;
      octopus.energy = ch - '0';
      octopus.flashed = false;
      caveRow.push_back(octopus);
    }
    cave.push_back(caveRow);
  }

  infile.close();

  return;
}

/// Small helper to visualise the cave for debugging
void printCave(const Cave& cave) {
  std::cout << "\n";
  for (const auto& row : cave) {
    for (const auto& octopus : row) {
      std::cout << octopus.energy;
    }
    std::cout << std::endl;
  }

  return;
}

/// Give every octopus 1 energy
void incrementCave(Cave& cave) {
  for (auto& row : cave) {
    for (auto& octopus : row) {
      octopus.energy++;
    }
  }

  return;
}

/// When the step stabilised, evaluate and prepare for the next
int countAndResetFlashed(Cave& cave) {
  int flashes = 0;
  for (auto& row : cave) {
    for (auto& octopus : row) {
      if (octopus.flashed) {
        octopus.flashed = false;
        flashes++;
      }
    }
  }

  return flashes;
}

/// Resolves all flashes in an excited cave. Probably increment before doing this.
void flashCave(Cave& cave) {

  const std::size_t nRows = cave.size();
  const std::size_t nCols = cave[0].size();

  bool flashInUpdate;

  do {
    flashInUpdate = false;

    for (std::size_t r = 0; r < nRows; ++r) {
      for (std::size_t c = 0; c < nCols; ++c) {
        if (cave[r][c].energy > 9 && !cave[r][c].flashed) {
          cave[r][c].energy = 0;
          cave[r][c].flashed = true;
          flashInUpdate = true;

          // update neighbours
          for (auto rDir: {-1, 0, 1}) {
            for (auto cDir: {-1, 0, 1}) {
              const std::size_t rNeighbour = r + rDir;
              const std::size_t cNeighbour = c + cDir;

              if ((rNeighbour < 0) || (rNeighbour >= nRows) || (cNeighbour < 0) || (cNeighbour >= nCols)) {
                continue;
              }

              if (!cave[rNeighbour][cNeighbour].flashed) {
                cave[rNeighbour][cNeighbour].energy++;
              }

            }
          }

        }
      }
    }
  } while (flashInUpdate);

  return;
}

int main(int argc, char* argv[]) {
  std::cout << "--- Day 11: Dumbo Octopus ---" << std::endl;

  const std::string filename = argc > 1 ? argv[1] : "input.txt";

  {
    Cave cave;
    initialiseCave(cave, filename);
    int flashes = 0;

    const int maxSteps = 100;

    // printCave(cave);
    for (int step = 0; step < maxSteps; step++) {
      incrementCave(cave);
      flashCave(cave);
      flashes += countAndResetFlashed(cave);

      // printCave(cave);
    }

    std::cout << "Part 1: Number of flashes = " << flashes << std::endl;
  }

  {
    Cave cave;
    initialiseCave(cave, filename);

    const std::size_t nRows = cave.size();
    const std::size_t nCols = cave[0].size();
    const int nOctopus = static_cast<int>(nRows * nCols);

    int step = 0;
    int nFlashes = 0;

    while (nFlashes < nOctopus) {
      step++;
      incrementCave(cave);
      flashCave(cave);

      nFlashes = countAndResetFlashed(cave);
    }

    // printCave(cave);

    std::cout << "Part 2: Cave synchronised in step = " << step << std::endl;
  }

  return 0;
}
