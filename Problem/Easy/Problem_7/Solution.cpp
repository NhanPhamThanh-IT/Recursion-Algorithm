// C++ program using to recursive function to print the reverse of a given string.

#include <iostream>
#include <string>
#include <cstring>

// Recursive function
void printReverse(std::string s)
{
    if (s.length() == 0)
        return;
    printReverse(s.substr(1));
    std::cout << s[0];
}

void printConstChar(const char * str, int n)
{
    if (n == 0)
        return;
    std::cout << str[n - 1];
    printConstChar(str, n - 1);
}

// Main function
int main()
{
    // Solution 1
    std::string s = "Nhan Pham";
    printReverse(s);
    
    std::cout << std::endl << std::endl;
    
    // Solution 2
    const char * str = "Nhan Pham";
    printConstChar(str, strlen(str));
    
    return 0;
}