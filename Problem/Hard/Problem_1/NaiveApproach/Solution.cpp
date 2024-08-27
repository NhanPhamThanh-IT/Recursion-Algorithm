// C++ code to implement the approach
 
#include <bits/stdc++.h>
using namespace std;
 
// Function to return ans with modulo
int PowerOfNum(int N, int R)
{
    long long ans = 1, mod = 1e9 + 7;
    for (int i = 1; i <= R; i++) {
        ans *= N;
        ans %= mod;
    }
    return ans;
}
 
// Driver code
int main()
{
    int N = 57, R = 75;
 
    // Function call
    cout << PowerOfNum(N, R);
 
    return 0;
}