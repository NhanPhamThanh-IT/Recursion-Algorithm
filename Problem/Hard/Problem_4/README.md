<div align="justify">

# Print all Palindromic Partitions of a String using Backtracking

Given a string, find all possible palindromic partitions of given string.

Note that this problem is different from Palindrome Partitioning Problem, there the task was to find the partitioning with minimum cuts in input string. Here we need to print all possible partitions.

### Examples

```
Input: nitin
Output: n i t i n
n iti n
nitin

Input: geeks
Output: g e e k s
g ee k s
```

### Brute Force Approach

```
The idea is to use recursion and backtracking.
```

- Partition the string to generate the substrings.
- Check whether the substring generated is palindrome or not.
- If the substring generated is palindrome, then add this substring to our current list and recursively call the function for the remaining string.
- When the end of the string is reached the current list is added to the result.

### Complexity Analysis

__Time complexity__: O(n*2^n), where n is the size of the string. There are 2^n possibilities of partitioning the string of length n, and for each possibility, we are checking if the string is a palindrome that costs O(n) time. Hence the overall time complexity is O(n*2^n).

__Auxiliary Space__: O(2^n), to store all possible partition of string.

</div>