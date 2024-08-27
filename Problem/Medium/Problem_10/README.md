<div align="justify">

# Program to calculate value of nCr using Recursion

Given two numbers __N__ and __r__, find the value of __NCr__ using recursion

### Examples

```
Input: N = 5, r = 2
Output: 10
Explanation: The value of 5C2 is 10

Input: N = 3, r = 1
Output: 3
```

### Approach

__Approach 1__

One very interesting way to find the C(n,r) is the recursive method which is based on the recursive equation.

```
C(n,r) = C(n-1,r-1) + C(n-1,r)
```

__Time Complexity__: O(2^n)

__Auxiliary Space__: O(n)

__Approach 2__

Another idea is simply based on the below formula.

```
NCr = N! / (r! * (N-r)!)
Also, 
NCr-1 = N! / ( (r-1)! * (N – (r-1))! )

Hence:
    - NCr * r! * (N – r)! = NCr-1  * (r-1)! * (N – (r-1))!
    - NCr * r * (N-r)! = NCr-1  * (N-r+1)!                          [eliminating (r – 1)! from both side]
    - NCr * r = nCr-1  * (N-r+1)
```

Therefore:

```
NCr = NCr-1 * (N-r+1) / r
```

__Time Complexity__: O(r)

__Auxiliary Space__: O(r)

### Complexity Analysis

The time complexity of the above approach is O(r). This is because the function makes a single recursive call for each value of r, and the time taken to calculate the value of nCr is constant.

The Auxiliary space complexity of the above approach is O(r), as the recursive function calls create a new stack frame for each call. This means that the program will consume a significant amount of memory for larger values of r.

</div>