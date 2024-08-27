# Python3 program to recursively delete a linked list
import math
 
# Link list node 
class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None
 
# Recursive Function to delete the entire linked list 
def deleteList(head):
    if (head == None):
        return
    deleteList(head.next) 
    # free(head)
 
# Given a reference (pointer to pointer) to the head of a list and an int, head=push a new node on the front of the list. 
def push(head_ref, new_data):
    new_node = Node(new_data)
    new_node.data = new_data
    new_node.next = head_ref
    head_ref = new_node
    return head_ref
 
# Driver Code
if __name__=='__main__':
     
    # Start with the empty list 
    head = None
 
    # Use head=push() to construct below list 1.12.1.4.1 
    head = push(head, 1)
    head = push(head, 4)
    head = push(head, 1)
    head = push(head, 12)
    head = push(head, 1)
    print("Deleting linked list")
    deleteList(head)
    print("Linked list deleted")