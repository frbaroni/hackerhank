#include <iostream>
#include <vector>
#include <algorithm>
#include <iterator>
using namespace std;

int lis_bad_perf(int n, vector<int>& values) {
    // Initialize lis[n] with [1, 1, ...]
    vector<int> lis(n, 1);

    // Remove base case: only a single element
    if(n > 1) { 
        // Iterate all elements
        for(int i = 1; i < n; i++)
            // Iterate previous elements
            for(int j = 0; j < i; j++)
                // If current element values[i] is greater than previous
                // element values[j] and current lis[i] is smaller than
                // previous lis[j], then, we can assume current element also
                // contains the previous subsequent set (we get previous value
                // and add +1 becasue of the current value)
                if(values[i] > values[j] && lis[i] < lis[j] + 1)
                    lis[i] = lis[j] + 1;
    }

    // Retrieve the maximum lis[i] and output it to cout
    return *max_element(lis.begin(), lis.end());
}

int lis_good_perf(int n, vector<int>& values) {
    vector<int> subseq;
    for(int i = 0; i < n; i++) {
        int a = values[i];
        int tmp = lower_bound(subseq.begin(), subseq.end(), a) - subseq.begin();
        if(tmp >= subseq.size()) {
            subseq.push_back(a);
        } else {
            subseq[tmp] = a;
        }
    }
    return subseq.size();
}

int main() {
    int n;

    // Read N
    cin >> n;

    // Initialize values[n] with cin
    vector<int> values;
    copy(istream_iterator<int>{cin}, istream_iterator<int>{},
                back_inserter(values));

    cout << lis_good_perf(n, values) << endl;

    return 0;
}
