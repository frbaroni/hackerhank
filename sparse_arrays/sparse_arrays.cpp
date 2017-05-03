#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <unordered_map>
using namespace std;

int main() {
    unordered_map<string, long> words{};
    string word;
    int n;
    cin >> n;
    while(n-- > 0) {
        cin >> word;
        words[word]++;
    }
    cin >> n;
    while(n-- > 0) {
        cin >> word;
        cout << words[word] << endl;
    }
    return 0;
}
