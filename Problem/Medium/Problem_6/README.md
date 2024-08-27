<div align="justify">

# Product of 2 Numbers using Recursion

Given two numbers x and y find the product using recursion.

### Examples

```
Input : x = 5, y = 2
Output : 10

Input : x = 100, y = 5
Output : 500
```

### Method

1. If x is less than y, swap the two variables value 
2. Recursively find y times the sum of x 
3. If any of them become zero, return 0 

### Complexity Analysis

__Time Complexity__: O(min(x,y))

__Auxiliary Space__: O(min(x,y)), The extra space is used in the recursive call stack.

</div>