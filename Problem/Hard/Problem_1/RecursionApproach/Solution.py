def power(x, n):
    if n == 0:
        return 1  # x^0 = 1
     
    if x == 0:
        return 0  # 0^y = 0, where y is any positive integer
     
    # Recursive calculation of power modulo MOD
    return (x * power(x, n - 1)) % 1000000007 
 
x = 57
n = 75
print(power(x, n))  # Print the result of power(x, n)