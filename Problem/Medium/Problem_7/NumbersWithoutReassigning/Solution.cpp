// C++ code to demonstrate printing pattern of numbers
 
#include <iostream>
using namespace std;
 
// function to print a row
int print_row(int ct, int num)
{
    // base case
    if (num == 0)
        return ct;
    cout << ct << "\t";
 
    // recursively calling print_row()
    print_row(ct + 1, num - 1);
}
 
// function to print the pattern
void pattern(int n, int count, int num)
{
    // base case
    if (n == 0)
        return;
    count = print_row(count, num);
    cout << endl;
 
    // recursively calling pattern()
    pattern(n - 1, count, num + 1);
}
 
// driver function
int main()
{
    int n = 5;
    pattern(n, 1, 1);
}