# Python code to implement the above approach
def power(num, rev):
 
    ans = 1
    mod = 1000000007
    pow = num * 1
     
    while (rev > 0) :
 
        # When rev is odd
        if (rev % 2 == 1) :
            ans = (ans * pow) % mod
             
        pow = (pow * pow) % mod
 
        # Shifting right (rev = rev/2 )
        rev >>= 1
             
    return ans
 
if __name__ == "__main__":
 
    N = 57
    R = 75
 
    # Function call
    print(power(N, R))