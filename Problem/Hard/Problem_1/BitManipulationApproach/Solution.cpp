// C++ code to implement the approach
 
#include <bits/stdc++.h>
using namespace std;
 
// Function to find the power
long long power(int num, int rev)
{
    long long ans = 1;
    long long mod = 1e9 + 7;
    long long pow = num * 1LL;
 
    while (rev > 0) {
        // When reverse is odd
        if (rev & 1) {
            ans = (ans * pow) % mod;
        }
        pow = (pow * pow) % mod;
        // Shifting right (rev = rev/2 )
        rev >>= 1;
    }
    return ans;
}
 
// Driver Code
int main()
{
    int N = 57, R = 75;
 
    // Function call
    cout << power(N, R) << endl;
 
    return 0;
}