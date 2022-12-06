#include <iostream>
#include <fstream>
#include <vector>


class Bingo {
  private:
    constexpr static int fieldSize = 5;

    void checkBingo(){
      // dim1
      for(int n=0; n<fieldSize; n++) { 
        for(int m=0; m<fieldSize; m++) {
          if (field[n][m] != -1) break;
	  if (m == fieldSize-1) {
            won = true;
	    return;
	  }
	}
      }

      // dim2
      for(int n=0; n<fieldSize; n++) { 
        for(int m=0; m<fieldSize; m++) {
          if (field[m][n] != -1) break;
          if (m == fieldSize-1) {
            won = true;
	    return;
	  }
	}
      }
      return;
    }

  public:
    int field[fieldSize][fieldSize] {};
    int stepsToWin {};
    int fieldSum {};
    int lastMatch {};
    bool won {};

    // constructor
    Bingo() {
      int field[fieldSize][fieldSize] = {};
      int stepsToWin = 0;
      int fieldSum = 0;
      bool won = false;
    }

    void draw(const int newNumber){
      if (won) return;
      ++stepsToWin;

      for(int n=0; n<fieldSize; n++) {
        for(int m=0; m<fieldSize; m++) {
          if (field[n][m] == newNumber) {
            field[n][m] = -1;
	    lastMatch = newNumber;
	    fieldSum -= newNumber;
      checkBingo();
	    return;
	  }
	}
      }
      return;
    }

    int score() {
      return fieldSum * lastMatch;
    }
};

std::vector<int> getDrawSequence(const std::string filename) {

  std::vector<int> drawSequence;
  std::ifstream infile(filename);
  std::string line;
  infile >> line;
 
  std::string s = "";
  for(int i=0; i < line.length(); i++) {
    char c = line[i];
    if (isdigit(c)) {
      s += c;
    } else {
      drawSequence.push_back(std::stoi(s));
      s = "";
    }     
  }

  drawSequence.push_back(std::stoi(s));

  return drawSequence;
}


int main() {
  const std::string filename = "input.txt";
  const std::vector<int> drawSequence = getDrawSequence(filename);
  std::ifstream infile(filename);
  int fieldValue;

  int stepsMin = drawSequence.size();
  int scoreMin = 0;
  int stepsMax = 0;
  int scoreMax = 0;

  // discard first line
  std::string line;
  infile >> line;

  int fieldPos = 0;
  Bingo singleBingo = Bingo();

  while (infile >> fieldValue) {
    singleBingo.field[fieldPos/5][fieldPos%5] = fieldValue;
    singleBingo.fieldSum += fieldValue;
    ++fieldPos;

    if (fieldPos == 25) {
      for(auto & draw : drawSequence) {
        singleBingo.draw(draw);
      }

      if (singleBingo.stepsToWin < stepsMin) {
        stepsMin = singleBingo.stepsToWin;
        scoreMin = singleBingo.score();
      }
      
      if (singleBingo.stepsToWin > stepsMax) {
        stepsMax = singleBingo.stepsToWin;
        scoreMax = singleBingo.score();
      }

      fieldPos = 0;
      singleBingo = Bingo();
    }
  }

  std::cout << "scoreMin = " <<  scoreMin << std::endl;
  std::cout << "scoreMax = " <<  scoreMax << std::endl;

  return 0;
}
