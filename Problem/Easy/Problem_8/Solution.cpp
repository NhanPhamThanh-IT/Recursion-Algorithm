// C++ program using to calculate length of the string using recursion.

#include<iostream>

// Recursive function
int findLength(char * str)
{
    if (*str == '\0')
        return 0;
    return 1 + findLength(str + 1);
}

// Main function
int main()
{
    char str[] = "Nhan Pham";
    std::cout << "The length of string " << str << " is: " << findLength(str);
    return 0;
}