// C++ program using to calculate the mean of array using recursion

#include <iostream>

#define MAX 100

// Recursive function
float calculateMeanArray(int a[MAX], int n)
{
    if (n == 1)
        return a[0];
    return float(calculateMeanArray(a, n - 1) * (n - 1) + a[n - 1]) / n;
}

// Main function
int main()
{
    int a[6] = { 1, 2, 3, 4, 5, 6 };
    int n = 6;
    std::cout << "Mean of the array is: " << calculateMeanArray(a, n);
    return 0;
}