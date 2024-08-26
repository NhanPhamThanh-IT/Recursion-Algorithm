// C++ program print numbers from N to 1 without using loops

#include <iostream>

// Recursive function
void print1ToN(int n)
{
    if (n < 1)
        return;
    std::cout << n << " ";
    print1ToN(n - 1);
}

// Main function
int main()
{
    int n = 10;
    print1ToN(n);
    return 0;
}