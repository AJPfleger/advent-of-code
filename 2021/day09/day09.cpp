#include <iostream>
#include <fstream>
#include <vector>
#include <map>

std::vector<std::vector<int>> getField(const std::string filename) {

  std::vector<std::vector<int>> field;
  
  {
    std::ifstream infile(filename);
    std::string line;
  
    infile >> line;
    std::vector<int> vecLine(line.length()+2,10);
    field.push_back(vecLine);
  }
  
  std::ifstream infile(filename);
  std::string line;

  while(infile >> line) {
    std::vector<int> vecLine(1,10);   

    for(int i=0; i < line.length(); i++) {
      vecLine.push_back(line[i]-48);
    }
    vecLine.push_back(10);
    field.push_back(vecLine);
  }

  std::vector<int> vecLine(line.length()+2,10);
  field.push_back(vecLine);
  
  return field;
}

bool checkPosition(const std::vector<std::vector<int>> &field, const int x, const int y) {

  const int pos = field[x][y];

  if (pos < field[x-1][y] && pos < field[x+1][y] && pos < field[x][y-1] && pos < field[x][y+1]) {
    return true;
  }

  return false;

}

bool checkNeighbours(const std::vector<int> &xy,
		     const std::map<std::vector<int>, std::string> &basin) {

  const int x = xy[0];
  const int y = xy[1];
  bool foundNeighbour = false;

  if (basin.find({x-1,y}) != basin.end()) {
    foundNeighbour =  true;
  } else if (basin.find({x+1,y}) != basin.end()) {
    foundNeighbour =  true;
  } else if (basin.find({x,y-1}) != basin.end()) {
    foundNeighbour =  true;
  } else if (basin.find({x,y+1}) != basin.end()) {
    foundNeighbour =  true;
  }

  return foundNeighbour;
}	


int getBasinSize(std::map<std::vector<int>, std::string> &uncovered,
		  std::map<std::vector<int>, std::string> &covered,
		  const std::vector<int> &s) {

  bool foundNew = true;
  std::map<std::vector<int>, std::string> basin;
  basin[s] = "";

  while (foundNew) {
    foundNew = false;
    for(auto & XY : uncovered) {
      const std::vector<int> xy = XY.first;
      const bool connected = checkNeighbours(xy,basin);
      if (connected){
        foundNew = true;
	covered[xy] = "";
	basin[xy] = "";
	uncovered.erase(xy);
	break;
      }
    }
  }

  return basin.size();
}


int main() {
  const std::string filename = "input.txt";
  const std::vector<std::vector<int>> field = getField(filename);

  std::map<std::vector<int>, std::string> sinks;
  {
    int sumRisk = 0;
  
    for(int x = 1; x < field.size()-1; x++) {
      for(int y = 1; y < field[x].size()-1; y++) {
        if (checkPosition(field,x,y)) {
          sumRisk += field[x][y]+1;
	  const std::vector<int> xy{x,y};
          sinks[xy] = "";
	}
      }
    }
    std::cout << "Part 1: sumRisk = " <<  sumRisk << std::endl;
  }

  {
    std::map<std::vector<int>, std::string> covered;
    std::map<std::vector<int>, std::string> uncovered;
  
    for(int x = 0; x < field.size(); x++) {
      for(int y = 0; y < field[0].size(); y++) {
        const std::vector<int> xy{x,y};
  
        if (field[x][y] > 8) { 
          covered[xy] = "";
        } else if (sinks.find(xy) != sinks.end()) {
          covered[xy] = "";
        } else {
          uncovered[xy] = "";
        }
      }
    }
  
    std::vector<int> basinSizes;
    for(auto & s : sinks) {
      const int bSize = getBasinSize(uncovered,covered,s.first);
      basinSizes.push_back(bSize);
    }
  
    sort(basinSizes.begin(),basinSizes.end(), std::greater<int>());
  
    int res = 1;
    for(int i=0; i<3; i++) {
      res *= basinSizes[i];
    }
  
    std::cout << "Part 2: result = " << res << std::endl;
  }

  return 0;
}
