<div align="justify">

# <div align="center">What is Implicit recursion?</div>

## What is Recursion?

__Recursion__ is a programming approach where a function repeats an action by calling itself, either __directly__ or __indirectly__. This enables the function to continue performing the action until a particular condition is __satisfied__, such as when a particular value is reached or another condition is met.

## What is Implicit Recursion?

A specific sort of recursion called __implicit recursion__ occurs when a function calls itself without making an explicit recursive call. This can occur when a function calls another function, which then calls the original code once again and starts a recursive execution of the original function. This can sometimes be difficult to spot and can lead to unintended behavior if not handled carefully.

### Example of the implicit recursion

We will use implicit recursion to find the second-largest elements from the array.

```cpp
#include <bits/stdc++.h>
 
using namespace std;
 
int findLargest(vector<int> numbers) {
  int largest = numbers[0];
  for (int number : numbers) {
    if (number > largest) {
      largest = number;
    }
  }
  return largest;
}
 
int findSecondLargest(vector<int> numbers) {
  // Remove the largest number from the list
  numbers.erase(remove(numbers.begin(), numbers.end(), findLargest(numbers)), numbers.end());
 
  // Return the largest remaining number
  return findLargest(numbers);
}
 
int main() {
  vector<int> numbers = {1, 2, 3, 4, 5};
 
  // Function call
  int secondLargest = findSecondLargest(numbers);
  cout << secondLargest << endl;
 
  return 0;
}
```

__Output__

```
4
```

__Time Complexity__: O(N)

__Auxiliary Space__: O(1)

In this case, the __find_second_largest__( It’s crucial to __remember that explicit recursion could also be used to accomplish this example, which would make the code simpler to read and comprehend.)__ method calls the __find_largest()__ function via implicit recursion to locate the second-largest number in a provided list of numbers. Implicit recursion can be used in this way to get the second-largest integer without having to write any more code, which is a handy use.

## Problem with implicit recursion

In the case of the implicit recursion, the issue of an infinite function call may occur. Here is a case where implicit recursion can cause the problem:

```cpp
#include <iostream>
 
using namespace std;
 
void func2();
void func1();
 
void func1() {
  cout << "This is the first function" << endl;
  func2();
}
 
void func2() {
  cout << "This is the second function" << endl;
  func1();
}
 
int main() {
  func1();
 
  return 0;
}
```

__Output__

```
This is the first function
This is the second function
This is the first function
This is the second function
...
...
```

In this example, the func1() function calls func2(), which then calls func1() once again.

## Steps to avoid this issue

- When utilizing implicit recursion, caution must be taken since if the recursive calls are not handled correctly, it is simple to produce an __endless loop__. 
- Additionally, it’s typically recommended to avoid implicit recursion if feasible because it might make your code more challenging to read and maintain. 
- Instead, explicit recursion, which is simpler to read and understand, is typically preferred.

</div>