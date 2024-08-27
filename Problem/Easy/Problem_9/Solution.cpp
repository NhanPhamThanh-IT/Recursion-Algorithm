// C++ program using to find sum of its digits using recursion.

#include <iostream>

// Recursive function
int sum_digits(int n, int sum = 0)
{
    if (n == 0)
        return sum;
    return sum_digits(n/10, sum+n%10);
}

// Main function
int main()
{
    int n = 45632;
    std::cout << "Sum digits of " << n << " is: " << sum_digits(n);
    return 0;
}