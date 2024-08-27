<div align="justify">

# Reverse a Doubly linked list using recursion

Given a doubly linked list. Reverse it using recursion.

__Original Doubly linked list__

<div align="center">
<img src="https://media.geeksforgeeks.org/wp-content/uploads/1-25.jpg">
</div>

__Reversed Doubly linked list__

<div align="center">
<img src="https://media.geeksforgeeks.org/wp-content/uploads/2-23.jpg">
</div>

### Algorithm

1. If list is empty, return 
2. Reverse head by swapping head->prev and head->next 
3. If prev = NULL it means that list is fully reversed. Else reverse(head->prev) 

### Complexity Analysis

__Time Complexity__: O(N), where N is the number of nodes in given doubly linked list.

__Auxiliary Space__: O(N), due to recursion call stack.

</div>