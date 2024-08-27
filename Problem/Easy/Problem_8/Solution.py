# Python3 program using to calculate length of the string using recursion.

# Recursive function
def findLength(s : str, length = 0) -> int:
    if s == '':
        return length
    return findLength(s[1:], length + 1)

# Main
if __name__ == '__main__':
    s = "Nhan Pham"
    print('Length of "{}" is: {}'.format(s, findLength(s)))