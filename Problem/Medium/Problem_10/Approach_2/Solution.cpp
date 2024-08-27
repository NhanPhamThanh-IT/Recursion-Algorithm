// C++ code to implement above approach
#include <bits/stdc++.h>
using namespace std;
 
// Function to calculate the value of nCr using recursion
int nCr(int N, int r)
{
    int res = 0;
    if (r == 0) {
        return 1;
    }
    else {
        res = nCr(N, r - 1)
              * (N - r + 1) / r;
    }
    return res;
}
 
// Driver code
int main()
{
    int N = 5, r = 3;
    cout << nCr(N, r);
    return 0;
}