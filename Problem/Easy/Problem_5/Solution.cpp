// C++ program using to convert decimal to binary number using recursion

#include <iostream>

// Recursive function
long long convertDecimalToBinary(int decimal) {
    if (decimal == 0)
        return 0;
    return (decimal % 2 + 10 * convertDecimalToBinary(decimal / 2));
}

// Main function
int main()
{
    int d = 10;
    std::cout << convertDecimalToBinary(d);
    return 0;
}