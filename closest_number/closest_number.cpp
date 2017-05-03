#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int closest(int a, int b, int x) {
    // Calculate our goal
    int goal = pow(a, b);

    // Calculate our smallest possible closest number:
    //   goal - reminder(goal % x)
    int smaller = goal - (goal % x);
    // Calculate the greatest possible closest number:
    //   smaller + x
    int bigger = smaller + x;

    // Calculate the deltas to goal
    int delta_smaller = abs(smaller - goal);
    int delta_bigger = abs(bigger - goal);
    // If smaller is closest to goal, return smaller
    if(delta_smaller < delta_bigger)
        return smaller;
    // Otherwise, return bigger
    return bigger;
}

int main() {
    int testcases;
    cin >> testcases;
    while(testcases-- > 0) {
        int a, b, x;
        cin >> a >> b >> x;
        cout << closest(a, b, x) << endl;
    }
    return 0;
}
