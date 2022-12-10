// I am not too happy with the solution, since many things are hardcoded and it takes still a long time
// to compute the second part of the problem.
//
// This is my approach to the problem:
//
// 1. realALU is a general implementation and takes all commands from the input file
// but it is really slow
//
// 2. simulatedALU is a manual translation of the commands in input.txt - still too slow
//
// 3. integratedALU combines the commands from the file with the search algorithm
// it manages to find the first solution in a few minutes and the second one in a few hours.
// I think it does not look very nice with the unrolled loops. Maybe, in the future
// I will come up with at a different method.
// To speed it up, it would be possible to use MP to start at different positions

#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <numeric>
#include <chrono>

// realALU reads the instructions from the input file and uses them to modify the input
bool realALU(const std::string &modelS, const std::vector<std::string> &input) {

  std::string cmd;
  std::string a;
  std::string b;
  int s = 0;

  std::vector<long long> variables(4, 0);

  auto itInput = input.begin();

  while(itInput < input.end()) {
    cmd = *itInput;
    ++itInput;
    a = *itInput;
    std::vector<long long>::iterator A = variables.begin() + static_cast<int>(a[0])-119;
    ++itInput;

    if (cmd == "inp") {
       *A = modelS[s]-48;
       ++s;
    } else {
      b = *itInput;
      ++itInput;

      const int B = (isdigit(b[0])) ? std::stoi(b) : variables[static_cast<int>(b[0])-119];

      if (cmd == "add") {
        *A += B;
      } else if (cmd == "mul") {
        *A *= B;
      } else if (cmd == "div") {
        *A /= B;
      } else if (cmd == "mod") {
        *A = *A%B;
      } else if (cmd == "eql") {
        *A = (*A==B) ? 1 : 0;
      } else {
        std::cout << "ERROR Unknown command" << std::endl; 
      }
    }
  }
  std::cout << variables[3] << std::endl; 
  if (variables[3] == 0) {
    std::cout << "Found model: " << modelS << std::endl;
    return false;
  }
  return true;
}

// calZ is a parametrised version of the input file. The parameters are stored as vectors in
// the calling functions.
//long long calcZ(const int &w, const long long &z, const int &a, const int &b, const int &c) {
long long calcZ(const int &w, const long long &z, const int &a, const int &b, const int &c) {

  if ((z%26)+b == w) {
    return z/a;
  } else {
    return (z/a)*26 + w + c;
  }

}

void integratedALU() {
  const std::vector<int> a = {1,1,1,1,1,26,26,1,26,1,26,26,26,26};
  const std::vector<int> b = {14,13,12,14,13,-7,-13,10,-7,11,-9,-2,-9,-14};
  const std::vector<int> c = {12,6,4,5,0,4,15,14,6,14,8,5,14,4};
  std::vector<long long> z(13,0);

  int i;
  
  for(int d1=9; d1>0; d1--) {
    i = 0;
    z[i] = calcZ(d1,0,a[i],b[i],c[i]);
   for(int d2=9; d2>0; d2--) {
      i = 1;
      z[i] = calcZ(d2,z[i-1],a[i],b[i],c[i]);
     for(int d3=9; d3>0; d3--) {
        i = 2;
        z[i] = calcZ(d3,z[i-1],a[i],b[i],c[i]);
       for(int d4=9; d4>0; d4--) {
          i = 3;
          z[i] = calcZ(d4,z[i-1],a[i],b[i],c[i]);
          std::cout << d4 << std::endl;
         for(int d5=9; d5>0; d5--) {
          i = 4;
          z[i] = calcZ(d5,z[i-1],a[i],b[i],c[i]);
         for(int d6=9; d6>0; d6--) {
          i = 5;
          z[i] = calcZ(d6,z[i-1],a[i],b[i],c[i]);
         for(int d7=9; d7>0; d7--) {
          i = 6;
          z[i] = calcZ(d7,z[i-1],a[i],b[i],c[i]);
         for(int d8=9; d8>0; d8--) {
          i = 7;
          z[i] = calcZ(d8,z[i-1],a[i],b[i],c[i]);
         for(int d9=9; d9>0; d9--) {
          i = 8;
          z[i] = calcZ(d9,z[i-1],a[i],b[i],c[i]);
         for(int d10=9; d10>0; d10--) {
          i = 9;
          z[i] = calcZ(d10,z[i-1],a[i],b[i],c[i]);
         for(int d11=9; d11>0; d11--) {
          i =10;
          z[i] = calcZ(d11,z[i-1],a[i],b[i],c[i]);
         for(int d12=9; d12>0; d12--) {
          i =11;
          z[i] = calcZ(d12,z[i-1],a[i],b[i],c[i]);
         for(int d13=9; d13>0; d13--) {
          i =12;
          z[i] = calcZ(d13,z[i-1],a[i],b[i],c[i]);
         for(int d14=9; d14>0; d14--) {
          i =13;
          z[i] = calcZ(d14,z[i-1],a[i],b[i],c[i]);
          if (z[i] == 0) {
            std::cout << "Found model:" << d1 << d2 << d3 << d4 << d5 << d6 << d7 << d8 << d9 << d10 << d11 << d12 << d13 << d14 << std::endl;
            return;
          }  
          } 
          } 
          } 
          } 
          } 
          } 
          } 
          } 
          } 
          } 
        } 
      } 
    }
  }

  return;
}


void integratedALULower() {
  long long z0,z1,z2,z3,z4,z5,z6,z7,z8,z9,z10,z11,z12,z13;
  const std::vector<int> a = {1,1,1,1,1,26,26,1,26,1,26,26,26,26};
  const std::vector<int> b = {14,13,12,14,13,-7,-13,10,-7,11,-9,-2,-9,-14};
  const std::vector<int> c = {12,6,4,5,0,4,15,14,6,14,8,5,14,4};
  //std::vector<long long> z(15,0);

int i;

for(int d1=1; d1<10; d1++) {
  i = 0;
  z0 = calcZ(d1,0,a[i],b[i],c[i]);
 for(int d2=1; d2<10; d2++) {
  i = 1;
  z1 = calcZ(d2,z0,a[i],b[i],c[i]);
 for(int d3=1; d3<10; d3++) {
  i = 2;
  z2 = calcZ(d3,z1,a[i],b[i],c[i]);
 for(int d4=1; d4<10; d4++) {
  i = 3;
  z3 = calcZ(d4,z2,a[i],b[i],c[i]);
  std::cout << d4 << std::endl;
 for(int d5=1; d5<10; d5++) {
  i = 4;
  z4 = calcZ(d5,z3,a[i],b[i],c[i]);
 for(int d6=1; d6<10; d6++) {
  i = 5;
  z5 = calcZ(d6,z4,a[i],b[i],c[i]);
 for(int d7=1; d7<10; d7++) {
  i = 6;
  z6 = calcZ(d7,z5,a[i],b[i],c[i]);
 for(int d8=1; d8<10; d8++) {
  i = 7;
  z7 = calcZ(d8,z6,a[i],b[i],c[i]);
 for(int d9=1; d9<10; d9++) {
  i = 8;
  z8 = calcZ(d9,z7,a[i],b[i],c[i]);
 for(int d10=1; d10<10; d10++) {
  i = 9;
  z9 = calcZ(d10,z8,a[i],b[i],c[i]);
 for(int d11=1; d11<10; d11++) {
  i =10;
  z10 = calcZ(d11,z9,a[i],b[i],c[i]);
 for(int d12=1; d12<10; d12++) {
  i =11;
  z11 = calcZ(d12,z10,a[i],b[i],c[i]);
 for(int d13=1; d13<10; d13++) {
  i =12;
  z12 = calcZ(d13,z11,a[i],b[i],c[i]);
 for(int d14=1; d14<10; d14++) {
  i =13;
  z13 = calcZ(d14,z12,a[i],b[i],c[i]);
  if (z13 == 0) {
    std::cout << "Found model:" << d1 << d2 << d3 << d4 << d5 << d6 << d7 << d8 << d9 << d10 << d11 << d12 << d13 << d14 << std::endl;
    return;
  }  
} 
} 
} 
} 
} 
} 
} 
} 
} 
} 
} 
} 
}
}

  return;
}

//bool fastProgram2(const std::string &modelS, const std::vector<int> &a, const std::vector<int> &b, const std::vector<int> &c) {
//  long long z = -17220238;
//  z += modelS[0]*456976;
//  z += modelS[1]*17576;
//  z += modelS[2]*676;
//  z += modelS[3]*26;
//  z += modelS[4];
//
//  for(int i=5; i<13; i++) {
//    z = subFunction(modelS[i]-48,z,a[i],b[i],c[i]);
////    std::cout << z << std::endl;
//  }
//
//  if (z == modelS[13]-34) {
//    std::cout << "Found model: " << modelS << std::endl;
//    return false;
//  }
//  return true;
//}

int main() {
  const std::string filename = "input.txt";
  long long model = 1e15-1;
  bool lookingForModel = true;

  std::ifstream infile("input.txt");
  std::string s;
  std::vector<std::string> input;
  while (infile >> s) {
    input.push_back(s);
  }

integratedALU();
std::cout << "result above" << std::endl;
//  const std::vector<int> a = {1,1,1,1,1,26,26,1,26,1,26,26,26};
//  const std::vector<int> b = {14,13,12,14,13,-7,-13,10,-7,11,-9,-2,-9};
//  const std::vector<int> c = {12,6,4,5,0,4,15,14,6,14,8,5,14};
//  auto test = runProgram("99999212949957",input);
//  auto start = std::chrono::steady_clock::now();  
//  long long count = 0;
//  while( (lookingForModel)  & (count < 1e7)) {
//    ++count;
//    std::string modelS = std::to_string(model);
//    if (!(modelS.find('0') != std::string::npos)) {
//      lookingForModel = fastProgram2(modelS, a, b, c);
//    }
//    --model;
//
//    if (model%10000000 == 0) std::cout << model << std::endl;
//  }
//
//  auto end = std::chrono::steady_clock::now();
//  std::chrono::duration<double> elapsed_seconds = end-start;
//  std::cout << "elapsed time: " << elapsed_seconds.count() << "s\n";
//  


//1e5: 9.16276s
// with -O3
//  long long count = 0;
//  while (lookingForModel & (count < 1e5)) {
//    ++count;
//    std::string modelS = std::to_string(model);
//    if (modelS.find('0') != std::string::npos) {
//        ; // found
//    } else {
//      lookingForModel = runProgram(modelS, filename);
//    }
//    --model;
//
//    if (model%100000 == 0) std::cout << model << std::endl;
//  }

//hand input over as &vector
//1e5: 2.38496s
// without optimization
// 0.6 with -O3


  return 0;
}
