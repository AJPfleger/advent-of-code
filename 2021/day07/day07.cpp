#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <numeric>


std::vector<int> getPositions(const std::string filename) {

  std::vector<int> positions;
  std::ifstream infile(filename);
  std::string line;
  infile >> line;
 
  std::string s = "";
  for(int i=0; i < line.length(); i++) {
    char c = line[i];
    if (isdigit(c)) {
      s += c;
    } else {
      positions.push_back(std::stoi(s));
      s = "";
    }     
  }

  positions.push_back(std::stoi(s));

  return positions;
}


int main() {
  const std::string filename = "input.txt";
  const std::vector<int> positions = getPositions(filename);
  const int maxPosition = *max_element(positions.begin(), positions.end());
  const int minPosition = *min_element(positions.begin(), positions.end());

  {
    int minFuel = maxPosition * positions.size();
  
    for(int p = minPosition; p <= maxPosition; p++) {
      auto absDif = [&](int a, int b){return a + std::abs(b-p);};
      int fuel = std::accumulate(positions.begin(), positions.end(), 0, absDif);
      if (fuel < minFuel) {
        minFuel = fuel;
      }
    }
    std::cout << "Part1: minFuel = " <<  minFuel << std::endl;
  }

  {
    int minFuel = maxPosition*(maxPosition+1)/2 * positions.size();
  
    for(int p = minPosition; p <= maxPosition; p++) {
      auto absDifTriangle = [&](int a, int b){return a + (std::abs(b-p)*(std::abs(b-p)+1))/2;};
      int fuel = std::accumulate(positions.begin(), positions.end(), 0, absDifTriangle);
      if (fuel < minFuel) {
        minFuel = fuel;
  	std::cout << minFuel << std::endl;
      }
    }
    std::cout << "Part2: minFuel = " <<  minFuel << std::endl;
  }

  return 0;
}
