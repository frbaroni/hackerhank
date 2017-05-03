#include <iostream>
using namespace std;

int main() {
    long n;
    cin >> n;
    long result = 1;
    for(long x = 1; x <= n; x++) {
        if((n + x) == (n xor x)) {
            result++;
        }
    }
    cout << result << endl;
    return 0;
}
