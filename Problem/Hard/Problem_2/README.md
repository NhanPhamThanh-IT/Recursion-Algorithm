<div align="justify">

# How to Sort a Stack using Recursion

Given a __stack__, the task is to sort it using recursion.

__Examples__

```
Input: elements present in stack from top to bottom -3 14 18 -5 30
Output: 30 18 14 -3 -5
Explanation: The given stack is sorted know 30 > 18 > 14 > -3 > -5

Input: elements present in stack from top to bottom 1 2 3
Output: 3 2 1
Explanation: The given stack is sorted know 3 > 2 > 1
```

## How to Sort a Stack Using Stack

> The idea of the solution is to hold all values in Function Call Stack until the stack becomes empty. When the stack becomes empty, insert all held items one by one in sorted order. and then print the stack

### Illustration

Below is the illustration of above approach

Let given stack be

<table border="1" align="center">
    <tr align="center">
        <td>-3</td>
    </tr>
    <tr align="center">
        <td>14</td>
    </tr>
    <tr align="center">
        <td>18</td>
    </tr>
    <tr align="center">
        <td>-5</td>
    </tr>
    <tr align="center">
        <td>30</td>
    </tr>
</table>

Let us illustrate sorting of stack using the above example:

__Step 1__: First pop all the elements from the stack and store popped element in the variable ‘temp’. After popping all the elements function’s stack frame will look like this:

<table border="1" align="center">
    <tr align="center">
        <td>-3</td>
        <td>stack frame 1</td>
    </tr>
    <tr align="center">
        <td>14</td>
        <td>stack frame 2</td>
    </tr>
    <tr align="center">
        <td>18</td>
        <td>stack frame 3</td>
    </tr>
    <tr align="center">
        <td>-5</td>
        <td>stack frame 4</td>
    </tr>
    <tr align="center">
        <td>30</td>
        <td>stack frame 5</td>
    </tr>
</table>

__Step 2__: Now stack is empty so function insert in sorted order is called and it inserts 30 (from stack frame 5) at the bottom of the stack. Now stack looks like the below:

<table border="1" align="center">
    <tr align="center">
        <td>30</td>
    </tr>
</table>

__Step 3__: Now next element  -5 (from stack frame 4) is picked. Since -5 < 30, -5 is inserted at the bottom of the stack. Now stack becomes:

<table border="1" align="center">
    <tr align="center">
        <td>30</td>
    </tr>
    <tr align="center">
        <td>-5</td>
    </tr>
</table>

__Step 4__: Next 18 (from stack frame 3) is picked. Since 18 < 30, 18 is inserted below 30. Now stack becomes:

<table border="1" align="center">
    <tr align="center">
        <td>30</td>
    </tr>
    <tr align="center">
        <td>18</td>
    </tr>
    <tr align="center">
        <td>-5</td>
    </tr>
</table>

__Step 5__: Next 14 (from stack frame 2) is picked. Since 14 < 30 and 14 < 18, it is inserted below 18. Now stack becomes:

<table border="1" align="center">
    <tr align="center">
        <td>30</td>
    </tr>
    <tr align="center">
        <td>18</td>
    </tr>
    <tr align="center">
        <td>14</td>
    </tr>
    <tr align="center">
        <td>-5</td>
    </tr>
</table>

__Step 6__: Now -3 (from stack frame 1) is picked, as -3 < 30 and -3 < 18 and -3 < 14, it is inserted below 14. Now stack becomes:

<table border="1" align="center">
    <tr align="center">
        <td>30</td>
    </tr>
    <tr align="center">
        <td>18</td>
    </tr>
    <tr align="center">
        <td>14</td>
    </tr>
    <tr align="center">
        <td>-3</td>
    </tr>
    <tr align="center">
        <td>-5</td>
    </tr>
</table>

Follow the steps mentioned below to implement the idea:

- Create a __stack__ and push all the elements in it.
- Call __sortStack()__, which will pop an element from the stack and pass the popped element to function __sortInserted()__, then it will keep calling itself until the stack is __empty__.
- Whenever __sortInserted()__ is called it will insert the passed element in stack in sorted order.
- Print the __stack__

### Complexity Analysis

__Time Complexity__: O(N2). 

__Auxiliary Space__: O(N) use of Stack

</div>