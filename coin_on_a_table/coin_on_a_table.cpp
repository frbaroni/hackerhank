#include <iostream>
#include <string>
#include <limits>
using namespace std;

const int MAX_BOARD = 51;

char board[MAX_BOARD][MAX_BOARD];
int costs[MAX_BOARD][MAX_BOARD];
int max_time;
int goalY, goalX;
int height, width;

void play(int x, int y, int cost, int time) {
  if(cost >= costs[x][y]) {
    return;
  }
  if(!(x >= 0 && x < width)) {
    return;
  }
  if(!(y >= 0 && y < height)) {
    return;
  }
  costs[x][y] = cost;
  //cout << "Costs[" << x << ", " << y << "] = " << costs[x][y] << endl;
  if(time == max_time) {
    return;
  }
  if(board[x][y] == '*') {
    return;
  }
  char step = board[x][y];
  play(x, y - 1, step == 'U' ? cost : cost + 1, time + 1);
  play(x, y + 1, step == 'D' ? cost : cost + 1, time + 1);
  play(x - 1, y, step == 'L' ? cost : cost + 1, time + 1);
  play(x + 1, y, step == 'R' ? cost : cost + 1, time + 1);
}

int main() {
  cin >> height >> width >> max_time;
  for(int y = 0; y < height; y++) {
    string line;
    cin >> line;
    for(int x = 0; x < width; x++) {
      board[x][y] = line[x]; 
      costs[x][y] = numeric_limits<int>::max();
      if(board[x][y] == '*') {
        goalX = x;
        goalY = y;
      }
    }
    //cout << line << endl;
  }
  //cout << "Height: " << height << endl;
  //cout << "Width: " << width << endl;
  //cout << "MaxTime: " << max_time << endl;
  //cout << "Goal: (" << goalX << ", " << goalY << ")" << endl;
  play(0, 0, 0, 0);
  int cost = costs[goalX][goalY];
  cout << (cost != numeric_limits<int>::max() ? cost : -1) << endl;
  return 0;
}
