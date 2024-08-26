<div align="justify">

# <div align="center">Types Of Recursions</div>

## What is Recursion?

The process in which a function calls itself directly or indirectly is called recursion and the corresponding function is called a recursive function. Using recursive algorithm, certain problems can be solved quite easily. Examples of such problems are Towers of Hanoi (TOH), Inorder/Preorder/Postorder Tree Traversals, DFS of Graph, etc.

## Types of Recursions

Recursion are mainly of two types depending on whether a function calls itself from within itself or more than one function call one another mutually. The first one is called direct recursion and another one is called indirect recursion. Thus, the two types of recursion are:

### 1. Direct Recursion

These can be further categorized into four types:

- __Tail Recursion__: If a recursive function calling itself and that recursive call is the last statement in the function then it’s known as __Tail Recursion__. After that call the recursive function performs nothing. The function has to process or perform any operation at the time of calling and it does nothing at returning time.

__Example__

```cpp
// Code Showing Tail Recursion 
#include <iostream> 
using namespace std; 
  
// Recursion function 
void fun(int n) 
{ 
    if (n > 0) { 
        cout << n << " "; 
  
        // Last statement in the function 
        fun(n - 1); 
    } 
} 
  
// Driver Code 
int main() 
{ 
    int x = 3; 
    fun(x); 
    return 0; 
}
```

__Output__

```
3 2 1 
```

Let’s understand the example by __tracing tree of recursive function__. That is how the calls are made and how the outputs are produced.

<div align="center">
<img src="https://github.com/NhanPhamThanh-IT/Recursion-Algorithm/blob/main/LectureMaterials/TypesOfRecursions/Image/Tail1.jpg">
</div>

__Time Complexity For Tail Recursion__: O(n) 

__Space Complexity For Tail Recursion__: O(n)

</div>

> [!NOTE]
> Time & Space Complexity is given for this specific example. It may vary for another example.

<div align="justify">

Let’s now converting Tail Recursion into Loop and compare each other in terms of Time & Space Complexity and decide which is more efficient.

```cpp
// Converting Tail Recursion into Loop 
#include <iostream> 
using namespace std; 
  
void fun(int y) 
{ 
    while (y > 0) { 
        cout << y << " "; 
        y--; 
    } 
} 
  
// Driver code 
int main() 
{ 
    int x = 3; 
    fun(x); 
    return 0; 
}
```

__Output__

```
3 2 1 
```

__Time Complexity__: O(n) 

__Space Complexity__: O(1)

</div>

> [!NOTE]
> Time & Space Complexity is given for this specific example. It may vary for another example.
So it was seen that in case of loop the Space Complexity is O(1) so it was better to write code in loop instead of tail recursion in terms of Space Complexity which is more efficient than tail recursion.

<div align="justify">

### Why space complexity is less in case of loop?

Before explaining this I am assuming that you are familiar with the knowledge that’s how the data stored in main memory during execution of a program. In brief,when the program executes,the main memory divided into three parts. One part for code section, the second one is heap memory and another one is stack memory. __Remember that the program can directly access only the stack memory, it can’t directly access the heap memory so we need the help of pointer to access the heap memory.__

Let’s now understand why space complexity is less in case of loop ?

In case of loop when function “(void fun(int y))” executes there only one activation record created in stack memory(activation record created for only ‘y’ variable) so it takes only ‘one’ unit of memory inside stack so it’s space complexity is O(1) but in case of recursive function every time it calls itself for each call a separate activation record created in stack.So if there’s ‘n’ no of call then it takes ‘n’ unit of memory inside stack so it’s space complexity is O(n). 

- __Head Recursion__: If a recursive function calling itself and that recursive call is the first statement in the function then it’s known as __Head Recursion__. There’s no statement, no operation before the call. The function doesn’t have to process or perform any operation at the time of calling and all operations are done at returning time.

__Example__

```cpp
// C++ program showing Head Recursion 
  
#include <bits/stdc++.h> 
using namespace std; 
  
// Recursive function 
void fun(int n) 
{ 
    if (n > 0) { 
  
        // First statement in the function 
        fun(n - 1); 
  
        cout << " "<< n; 
    } 
} 
  
// Driver code 
int main() 
{ 
    int x = 3; 
    fun(x); 
    return 0; 
}
```

__Output__

Let’s understand the example by __tracing tree of recursive function__. That is how the calls are made and how the outputs are produced.

<div align="center">
<img src="https://github.com/NhanPhamThanh-IT/Recursion-Algorithm/blob/main/LectureMaterials/TypesOfRecursions/Image/Head3.jpg">
</div>

__Time Complexity For Head Recursion__: O(n)

__Space Complexity For Head Recursion__: O(n)

```cpp
// Converting Head Recursion into Loop 
#include <iostream> 
using namespace std; 
  
// Recursive function 
void fun(int n) 
{ 
    int i = 1; 
    while (i <= n) { 
        cout <<" "<< i; 
        i++; 
    } 
} 
  
// Driver code 
int main() 
{ 
    int x = 3; 
    fun(x); 
    return 0; 
}
```

__Output__

- __Tree Recursion__: To understand __Tree Recursion__ let’s first understand __Linear Recursion__. If a recursive function calling itself for one time then it’s known as __Linear Recursion__. Otherwise if a recursive function calling itself for more than one time then it’s known as __Tree Recursion__.

__Pseudo Code for linear recursion__

```
fun(n)
{
    // some code
    if(n>0)
    {
        fun(n-1); // Calling itself only once
    }
    // some code
}
```

__Program for tree recursion__

```cpp
// C++ program to show Tree Recursion 
#include <iostream> 
using namespace std; 
  
// Recursive function 
void fun(int n) 
{ 
    if (n > 0)  
    { 
        cout << " " << n; 
          
        // Calling once 
        fun(n - 1); 
          
        // Calling twice 
        fun(n - 1); 
    } 
} 
  
// Driver code 
int main() 
{ 
    fun(3); 
    return 0; 
}
```

__Output__

```
3 2 1 1 2 1 1
```

Let’s understand the example by __tracing tree of recursive function__. That is how the calls are made and how the outputs are produced.

<div align="center">
<img src="https://github.com/NhanPhamThanh-IT/Recursion-Algorithm/blob/main/LectureMaterials/TypesOfRecursions/Image/Tree4.jpg">
</div>

__Time Complexity For Tree Recursion__: O(2^n)

__Space Complexity For Tree Recursion__: O(n)

</div>

> [!NOTE]
> Time & Space Complexity is given for this specific example. It may vary for another example.

<div align="justify">

- __Nested Recursion__: In this recursion, a recursive function will pass the parameter as a recursive call. That means __“recursion inside recursion”__. Let see the example to understand this recursion.

__Example__

```cpp
// C++ program to show Nested Recursion 
#include <iostream> 
using namespace std; 
  
int fun(int n) 
{ 
    if (n > 100) 
        return n - 10; 
  
    // A recursive function passing parameter 
    // as a recursive call or recursion inside  
    // the recursion 
    return fun(fun(n + 11)); 
} 
  
// Driver code 
int main() 
{ 
    int r; 
    r = fun(95); 
    
    cout << " " << r; 
    
    return 0; 
}
```

__Output__

```
91
```

Let’s understand the example by __tracing tree of recursive function__. That is how the calls are made and how the outputs are produced.

<div align="center">
<img src="https://github.com/NhanPhamThanh-IT/Recursion-Algorithm/blob/main/LectureMaterials/TypesOfRecursions/Image/Nested2.jpg">
</div>

### 2. Indirect Recursion

In this recursion, there may be more than one functions and they are calling one another in a circular manner.

<div align="center">
<img src="">
</div>

From the above diagram fun(A) is calling for fun(B), fun(B) is calling for fun(C) and fun(C) is calling for fun(A) and thus it makes a cycle.

```cpp
// C++ program to show Indirect Recursion 
#include <iostream> 
using namespace std; 
  
void funB(int n); 
  
void funA(int n) 
{ 
    if (n > 0) { 
        cout <<" "<< n; 
  
        // fun(A) is calling fun(B) 
        funB(n - 1); 
    } 
} 
  
void funB(int n) 
{ 
    if (n > 1) { 
        cout <<" "<< n; 
  
        // fun(B) is calling fun(A) 
        funA(n / 2); 
    } 
} 
  
// Driver code 
int main() 
{ 
    funA(20); 
    return 0; 
}
```

__Output__

```
20 19 9 8 4 3 1
```

Let’s understand the example by __tracing tree of recursive function__. That is how the calls are made and how the outputs are produced.

<div align="center">
<img src="">
</div>

</div>
