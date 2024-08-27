// C++ program using tail recursion to calculate sum of array elements.

#include <iostream>

// Recursive function
long long sumArray(int a[], int n = 0, int total = 0)
{
    if (n <= 0)
        return total;
    return sumArray(a, n - 1, total + a[n - 1]);
}

// Main function
int main()
{
    int n = 4;
    int arr[4] = {15, 12, 13, 10};
    std::cout << "Sum of array is: " << sumArray(arr, n);
    return 0;
}