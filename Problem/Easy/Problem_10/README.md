<div align="justify">

# Tail recursion to calculate sum of array elements

Given an array A[], we need to find the sum of its elements using Tail Recursion Method. We generally want to achieve tail recursion (a recursive function where recursive call is the last thing that function does) so that compilers can optimize the code. Basically, if recursive call is the last statement, the compiler does not need to save the state of parent call.

__Examples__

```
Input : A[] = {1, 8, 9}
Output : 18

Input : A[] = {2, 55, 1, 7}
Output : 65
```

For Linear Recursion Method, refer: https://www.geeksforgeeks.org/sum-array-elements-using-recursion/

Logic: Here the key to tail recursion is whatever operation is applied with the function call, maintain it as a separate function parameter. 

So, keep the sum of the last elements K elements as a function parameter and return sum when K=0.

</div>