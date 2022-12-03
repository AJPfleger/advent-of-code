#include <iostream>
#include <fstream>

void printStats(const int depth, const int position) {
  std::cout << "Final Depth = " << depth;
  std::cout << "\nFinal Position = " << position;
  std::cout << "\nResult = " << depth * position << std::endl;
 
  return;
}

int main() {
  {
    std::cout << "\n*** Part 1 ***\n";

    int position = 0;
    int depth = 0;
    std::ifstream infile("input.txt");

    std::string direction;
    int distance;
    while (infile >> direction >> distance)
    {
      if (direction == "forward"){
        position += distance;
      } else if (direction == "down") {
        depth += distance;
      } else {
	depth -= distance;
	if (depth < 0) {
          depth = 0;
	  std::cout << "WARNING tried to ascend above the surface" << std::endl;
	}
      }
    }
    
    printStats(depth, position);
  }

  {
    std::cout << "\n*** Part 2 ***\n";

    int position = 0;
    int depth = 0;
    int aim = 0;
    std::ifstream infile("input.txt");

    std::string direction;
    int distance;
    while (infile >> direction >> distance)
    {
      if (direction == "forward"){
        position += distance;
        depth += distance*aim;
        
	if (depth < 0) {
          depth = 0;
	  std::cout << "WARNING tried to ascend above the surface" << std::endl;
	}
      } else if (direction == "down") {
        aim += distance;
      } else {
	aim -= distance;
      }
    }

    printStats(depth, position);
  }

    return 0;
}
