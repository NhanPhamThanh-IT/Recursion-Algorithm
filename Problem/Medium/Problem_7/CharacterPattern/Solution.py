# Python3 code to demonstrate printing pattern of alphabets
 
# function to print a row
def print_row(no, val):
    # base case
    if (no == 0):
        return;
    print(chr(val + 64), end=" ");
 
    # recursively calling print_row()
    print_row(no - 1, val);
 
# function to print the pattern
def pattern(n, num):
    # base case
    if (n == 0):
        return;
    print_row(num - n + 1, num - n + 1);
    print();
 
    # recursively calling pattern()
    pattern(n - 1, num);
 
# Driver code
if __name__ == '__main__':
    n = 5;
    pattern(n, n);