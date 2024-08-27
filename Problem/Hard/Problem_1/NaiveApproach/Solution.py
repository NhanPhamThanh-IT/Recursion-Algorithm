# Python3 code to implement the approach
 
# Function to return ans with modulo
def PowerOfNum(N, R):
    ans = 1
    mod = 1e9 + 7
    for i in range(1,R+1):
        ans *= N
        ans %= mod
    return ans
 
# Driver code
N = 57
R = 75
 
# Function call
print(int(PowerOfNum(N, R)))