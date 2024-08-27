<div align="justify">

# Length of longest palindromic sub-string using recursion

Given a string __S__, the task is to find the length longest sub-string which is a palindrome

__Examples__

```
Input: S = “aaaabbaa” 
Output: 6 
Explanation: 
Sub-string “aabbaa” is the longest palindromic sub-string.

Input: S = “banana” 
Output: 5 
Explanation: 
Sub-string “anana” is the longest palindromic sub-string.
```

### Approach

The idea is to use recursion to break the problem into smaller sub-problems. In order to break the problem into two smaller sub-problems, Compare the start and end characters of the string and recursively call the function for the middle substring. Below is the illustration of the recursion:

- __Base Case__: The base case for this problem is when the starting index of the string is greater than or equal to the ending index.

```
if (start > end)
    return count
if (start == end)
    return count + 1
```

- __Recursive Case__: Compare the characters at the start and end index of the string. When starting and ending characters are equal, then recursively call for the substring by excluding the starting and ending characters.

```
recursive_func(string, start+1, end-1)
```

- When starting and ending characters are not equal, then recursively call for the substring by excluding the starting and ending characters one at a time.

```
recursive_func(string, start+1, end)
recursive_func(string, start, end-1)
```

- __Return statement__: At each recursive call, return the maximum count possible by including and excluding the start and end characters.

### Complexity Analysis

__Time Complexity__: The time complexity of this code is __O(n^2)__ as there are two recursive calls in each iteration and the loop iterates over all characters of the string.

__Auxiliary Space__: The space complexity is __O(n)__ as the recursive function calls consume space on the call stack.

</div>