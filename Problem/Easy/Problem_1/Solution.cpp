// C++ program print numbers from 1 to N withou using any loops.

#include <iostream>

// Recursive function
void print1ToN(int n = 0, int cnt = 1)
{
    if (cnt > n)
        return;
    std::cout << cnt << " ";
    print1ToN(n, cnt + 1);
}

// Main function
int main()
{
    int n = 10;
    print1ToN(n);
    return 0;
}