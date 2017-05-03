#include <iostream>
#include <deque>
#include <tuple>
using namespace std;

using element = tuple<int, int>;

int main() {
    deque<element> elements;
    int n;
    cin >> n;
    while(n-- > 0) {
        int operation;
        cin >> operation;
        int current_max{0};
        if(!elements.empty()) {
            current_max = get<1>(elements.back());
        }
        switch(operation) {
            case 1:
                int value;
                cin >> value;
                elements.emplace_back(value, max(current_max, value));
            break;
            case 2:
                elements.pop_back();
            break;
            case 3:
                cout << current_max << endl;
            break;
        }
    }
    return 0;
}
