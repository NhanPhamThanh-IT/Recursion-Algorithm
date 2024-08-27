# Python code to implement above approach
 
# Function to calculate the value Of nCr using recursion
def nCr(N, r):
    res = 0
    if(r == 0):
        return 1
    else:
        res = nCr(N, r-1) * (N-r + 1) / r
    return res
 
 
# Driver code
if __name__ == "__main__":
    N = 5
    r = 3
    print(int(nCr(N, r)))