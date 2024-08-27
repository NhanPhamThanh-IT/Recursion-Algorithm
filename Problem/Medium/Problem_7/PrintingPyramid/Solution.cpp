// C++ code to demonstrate star pattern
 
#include <iostream>
using namespace std;
 
// function to print spaces
void print_space(int space)
{
    // base case
    if (space == 0)
        return;
    cout << " ";
 
    // recursively calling print_space()
    print_space(space - 1);
}
 
// function to print asterisks
void print_asterisk(int asterisk)
{
    // base case
    if (asterisk == 0)
        return;
    cout << "* ";
 
    // recursively calling asterisk()
    print_asterisk(asterisk - 1);
}
 
// function to print the pattern
void pattern(int n, int num)
{
    // base case
    if (n == 0)
        return;
    print_space(n - 1);
    print_asterisk(num - n + 1);
    cout << endl;
 
    // recursively calling pattern()
    pattern(n - 1, num);
}
 
// driver function
int main()
{
    int n = 5;
    pattern(n, n);
    return 0;
}