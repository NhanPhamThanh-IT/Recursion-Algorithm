<div align="justify">

# Sum of digit of a number using recursion

Given a number, we need to find sum of its digits using recursion.

__Examples__

```
Input : 12345
Output : 15

Input : 45632
Output :20
```

The step-by-step process for a better understanding of how the algorithm works. 
Let the number be 12345. 

- __Step 1__ -> 12345 % 10 which is equal-too 5 + ( send 12345/10 to next step ) 
- __Step 2__ -> 1234 % 10 which is equal-too 4 + ( send 1234/10 to next step ) 
- __Step 3__ -> 123 % 10 which is equal-too 3 + ( send 123/10 to next step ) 
- __Step 4__ -> 12 % 10 which is equal-too 2 + ( send 12/10 to next step ) 
- __Step 5__ -> 1 % 10 which is equal-too 1 + ( send 1/10 to next step ) 
- __Step 6__ -> 0 algorithm stops 

Following diagram will illustrate the process of recursion 

<div align="center">
<img src="https://media.geeksforgeeks.org/wp-content/uploads/20240602131617/1-37-e1513491182807-copy.webp">
</div>

</div>