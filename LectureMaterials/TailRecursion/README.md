<div align="justify">

# <div align="center">What is Tail Recursion</div>

> __Tail recursion__ is defined as a recursive function in which the recursive call is the last statement that is executed by the function. So basically nothing is left to execute after the recursion call.

For example the following C++ function print() is tail recursive.

```cpp
// An example of tail recursive function
 
static void print(int n)
{
    if (n < 0)
        return;
    cout << " " << n;
  
    // The last executed statement is recursive call
    print(n - 1);
}
```

__Time Complexity__: O(n)

__Auxiliary Space__: O(n)

## Need for Tail Recursion

The tail recursive functions are considered better than non-tail recursive functions as tail-recursion can be optimized by the compiler. 

Compilers usually execute recursive procedures by using a __stack__. This stack consists of all the pertinent information, including the parameter values, for each recursive call. When a procedure is called, its information is __pushed__ onto a stack, and when the function terminates the information is __popped__ out of the stack. Thus for the non-tail-recursive functions, the __stack depth__ (maximum amount of stack space used at any time during compilation) is more. 

> The idea used by compilers to optimize tail-recursive functions is simple, since the recursive call is the last statement, there is nothing left to do in the current function, so saving the current function’s stack frame is of no use.

## Can a non-tail-recursive function be written as tail-recursive to optimize it?

Consider the following function to calculate the factorial of n.

It is a non-tail-recursive function. Although it looks like a tail recursive at first look. If we take a closer look, we can see that the value returned by fact(n-1) is used in __fact(n)__. So the call to __fact(n-1)__ is not the last thing done by __fact(n)__.

```cpp
#include <iostream>
using namespace std;
 
// A NON-tail-recursive function.  The function is not tail
// recursive because the value returned by fact(n-1) is used
// in fact(n) and call to fact(n-1) is not the last thing
// done by fact(n)
unsigned int fact(unsigned int n)
{
    if (n <= 0)
        return 1;
 
    return n * fact(n - 1);
}
 
// Driver program to test above function
int main()
{
    cout << fact(5);
    return 0;
}
```

__Output__

```
120
```

__Time Complexity__: O(n)

__Auxiliary Space__: O(n)

The above function can be written as a tail-recursive function. The idea is to use one more argument and accumulate the factorial value in the second argument. When n reaches 0, return the accumulated value.

Below is the implementation using a tail-recursive function.

```cpp
#include <iostream>
using namespace std;
 
// A tail recursive function to calculate factorial
unsigned factTR(unsigned int n, unsigned int a)
{
    if (n <= 1)
        return a;
 
    return factTR(n - 1, n * a);
}
 
// A wrapper over factTR
unsigned int fact(unsigned int n) { return factTR(n, 1); }
 
// Driver program to test above function
int main()
{
    cout << fact(5);
    return 0;
}
```

__Output__

```
120
```

__Time Complexity__: O(n)

__Auxiliary Space__: O(1)

</div>