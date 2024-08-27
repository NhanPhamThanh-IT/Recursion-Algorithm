# Python3 code to demonstrate printing pattern of numbers
 
# function to print a row
def print_row(ct, num):
     
    # base case
    if (num == 0):
        return ct;
    print(ct, end = " ");
 
    # recursively calling print_row()
    return print_row(ct + 1, num - 1);
 
# function to print the pattern
def pattern(n, count, num):
     
    # base case
    if (n == 0):
        return;
    count = print_row(count, num);
    print();
 
    # recursively calling pattern()
    pattern(n - 1, count, num + 1);
 
# Driver Code
if __name__ == '__main__':
    n = 5;
    pattern(n, 1, 1);