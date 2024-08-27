# Python3 program using to find sum of array elements using recursion.

# Recursive function
def sumOfArray(arr : list, n : int, total = 0) -> int:
    if n <= 0:
        return total
    return sumOfArray(arr, n - 1, total + arr[n - 1]);

# Main
if __name__ == "__main__":
    arr = [15, 12, 13, 10]
    print('Sum of array is : {}'.format(sumOfArray(arr, len(arr))))