#include <iostream>
#include <string>
#include <deque>
using namespace std;

bool balanced(string brackets) {
    deque<char> stack{};
    auto iter = brackets.begin(); 
    while(iter != brackets.end()) {
        char c = *iter;
        if(c == '(' || c == '[' || c == '{') {
            stack.push_back(c);
        } else {
            if(stack.empty()) {
                return false;
            }
            char expected;
            if(c == ')') {
                expected = '(';
            } else if(c == ']') {
                expected = '[';
            } else if (c == '}') {
                expected = '{';
            }
            if(stack.back() != expected) {
                return false;
            }
            stack.pop_back();
        }
        ++iter;
    }
    return stack.empty();
}

int main() {
    int n;
    string value;
    cin >> n;
    while(n-- > 0) {
        cin >> value;
        if(balanced(value)) {
            cout << "YES" << endl;
        } else {
            cout << "NO" << endl;
        }
    }
    return 0;
}
