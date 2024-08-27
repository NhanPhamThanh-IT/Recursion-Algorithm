<div align="justify">

# Find the value of a number raised to its reverse

Given a number N and its reverse R. The task is to find the number obtained when the number is raised to the power of its own reverse. The answer can be very large, return the result modulo __10^9+7__.

__Examples__

```
Input : N = 2, R = 2
Output: 4
Explanation: Number 2 raised to the power of its reverse 2 gives 4 which gives 4 as a result after performing modulo 10^9+7

Input : N = 57, R = 75
Output: 262042770
Explanation: 57^75 modulo 10^9+7 gives us the result as 262042770
```

### Naive Approach

> The easiest way to solve this problem could be to traverse a loop from 1 to R(reverse) and multiply our answer with N  in each iteration.

Follow the steps mentioned below to implement the idea:

- Create a variable (say __ans__) and initialize it to __1__ to store the final result.
- Then, start a loop from __1__ and it goes till __R__. Multiply the variable __ans__ with N.
- Return the result ans with modulo of __1e9+7__.

__Time Complexity__: O(R)

__Auxiliary Space__: O(1)

### Find the value of a number raised to its reverse using Recursion

We can use the same approach as above but instead of an iterative loop, we can use recursion for the purpose.

__Time Complexity__: O(R)

__Auxiliary Space__: O(R)

### Find the value of a number raised to its reverse using Bit Manipulation

The efficient way of solving this problem could be bit manipulation, just break the problem into small parts and solve them here the concept of binary exponentiation method will be used.

- Every number can be written as the sum of powers of 2
- Traverse through all the bits of a number from __LSB__ (Least Significant Bit) to __MSB__ (Most Significant Bit) in __O(log N)__ time.

Follow the steps mentioned below to implement the idea:

__Step 1__: First, create a variable (say __ans__) and initialize it to 1 to store the result.
__Step 2__: Then, check if the given reverse number is __odd__ or not.

- If yes, then multiply the answer with pow __ans = (ans * pow) % mod__.
- Then, multiply the __pow__ with __pow__ i.e., pow = (pow*pow).
- Start shifting right by __R = R/2__.

__Step 3__: Finally, return the __ans__ as result.

__Time Complexity__: O(log R)

__Auxiliary Space__: O(1)

</div>