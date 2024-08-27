<div align="justify">

# Sort the Queue using Recursion

Given a queue and the task is to sort it using recursion without using any loop. We can only use the following functions of queue:

> __empty(q)__: Tests whether the queue is empty or not. 
> 
> __push(q)__: Adds a new element to the queue. 
>
> __pop(q)__: Removes front element from the queue. 
> 
> __size(q)__: Returns the number of elements in a queue. 
>
> __front(q)__: Returns the value of the front element without removing it. 

__Examples__

```
Input: queue = {10, 7, 16, 9, 20, 5} 
Output: 5 7 9 10 16 20

Input: queue = {0, -2, -1, 2, 3, 1} 
Output: -2 -1 0 1 2 3 
```

__Approach__: The idea of the solution is to hold all values in the function call stack until the queue becomes empty. When the queue becomes empty, insert all held items one by one in sorted order. Here sorted order is important.

### How to manage sorted order?

Whenever you get the item from the function call stack, then first calculate the size of the queue and compare it with the elements of queue. Here, two cases arises:

1. If the item (returned by function call stack) is greater than the front element of the queue then dequeue front element and enqueue this element into the same queue by decreasing the size.
2. If the item is less than the front element from the queue then enqueue the element in the queue and dequeue the remaining element from the queue and enqueue by decreasing size repeat the case 1 and 2 unless size becomes zero. Take care of one thing, if size became zero and your element remains greater than all elements of the queue then push your element into the queue.

__Time Complexity__: The time complexity of this code is O(n^2), as the time taken to sort the queue is O(n^2) due to the use of recursion. The function pushInQueue() is called n times, and each time it calls the function FrontToLast() which takes O(n) time, resulting in a time complexity of O(n^2).

__Auxiliary Space__:  The Auxiliary Space of this code is O(n), as the maximum size of the queue will be n, where n is the number of elements in the queue.

</div>