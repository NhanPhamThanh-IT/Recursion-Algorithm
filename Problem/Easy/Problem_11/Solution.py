# python code to print first n fibonacci numbers
 
 
def fibonacci_numbers(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        # printing fibonacci numbers
        return fibonacci_numbers(num-2)+fibonacci_numbers(num-1)
 
 
n = 7
for i in range(0, n):
    print(fibonacci_numbers(i), end=" ")