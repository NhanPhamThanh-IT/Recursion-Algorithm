# Python 3 program print 1 to N without using loops.

# Recursive function
def print1ToN(n, cnt=1):
    if cnt > n:
        return
    print(cnt, end=' ')
    print1ToN(n, cnt+1)

# Main function
if __name__ == '__main__':
    n = 10
    print1ToN(n)