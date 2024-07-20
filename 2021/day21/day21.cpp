// --- Day 21: Dirac Dice ---
// https://adventofcode.com/2021/day/21
//
// https://github.com/AJPfleger
//
// g++ day13.cpp -o day13 -std=c++11 -O3

#include <fstream>
#include <iostream>
#include <vector>
#include <sstream>
#include <cassert>

//using PointList = std::vector<std::pair<int, int>>;
//using Fold = std::pair<char, int>;
//using FoldingList = std::vector<Fold>;
//
//std::tuple<PointList, FoldingList> getPointsAndFolds(
//    const std::string filename
//) {
//  PointList points;
//  FoldingList folds;
//
//  std::ifstream infile(filename);
//  std::string line;
//  std::string coordinate;
//
//  // read points
//  while (std::getline(infile, line) && !line.empty()) {
//    std::string x, y;
//    std::stringstream ss(line);
//
//    std::getline(ss, x, ',');
//    std::getline(ss, y, ',');
//    // std::cout << x << "|" << y << std::endl;
//    points.push_back(std::make_pair(std::stoi(x),std::stoi(y)));
//  }
//
//  // read folds
//  while (std::getline(infile, line)) {
//    const char direction = line[11];
//    const int foldingPosition = std::stoi(line.substr(13));
//    // std::cout << line[11] << "|" << foldingPosition << std::endl;
//
//    folds.push_back(std::make_pair(direction, foldingPosition));
//  }
//
//  infile.close();
//
//  return std::make_tuple(points, folds);
//}
//
//void reducePoints(PointList& points) {
//  std::sort(points.begin(), points.end());
//  points.erase(std::unique(points.begin(), points.end()), points.end());
//  return;
//}
//
//void applyFold(const Fold& fold, PointList& points) {
//  auto [direction, foldingPosition] = fold;
//  // std::cout << "fold:" << direction << "|" << foldingPosition << std::endl;
//
//  for(auto& [x, y] : points) {
//    // std::cout << "before: " << x << "|" << y << std::endl;
//    if (direction == 'x') {
//      if (x > foldingPosition) {
//        x = foldingPosition - (x - foldingPosition);
//      }
//    } else if (direction == 'y') {
//      if (y > foldingPosition) {
//        y = foldingPosition - (y - foldingPosition);
//      }
//    } else {
//      throw std::runtime_error("Direction seems unclear.");
//    }
//    // std::cout << "after:  " << x << "|" << y << std::endl;
//  }
//
//  reducePoints(points);
//
//  return;
//}
//
//void printPoints(PointList& points) {
//  int xMax = 0;
//  int yMax = 0;
//  // Find dimensions
//  for(const auto& [x, y] : points) {
//    xMax = std::max(xMax, x);
//    yMax = std::max(yMax, y);
//  }
//
//  std::vector<std::string> paper;
//
//  // Initialize each string with the specified number of zeros
//  for (int i = 0; i <= yMax; ++i) {
//    paper.push_back(std::string(xMax+1, ' '));
//  }
//
//  for(const auto& [x, y] : points) {
//    paper[y][x] = '\xDB';
//  }
//
//  for (const auto& line : paper) {
//    std::cout << line << std::endl;
//  }
//
//  return;
//}

std::vector<int> getStartingPositions(const std::string filename) {


  std::vector<int> startingPosition;

  std::ifstream infile(filename);
  std::string line;

  // read points
  while (std::getline(infile, line)) {
    startingPosition.push_back(line[28] - '0');
  }

  infile.close();

  return startingPosition;
}


int main(int argc, char* argv[]) {
  std::cout << "--- Day 21: Dirac Dice ---" << std::endl;

  const std::string filename = argc > 1 ? argv[1] : "input.txt";

  {
    const int maxThrows = 3;
    const int maxPositions = 10;
    const int maxDice = 100;
    const int maxScore = 1000;
    std::vector<int> positions = getStartingPositions(filename);
    std::vector<int> score = {0, 0};

    int dice = 1;
    int dieRolls = 0;
    int player = 0;

    constexpr int maxRolls = 2 * maxScore * maxThrows;
    while (dieRolls < maxRolls) {
      int sum = 0;
      for (int t = 0; t < maxThrows; t++) {
        sum += dice;
        ++dice;
        dice = (dice - 1) % maxDice + 1;
        ++dieRolls;
      }

      positions.at(player) = (positions.at(player) + sum - 1) % maxPositions + 1;

      score.at(player) += positions.at(player);
      if (score.at(player) >= maxScore) {
        break;
      }

      player = (player + 1) % 2;
    }

    const int result = score.at((player + 1) % 2) * dieRolls;

    std::cout << "Part 1: result = " << result << std::endl;

    if (filename == "testinput.txt") {
      assert(result == 739785);
    }

  }







//  {
//    auto [points, folds] = getPointsAndFolds(filename);
//
//    for (const auto& f : folds) {
//      applyFold(f, points);
//      break;
//    }
//
//    std::cout << "Part 1: Unique points after 1 fold = " << points.size() << std::endl;
//  }
//
//  {
//    auto [points, folds] = getPointsAndFolds(filename);
//
//    for (const auto& f : folds) {
//      applyFold(f, points);
//    }
//
//    std::cout << "Part 2: Final message:" << std::endl;
//    printPoints(points);
//  }

  return 0;
}
