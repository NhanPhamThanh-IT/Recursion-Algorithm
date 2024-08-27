<div align="justify">

# Print all Palindromic Partitions of a String using Bit Manipulation

Given a string, find all possible palindromic partitions of a given string.

Note that this problem is different from Palindrome Partitioning Problem, there the task was to find the partitioning with minimum cuts in input string. Here we need to print all possible partitions.

__Example__

```
Input: nitin
Output: n i t i n
n iti n
nitin

Input: geeks
Output: g e e k s
g ee k s
```

### Print all Palindromic Partitions Using Bit Manipulation

The idea is to consider the space between two characters in the string.

- If there n characters in the string, then there are n-1 positions to put a space or say cut the string.
- Each of these positions can be given a binary number 1 (If a cut is made in this position) or 0 (If no cut is made in this position).
- This will give a total of 2n-1 partitions and for each partition check whether this partition is palindrome or not.

__Illustration__

```
Input : geeks

0100 => ["ge","eks"] (not valid)
1011 => ["g","ee","k","s"] (valid)
1111 => ["g","e","e","k","s"] (valid)
0000 => ["geeks"] (not valid)
```

__Complexity Analysis__

__Time complexity__: O(n*2^n), n is size of the string.

__Auxiliary Space__: O(2^n), to store all possible partition of string.

</div>