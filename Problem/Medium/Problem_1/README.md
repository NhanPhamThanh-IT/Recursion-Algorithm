<div align="justify">

# Recursively remove all adjacent duplicates

Given a string __S__, the task is to remove all its adjacent duplicate characters recursively.

__Examples__

```
Input: S = “geeksforgeek”
Output: “gksforgk”
Explanation: g(ee)ksforg(ee)k -> gksforgk

Input: S = “abccbccba”
Output: ““
Explanation: ab(cc)b(cc)ba->abbba->a(bbb)a->aa->(aa)->”” (empty string)
```

### Table Of Content

- __[Naive Approach]__ Using Recursion – O(N^2) Time and O(N) Space
- __[Expected Approach]__ Using Recursion – O(N^2) Time and O(N) Space

### [Naive Approach] Using Recursion – O(N^2) Time and O(N) Space

> The idea is to first iteratively build a new string in __result__ by removing adjacent duplicates. After one full pass, if the length of the string of __result__ remains as original string, returns the __result__. If changes were made (meaning some duplicates were removed), simply calls itself recursively on the newly formed string. This ensures that any new adjacent duplicates formed by the removal of previous ones are also eliminated. The idea is to gradually “peel off” the duplicates layer by layer until no adjacent duplicates are left.

__Time Complexity__: O(N^2), In the worst case, the function may need to iterate almost through the entire string for each recursion, which makes the time complexity as O(N^2).

__Auxiliary Space__:O(N), As we are making a new string at every iteration.

### [Expected Approach] Using Recursion – O(N2) Time and O(N) Space

> This solution also removes adjacent duplicates but it does this by modifying the string in place. It uses an index to track where to place non-duplicate characters. It skips over duplicate characters and moves only unique characters forward. After processing the original string, trims the original string to remove extra characters. If any adjacent duplicates were removed in this process then recursively call the function itself to repeat this process again. This approach is efficient because it modifies the string directly without creating new ones.

__Time Complexity__: O(N^2), In the worst case, the function may need to iterate almost through the entire string for each recursion, which makes the time complexity as O(N^2).

__Auxiliary Space__: O(N), As the size of the recursive call stack can be N/2 in the worst case if we have the input like this abccba.

</div>