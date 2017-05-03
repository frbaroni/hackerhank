#include <iostream>
using namespace std;

int main() {
    int a[100]{0};
    int n, v;
    cin >> n;
    while(n-- > 0) {
        cin >> v;
        a[v]++;
    }
    for(int i = 0; i < 100; i++) {
        if(a[i] == 1) {
            cout << i << endl;
            break;
        }
    }
    return 0;
}
