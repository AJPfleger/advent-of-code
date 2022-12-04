#include <iostream>
#include <fstream>
#include <vector>
#include <math.h>


int binaryLength(const std::string filename) {
  
  std::ifstream infile(filename);

  std::string line;
  infile >> line;
  std::cout << "bL line = " << line << std::endl;
  return line.length();
}

void append01more(std::string &s, const int c0, const int c1) {
  if (c1>=c0) {
    s.append("1");
  } else {
    s.append("0");
  } 
  return;
}

void append01less(std::string &s, const int c0, const int c1) {
  if (c1<c0) {
    s.append("1");
  } else {
    s.append("0");
  } 
  return;
}

std::string findSequence(const std::string filename, const std::string mode) {
  const int digits = binaryLength(filename);
  std::string s = "";

  for(int d=0; d<digits; d++) {

    std::ifstream infile(filename);

    int c0 = 0;
    int c1 = 0;
    std::string line;
    std::string lastValidLine;
    while (infile >> line) {
      if (line.compare(0,d,s) == 0) {
        if (line[d] == '1') {
          ++c1;
        } else {
          ++c0;
 	  }
	lastValidLine = line;
      }
    }

    if (c0+c1 == 1) {
	    std::cout << "aborted at line" << std::endl;
      return lastValidLine;
    }   

    if (mode.compare("oxygen") == 0) {
      append01more(s, c0, c1);
    } else if (mode.compare("co2") == 0) {
      append01less(s, c0, c1);
    } else {
      std::cout << "ERROR findSequence - mode not found";
    }
  }

  return s;
}

void printResult(const std::string name0, const std::string res0, const std::string name1, const std::string res1) { 
  std::cout << name0 << " = " << res0 << " = " << std::stoi(res0, nullptr, 2) << std::endl;
  std::cout << name1 << " = " << res1 << " = " << std::stoi(res1, nullptr, 2) << std::endl;
  std::cout << name0 << " * " << name1 << " = " << std::stoi(res0, nullptr, 2) * std::stoi(res1, nullptr, 2) << std::endl;
  return;
} 

int main() {
    const std::string filename = "input.txt";
    const int digits = binaryLength(filename);
 
  {
    std::cout << "\n*** Part 1 ***\n";

    std::ifstream infile(filename);

    std::vector<int> count0(digits, 0);
    std::vector<int> count1(digits, 0);

    std::string line;
    while (infile >> line) {
      for(int i=0; i<digits; i++) {
        if (line[i] == '1') {
          ++count1.at(i);
	} else {
          ++count0.at(i);
	}
      }
    }

    std::string gamma = "";
    std::string epsilon = "";
    for(int i=0; i<digits; i++) {
      append01more(gamma, count0.at(i), count1.at(i));
      append01less(epsilon, count0.at(i), count1.at(i));
    }

    printResult("gamma", gamma, "epsilon", epsilon);
  }

  {
    std::cout << "\n*** Part 2 ***\n";

    std::string oxygen = findSequence(filename,"oxygen");
    std::string co2 = findSequence(filename,"co2"); 

    printResult("oxygen", oxygen, "co2", co2);
  }

  return 0;
}
