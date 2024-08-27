<div align="justify">

# Word Break

Given an input string and a dictionary of words, find out if the input string can be segmented into a space-separated sequence of dictionary words. See following examples for more details. 
This is a famous Google interview question, also being asked by many other companies now a days.

```
Consider the following dictionary
{ i, like, sam, sung, samsung, mobile, ice, cream, icecream, man, go, mango}
Input: ilike
Output: Yes
The string can be segmented as “i like”.

Input: ilikesamsung
Output: Yes
The string can be segmented as “i like samsung” or “i like sam sung”.
```

### Recursive implementation

The idea is simple, we consider each prefix and search for it in dictionary. If the prefix is present in dictionary, we recur for rest of the string (or suffix). If the recursive call for suffix returns true, we return true, otherwise we try next prefix. If we have tried all prefixes and none of them resulted in a solution, we return false.

### Dynamic Programming

Why Dynamic Programming? The above problem exhibits overlapping sub-problems. For example, see the following partial recursion tree for string “abcde” in the worst case.

<div align="center">
<img src="https://media.geeksforgeeks.org/wp-content/cdn-uploads/wordBreak1.png">
</div>

__Time complexity__: O(n^3 + dict_len), where n is the length of the input string. We create a dictionary in a hash set.

__Auxiliary Space__: O(n + dict_len).

### Optimized Dynamic Programming

In this approach, apart from the dp table, we also maintain all the prefix lengths which have already matched. We store this in an array matched_len[]. For the current prefix length to be checked, we consider only those prefixes which have already matched using matched_len[]. This way we avoid unnecessary iterations and string comparisons.

</div>