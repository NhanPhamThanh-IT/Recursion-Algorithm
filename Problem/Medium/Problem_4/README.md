<div aligne="justify">

# Binary to Gray code using recursion

Given the Binary code of a number as a decimal number, we need to convert this into its equivalent Gray Code. Assume that the binary number is in the range of integers. For the larger value, we can take a binary number as string.

> In __gray code__, only one bit is changed in 2 consecutive numbers. 

### Examples

```
Input: 1001 
Output: 1101
Explanation: 1001 -> 1101 -> 1101 -> 1101

Input: 11
Output: 10
Explanation: 11 -> 10
```

### Approach

The idea is to check whether the last bit and second last bit are same or not, if it is same then move ahead otherwise add 1.

Follow the steps to solve the given problem:

```
binary_to_grey(n)
if n == 0
    grey = 0
else if last two bits are opposite  to each other
    grey = 1 + 10 * binary_to_gray(n/10))
else if last two bits are same
    grey = 10 * binary_to_gray(n/10))
```

__Time Complexity__: O(logN), Traverse through all the digits, as there are logN bits.

__Auxiliary Space__: O(1)

</div>