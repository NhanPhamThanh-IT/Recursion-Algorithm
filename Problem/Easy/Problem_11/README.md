<div align="justify">

# Program to print first n Fibonacci Numbers | Set 1

Given an integer __N__. The task is to find the first __N__ Fibonacci numbers.

<div align="center">
<img src="https://media.geeksforgeeks.org/wp-content/cdn-uploads/fibonacci-sequence.png">
</div>

__Examples__

```
Input: n = 3
Output: 0 1 1

Input: n = 7
Output: 0 1 1 2 3 5 8
```

### Program to print first ‘n’ Fibonacci Numbers using recursion

Below is the idea to solve the problem:

Use recursion to find nth fibonacci number by calling for n-1 and n-2 and adding their return value. The base case will be if n=0 or n=1 then the fibonacci number will be 0 and 1 respectively.

Follow the below steps to Implement the idea - Build a recursive function that takes integer N as a parameter.

- If N = 0 fibonacci number will be 0.
- Else if n = 1 Fibonacci number will be 1.
- Else return value for func(n-1) + func(n-2).

__Time Complexity__: O(n*2n)

__Auxiliary Space__: O(n), For recursion call stack.

### An iterative approach to print first ‘n’ Fibonacci numbers

Below is the idea to solve the problem

- Use two variables __f1__ and __f2__ and initialize with 0 and 1 respectively because the 1st and 2nd elements of the Fibonacci series are __0__ and __1__ respectively. 
- Iterate from __1 to n-1__ and print __f2__ then store f2 in temp variable and update f2 with f2 + f1 and f1 as f2.

__Time Complexity__: O(n) 

__Auxiliary Space__: O(1)

</div>