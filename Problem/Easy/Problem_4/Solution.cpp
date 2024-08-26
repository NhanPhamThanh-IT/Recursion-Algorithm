// Write the program to calculate sum of first N natural numbers
#include <iostream>

// Recursive function
long long sumNaturalNumbers(int n = 0, long long sum = 0)
{
    if (n == 0)
        return sum;
    return sumNaturalNumbers(n - 1, sum + n);
}

// Main function
int main()
{
    int n = 6;
    std::cout << sumNaturalNumbers(n);
    return 0;
}