<div align="justify">

# Reversing a queue using recursion

Given a queue, write a recursive function to reverse it.

### Standard operations allowed

- __enqueue(x)__: Add an item x to rear of queue. 
- __dequeue()__: Remove an item from front of queue. 
- __empty()__: Checks if a queue is empty or not.

### Examples

```
Input : Q = [5, 24, 9, 6, 8, 4, 1, 8, 3, 6]
Output : Q = [6, 3, 8, 1, 4, 8, 6, 9, 24, 5]

Explanation : Output queue is the reverse of the input queue.

Input : Q = [8, 7, 2, 5, 1]
Output : Q = [1, 5, 2, 7, 8]
```

### Recursive Algorithm

1. The pop element from the queue if the queue has elements otherwise return empty queue.
2. Call reverseQueue function for the remaining queue.
3. Push the popped element in the resultant reversed queue.

<div align="center">
<img src="https://media.geeksforgeeks.org/wp-content/uploads/Queue-reversal-using-recursion.jpg">
</div>

### Pseudo Code

```
queue reverseFunction(queue)
{
    if (queue is empty)
       return queue;
    else {
       data = queue.front()
       queue.pop()
       queue = reverseFunction(queue);
       q.push(data);
       return queue;
    }
}
```

### Complexity analysis

- __Time Complexity__: O(n). 
- __Auxiliary Space__: O(n), since recursion uses stack internally.

</div>