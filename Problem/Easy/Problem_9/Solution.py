# Python3 program using to find sum of its digits using recursion.

# Recursive function
def sumDigits(num : int, total = 0) -> int:
    if num == 0:
        return total
    return sumDigits(int(num // 10), total + num % 10)
    
# Main
if __name__ == '__main__':
    n = 45632
    print("Sum digits of {} is: {}".format(n, sumDigits(n)))