# Python3 to find Product of 2 Numbers using Recursion 
  
# Recursive function to calculate multiplication of two numbers  
def product( x , y ): 
    # If x is less than y swap the numbers 
    if x < y: 
        return product(y, x) 
      
    # Iteratively calculate y times sum of x 
    elif y != 0: 
        return (x + product(x, y - 1)) 
      
    # If any of the two numbers is zero return zero 
    else: 
        return 0
  
# Driver code 
x = 5
y = 2
print( product(x, y))