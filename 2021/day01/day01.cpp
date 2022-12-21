#include <iostream>
#include <fstream>

int main() {
  {
    int result = 0;
    std::ifstream infile("input.txt");

    int prevMeas = INT_MAX;
    int meas;
    while (infile >> meas)
    {
      if (meas > prevMeas){
        ++result;
      }
      prevMeas = meas;
    }

    std::cout << "*** Part 1 ***\n";
    std::cout << result << " measurements are larger than the previous measurement." << std::endl;
  }

  {
    int result = 0;
    std::ifstream infile("input.txt");

    int prevMeas [3] = {INT_MAX, INT_MAX, INT_MAX};
    int meas;
    int i = 0;
    while (infile >> meas)
    {
      prevMeas[i%3] = prevMeas[i%3] + meas;
      prevMeas[(i+1)%3] = prevMeas[(i+1)%3] + meas;

      if ((i>2) and (prevMeas[i%3] > prevMeas[(i+2)%3])) {
        ++result;
      }

      prevMeas[(i+2)%3] = meas;

      ++i;
    }

    std::cout << "\n*** Part 2 ***\n";
    std::cout << result << " groups are larger than the previous groups." << std::endl;
  }

    return 0;
}
