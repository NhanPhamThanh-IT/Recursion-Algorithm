<div align="justify">

# <div align="center">Why is Tail Recursion optimization faster than normal Recursion?</div>

## What is tail recursion?

Tail recursion is defined as a recursive function in which the recursive call is the last statement that is executed by the function. So basically nothing is left to execute after the recursion call.

## What is non-tail recursion?

Non-tail or head recursion is defined as a recursive function in which the recursive call is the first statement that is executed by the function. It means there is no statement or operation before the recursive calls.

## Why is tail recursion optimization faster than normal recursion?

In non-tail recursive functions, after one recursive call is over, there are more statements to compute, and hence all the functions do not unfold as soon as the base case is hit.

Every time when a recursive call is done (or any function call), a stack frame is added to the call stack. This keeps track of where you were at the time the function call was made so we can continue from where we left off. If this is done enough times, say through a recursive function to compute the 1 billionth Fibonacci number, you can get a stack overflow, which will typically terminate the process.

Tail recursion works off the realization that some recursive calls don’t need to “continue from where they left off” once the recursive call returns. Specifically, when the recursive call is the last statement that would be executed in the current context. Tail recursion is an optimization that doesn’t bother to push a stack frame onto the call stack in these cases, which allows your recursive calls to go very deep in the call stack.

> If the last action of a method is a call to another method, instead of creating a new stack frame for the context of the new method (arguments, local variables, etc.), we can replace the current one. One of the drawbacks of normal recursive methods is that they heavily use the call stack. Tail-call optimization eliminates this problem and guarantees that the performance of a recursive algorithm is exactly as good as its iterative counterpart (yet potentially it is much more readable).

__Example of tail recursive function__

```cpp
// C++ code to implement the above approach
#include <bits/stdc++.h>
using namespace std;
 
// Tail recursion
void fun(int n)
{
  if(n == 0)
    return;
 
  cout<<n<<" ";
  fun(n-1);
}
 
// Driver Code
int main()
{
 
  fun(5);
 
  return 0;
}
```

__Output__

```
5 4 3 2 1 
```

__Time Complexity__: O(N)

__Auxiliary Space__: O(N)

__Example of non-tail recursive function__

```cpp
#include <iostream>
using namespace std;
 
// Non-tail recursion
void fun(int n)
{
  if (n == 0)
    return;
 
  fun(n - 1);
 
  cout<<n<<" ";
}
 
int main() {
 
    fun(5);
    return 0;
}
```

__Output__

```
1 2 3 4 5 
```

__Time Complexity__: O(N)

__Auxiliary Space__: O(N)

</div>