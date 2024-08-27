<div align="justify">

# Program for Tower of Hanoi Algorithm

Tower of Hanoi is a mathematical puzzle where we have three rods (__A__, __B__, and __C__) and __N__ disks. Initially, all the disks are stacked in decreasing value of diameter i.e., the smallest disk is placed on the top and they are on rod __A__. The objective of the puzzle is to move the entire stack to another rod (here considered __C__), obeying the following simple rules:

- Only one disk can be moved at a time.
- Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack i.e. a disk can only be moved if it is the uppermost disk on a stack.
- No disk may be placed on top of a smaller disk.

### Examples

```
Input: 2
Output: Disk 1 moved from A to B
Disk 2 moved from A to C
Disk 1 moved from B to C

Input: 3
Output: Disk 1 moved from A to C
Disk 2 moved from A to B
Disk 1 moved from C to B
Disk 3 moved from A to C
Disk 1 moved from B to A
Disk 2 moved from B to C
Disk 1 moved from A to C
```

### Tower of Hanoi using Recursion

The idea is to use the helper node to reach the destination using recursion. Below is the pattern for this problem:

- Shift ‘N-1’ disks from ‘A’ to ‘B’, using C.
- Shift last disk from ‘A’ to ‘C’.
- Shift ‘N-1’ disks from ‘B’ to ‘C’, using A.

<div align="center">
<img src="https://media.geeksforgeeks.org/wp-content/uploads/tower-of-hanoi.png">
</div>

Follow the steps below to solve the problem:

- Create a function __towerOfHanoi__ where pass the __N__ (current number of disk), __from_rod__, __to_rod__, __aux_rod__.
- Make a function call for N – 1 th disk.
- Then print the current the disk along with __from_rod__ and __to_rod__
- Again make a function call for N – 1 th disk.

### Complexity Analysis

__Time complexity__: O(2^N), There are two possibilities for every disk. Therefore, 2 * 2 * 2 * . . . * 2(N times) is 2^N

__Auxiliary Space__: O(N), Function call stack space

# Time Complexity Analysis | Tower Of Hanoi (Recursion)

Tower of Hanoi is a mathematical puzzle where we have three rods and n disks. The objective of the puzzle is to move the entire stack to another rod, obeying the following simple rules:

1. Only one disk can be moved at a time. 
2. Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack i.e. a disk can only be moved if it is the uppermost disk on a stack. 
3. No disk may be placed on top of a smaller disk. 

### Algorithm

- Move the top n – 1 disks from Source to Auxiliary tower,
- Move the nth disk from Source to Destination tower,
- Move the n – 1 disks from Auxiliary tower to Destination tower.
- Transferring the top n – 1 disks from Source to auxiliary tower can again be thought of as a fresh problem and can be solved in the same manner. Once we solve Towers of Hanoi with three disks, we can solve it with any number of disks with the above algorithm. 

### Pseudo Code

```
TOH(n, x, y, z)
{
   if (n >= 1)
   {
      // put (n-1) disk to z by using y
      TOH((n-1), x, z, y)
   
       // move larger disk to right place
       move:x-->y
     
      // put (n-1) disk to right place 
      TOH((n-1), z, y, x)
   }
}
```

</div>