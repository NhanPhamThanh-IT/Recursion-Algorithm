<div align="justify">

# Decimal to binary number using recursion

Given a decimal number as input, we need to write a program to convert the given decimal number into an equivalent binary number. 

__Examples__

```
Input : 7
Output :111

Input :10
Output :1010
```

Below is Recursive solution:

```
findBinary(decimal)
   if (decimal == 0)
      binary = 0
   else
      binary = decimal % 2 + 10 * (findBinary(decimal / 2))
```

<div align="center">
<img src="https://media.geeksforgeeks.org/wp-content/uploads/decimal2binary-1-300x240.png">
</div>

Step-by-step process for a better understanding of how the algorithm works 
Let the decimal number be 10. 

- __Step 1__ -> 10 % 2 which is equal-too 0 + 10 * ( 10/2 ) % 2 
- __Step 2__ -> 5 % 2 which is equal-too 1 + 10 * ( 5 / 2) % 2
- __Step 3__ -> 2 % 2 which is equal-too 0 + 10 * ( 2 / 2 ) % 2
- __Step 4__ -> 1 % 2 which is equal-too 1 + 10 * ( 1 / 2 ) % 2

<div align="center">
<img src="https://media.geeksforgeeks.org/wp-content/uploads/20230406084409/recursion.jpg">
</div>

</div>