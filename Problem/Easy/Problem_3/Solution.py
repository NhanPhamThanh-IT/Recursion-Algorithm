# Python3 program using for calculate the mean of array using recursion

# Recursive function
def calculateMeanOfArray(arr : list, n : int) -> float:
    if n == 1:
        return float(arr[n-1])
    return float((calculateMeanOfArray(arr, n - 1) * (n - 1) + arr[n - 1]) / n)

# Main
if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6]
    n = len(arr)
    print('MEAN of the array is: {}'.format(calculateMeanOfArray(arr, n)))