# Python3 code to convert Binary to Gray code using recursion
 
# Function to change Binary to Gray using recursion

def binary_to_gray(n):
    if not(n):
        return 0
 
    # Taking last digit
    a = n % 10
 
    # Taking second last digit
    b = int(n / 10) % 10
 
    # If last digit are opposite bits
    if (a and not(b)) or (not(a) and b):
        return (1 + 10 * binary_to_gray(int(n / 10)))
 
    # If last two bits are same
    return (10 * binary_to_gray(int(n / 10)))
 
 
# Driver Code
binary_number = 1011101
print(binary_to_gray(binary_number), end='')