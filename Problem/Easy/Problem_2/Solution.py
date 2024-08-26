# Python3 program print N to 1 without loop

# Recursive function
def printNTo1(n : int) -> None:
    if n < 1:
        return;
    print(n, end=' ')
    printNTo1(n - 1)

# Main function
if __name__ == "__main__":
    n = 10
    printNTo1(10)