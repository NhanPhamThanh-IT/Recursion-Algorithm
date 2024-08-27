# Python3 code to demonstrate star pattern 
 
# function to print spaces
def print_space(space):
     
    # base case
    if (space == 0):
        return;
     
    print(" ", end=" ");
 
    # recursively calling print_space()
    print_space(space - 1);
 
# function to print asterisks
def print_asterisk(asterisk):
     
    # base case
    if (asterisk == 0):
        return;
     
    print("*", end =" ");
 
    # recursively calling print_asterisk()
    print_asterisk(asterisk - 1);
 
# function to print the pattern
def pattern(n, num):
     
    # base case
    if (n == 0):
        return;
     
    print_space(n - 1);
    print_asterisk(num - n + 1);
    print();
 
    # recursively calling pattern()
    pattern(n - 1, num);
 
# Driver code
if __name__ == '__main__':
    n = 5;
    pattern(n, n);