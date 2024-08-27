// C++ program for the above approach
#include <bits/stdc++.h>
using namespace std;
const long long mod = 1e9 + 7;
 
long long power(long long x, long long n)
{
    // If x^0 return 1
    if (n == 0)
        return 1;
 
    // If we need to find of 0^y
    if (x == 0)
        return 0;
 
    // For all other cases
    return (x * power(x, n - 1)) % mod;
}
 
// Driver Code
int main()
{
    long long x = 57;
    long long n = 75;
 
    // Function call
    cout << (power(x, n));
}