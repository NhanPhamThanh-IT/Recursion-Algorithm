# Python3 program using recursive function to print the reverse of a given string.

# Recursive function
def reverseString(s : str) -> None:
    if len(s) == 0:
        return
    print(s[-1], end='')
    reverseString(s[:-1])

def reverseString_2(s : str) -> None:
    if len(s) == 0:
        return
    reverseString_2(s[1:])
    print(s[0], end='')

# Main
if __name__ == '__main__':
    s = "Nhan Pham"
    
    # Solution 1
    reverseString(s)
    
    print('')
    
    # Solution 2
    reverseString_2(s)