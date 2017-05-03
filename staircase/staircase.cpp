#include <string>
#include <sstream>
#include <iostream>
#include <algorithm>
using namespace std;


string staircase(int width, int current);

string staircase(int width) {
    return staircase(width, width - 1);
}

string staircase(int width, int current) {
    if(current < 0) {
        return "";
    }
    stringstream res;
    for(int i = 0; i < current; i++) {
        res << " ";
    }
    for(int i = 0; i < width - current; i++) {
        res << "#";
    } 
    res << endl;
    res << staircase(width, current - 1);
    return res.str();
}

int main() {
    int width;
    cin >> width;
    cout << staircase(width);
    return 0;
}
