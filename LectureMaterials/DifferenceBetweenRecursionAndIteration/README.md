<div align="justify">

# <div align="center">Difference Between Recursion And Iteration</div>

A program is called recursive when an entity calls itself. A program is called iterative when there is a loop (or repetition).

__Example__: Program to find the factorial of a number.

### C

```c
// C program to find factorial of given number
#include <stdio.h>
 
// ----- Recursion -----
// method to find factorial of given number
int factorialUsingRecursion(int n)
{
    if (n == 0)
        return 1;
 
    // recursion call
    return n * factorialUsingRecursion(n - 1);
}
 
// ----- Iteration -----
// Method to find the factorial of a given number
int factorialUsingIteration(int n)
{
    int res = 1, i;
 
    // using iteration
    for (i = 2; i <= n; i++)
        res *= i;
 
    return res;
}
 
// Driver method
int main()
{
    int num = 5;
    printf("Factorial of %d using Recursion is: %d\n", num,
           factorialUsingRecursion(5));
 
    printf("Factorial of %d using Iteration is: %d", num,
           factorialUsingIteration(5));
 
    return 0;
}
```

### Python3

```py
# Python3 program to find factorial of given number
 
# ----- Recursion -----
# method to find factorial of given number
def factorialUsingRecursion(n):
    if (n == 0):
        return 1;
 
    # recursion call
    return n * factorialUsingRecursion(n - 1);
 
# ----- Iteration -----
# Method to find the factorial of a given number
def factorialUsingIteration(n):
    res = 1;
 
    # using iteration
    for i in range(2, n + 1):
        res *= i;
 
    return res;
 
# Driver method
num = 5;
print("Factorial of",num,"using Recursion is:",
                    factorialUsingRecursion(5));
 
print("Factorial of",num,"using Iteration is:",
                    factorialUsingIteration(5));
```

### Java

```java
// Java program to find factorial of given number
class NhanPham {
 
    // ----- Recursion -----
    // method to find factorial of given number
    static int factorialUsingRecursion(int n)
    {
        if (n == 0)
            return 1;
 
        // recursion call
        return n * factorialUsingRecursion(n - 1);
    }
 
    // ----- Iteration -----
    // Method to find the factorial of a given number
    static int factorialUsingIteration(int n)
    {
        int res = 1, i;
 
        // using iteration
        for (i = 2; i <= n; i++)
            res *= i;
 
        return res;
    }
 
    // Driver method
    public static void main(String[] args)
    {
        int num = 5;
        System.out.println("Factorial of " + num
                           + " using Recursion is: "
                           + factorialUsingRecursion(5));
 
        System.out.println("Factorial of " + num
                           + " using Iteration is: "
                           + factorialUsingIteration(5));
    }
}
```

__Output__

```
Factorial of 5 using Recursion is: 120
Factorial of 5 using Iteration is: 120
```

__Time and Space Complexity__

```
Time Complexity: O(2^n)
Auxiliary Space: O(n)
```

Below is a detailed explanation to illustrate the difference between the two using the above example. We will study the different aspects of both recursive and iterative approaches.

## 1. Time Complexity

The time complexity of the method may vary depending on whether the algorithm is implemented using recursion or iteration.

- __Recursion__: The time complexity of recursion can be found by finding the value of the nth recursive call in terms of the previous calls. Thus, finding the destination case in terms of the base case, and solving in terms of the base case gives us an idea of the time complexity of recursive equations.
- __Iteration__: The time complexity of iteration can be found by finding the number of cycles being repeated inside the loop. 

## 2. Usage

Usage of either of these techniques is a trade-off between time complexity and size of code. If time complexity is the point of focus, and the number of recursive calls would be large, it is better to use iteration. However, if time complexity is not an issue and shortness of code is, recursion would be the way to go.

- __Recursion__: Recursion involves calling the same function again, and hence, has a very small length of code. However, as we saw in the analysis, the time complexity of recursion can get to be exponential when there are a considerable number of recursive calls. Hence, usage of recursion is advantageous in shorter code, but higher time complexity.
- __Iteration__: Iteration is the repetition of a block of code. This involves a larger size of code, but the time complexity is generally lesser than it is for recursion. 

## 3. Overhead

Recursion has a large amount of Overhead as compared to Iteration. 

- __Recursion__: Recursion has the overhead of repeated function calls, that is due to the repetitive calling of the same function, the time complexity of the code increases manyfold.
- __Iteration__: Iteration does not involve any such overhead

## 4. Infinite Repetition

Infinite Repetition in recursion can lead to a CPU crash but in iteration, it will stop when memory is exhausted. 

- __Recursion__: In Recursion, Infinite recursive calls may occur due to some mistake in specifying the base condition, which on never becoming false, keeps calling the function, which may lead to a system CPU crash.
- __Iteration__: Infinite iteration due to a mistake in iterator assignment or increment, or in the terminating condition, will lead to infinite loops, which may or may not lead to system errors, but will surely stop program execution any further.

## Difference between Iteration and Recursion

The following table lists the major differences between iteration and recursion:

<table>
  <thead>
    <tr align="center">
      <th>Property</th>
      <th>Recursion</th>
      <th>Iteration</th>
    </tr>
  </thead>
  <tbody>
    <tr align="justify">
      <td align="center"><strong>Definition</strong></td>
      <td>Function calls itself.</td>
      <td>A set of instructions repeatedly executed.</td>
    </tr>
    <tr align="justify">
      <td align="center"><strong>Application</strong></td>
      <td>For functions.</td>
      <td>For loops.</td>
    </tr>
    <tr align="justify">
      <td align="center"><strong>Termination</strong></td>
      <td>Through base case, where there will be no function call.</td>
      <td>When the termination condition for the iterator ceases to be satisfied.</td>
    </tr>
    <tr align="justify">
      <td align="center"><strong>Usage</strong></td>
      <td>Used when code size needs to be small, and time complexity is not an issue.</td>
      <td>Used when time complexity needs to be balanced against an expanded code size.</td>
    </tr>
    <tr align="justify">
      <td align="center"><strong>Code Size</strong></td>
      <td>Smaller code size.</td>
      <td>Larger code size.</td>
    </tr>
    <tr align="justify">
      <td align="center"><strong>Time Complexity</strong></td>
      <td>Very high (generally exponential) time complexity.</td>
      <td>Relatively lower time complexity (generally polynomial-logarithmic).</td>
    </tr>
    <tr align="justify">
      <td align="center"><strong>Space Complexity</strong></td>
      <td>The space complexity is higher than iterations.</td>
      <td>Space complexity is lower.</td>
    </tr>
    <tr align="justify">
      <td align="center"><strong>Stack</strong></td>
      <td>The stack is used to store local variables when the function is called.</td>
      <td>Stack is not used.</td>
    </tr>
    <tr align="justify">
      <td align="center"><strong>Speed</strong></td>
      <td>Execution is slow since it has the overhead of maintaining and updating the stack.</td>
      <td>Normally, it is faster than recursion as it doesn’t utilize the stack.</td>
    </tr>
    <tr align="justify">
      <td align="center"><strong>Memory</strong></td>
      <td>Recursion uses more memory compared to iteration.</td>
      <td>Iteration uses less memory compared to recursion.</td>
    </tr>
    <tr align="justify">
      <td align="center"><strong>Overhead</strong></td>
      <td>Possesses overhead of repeated function calls.</td>
      <td>No overhead as there are no function calls in iteration.</td>
    </tr>
    <tr align="justify">
      <td align="center"><strong>Infinite Repetition</strong></td>
      <td>If the recursive function does not meet a termination condition or the base case is not defined or never reached, it leads to a stack overflow error, potentially crashing the system in infinite recursion.</td>
      <td>If the control condition of the iteration statement never becomes false or the control variable does not reach the termination value, it will cause an infinite loop. On infinite loop, it uses CPU cycles repeatedly.</td>
    </tr>
  </tbody>
</table>

</div>