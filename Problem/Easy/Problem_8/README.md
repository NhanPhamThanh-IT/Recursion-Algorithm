<div align="justify">

# Program for length of a string using recursion

Given a string calculate length of the string using recursion. 

__Examples__

```
Input : str = "abcd"
Output :4

Input : str = "GEEKSFORGEEKS"
Output :13
```

__Algorithm__

```
recLen(str)
{
    If str is NULL 
        return 0
    Else 
        return 1 + recLen(str + 1)
}
```

</div>