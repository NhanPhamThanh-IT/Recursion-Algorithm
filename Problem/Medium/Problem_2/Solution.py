# defining a class Queue
class Queue:
 
    def __init__(self):
        self.queue = []
 
    def put(self, item):
        self.queue.append(item)
 
    def get(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)
         
    def front(self):
        return self.queue[0]
 
    def size(self):
        return len(self.queue) 
         
    def empty(self):
        return not(len(self.queue))
 
# Function to push element in last by popping from front until size becomes 0 
def FrontToLast(q, qsize) : 
 
    # Base condition 
    if qsize <= 0: 
        return
 
    # pop front element and push this last in a queue 
    q.put(q.get()) 
 
    # Recursive call for pushing element 
    FrontToLast(q, qsize - 1) 
 
# Function to push an element in the queue while maintaining the sorted order 
def pushInQueue(q, temp, qsize) :
     
    # Base condition 
    if q.empty() or qsize == 0: 
        q.put(temp)
        return
     
    # If current element is less than the element at the front 
    elif temp <= q.front() : 
 
        # Call stack with front of queue
        q.put(temp) 
 
        # Recursive call for inserting a front element of the queue to the last 
        FrontToLast(q, qsize) 
 
    else : 
 
        # Push front element into last in a queue 
        q.put(q.get()) 
 
        # Recursive call for pushing element in a queue 
        pushInQueue(q, temp, qsize - 1) 
     
# Function to sort the given queue using recursion 
def sortQueue(q):
     
    # Return if queue is empty 
    if q.empty(): 
        return
 
    # Get the front element which will be stored in this variable throughout the recursion stack 
    temp = q.get()
     
    # Recursive call 
    sortQueue(q) 
 
    # Push the current element into the queue according to the sorting order 
    pushInQueue(q, temp, q.size())
 
# Driver code
qu = Queue()
 
# Data is inserted into Queue using put() Data is inserted at the end 
qu.put(10) 
qu.put(7) 
qu.put(16) 
qu.put(9) 
qu.put(20) 
qu.put(5)
 
# Sort the queue 
sortQueue(qu)
 
# Print the elements of the queue after sorting 
while not qu.empty(): 
    print(qu.get(), end = ' ')