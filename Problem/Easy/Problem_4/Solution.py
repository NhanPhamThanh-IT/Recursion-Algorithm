# The Python3 program using for calculate the sum of first N natural numbers with recursion

# Recursive function
def sumFirstNaturalNumbers(n : int, sum = 0) -> int:
    if n == 0:
        return sum
    return sumFirstNaturalNumbers(n - 1, sum + n)

# Main
if __name__ == "__main__":
    n = 6
    print("Sum of N first natural numbers is {}".format(sumFirstNaturalNumbers(n)))