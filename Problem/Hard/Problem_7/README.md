<div align="justify">

# N Queen Problem

### What is N-Queen problem?

<div align="center">
<img src="https://media.geeksforgeeks.org/wp-content/uploads/20230814111624/N-Queen-Problem.png">
</div>

The __N__ Queen is the problem of placing __N__ chess queens on an __N×N__ chessboard so that no two queens attack each other.

For example, the following is a solution for the 4 Queen problem.

<div align="center">
<img src="https://media.geeksforgeeks.org/wp-content/uploads/20230814111654/Solution-Of-4-Queen-Problem.png">
</div>

The expected output is in the form of a matrix that has '__Q__'s for the blocks where queens are placed and the empty spaces are represented by '__.__'. For example, the following is the output matrix for the above 4-Queen solution.

```
. Q . .
. . . Q 
Q . . .
. . Q . 
```

### N Queen Problem using Backtracking

> The idea is to place queens one by one in different columns, starting from the leftmost column. When we place a queen in a column, we check for clashes with already placed queens. In the current column, if we find a row for which there is no clash, we mark this row and column as part of the solution. If we do not find such a row due to clashes, then we backtrack and return __false__.

Below is the recursive tree of the above approach:

<div align="center">
<img src="https://media.geeksforgeeks.org/wp-content/uploads/20230814111826/Backtracking.png">
</div>

Follow the steps mentioned below to implement the idea:

__Step 1__:  Start in the leftmost column

__Step 2__: If all queens are placed return true

__Step 3__: Try all rows in the current column. Do the following for every row.

- If the queen can be placed safely in this row. Then mark this __[row, column]__ as part of the solution and recursively check if placing queen here leads to a solution. If placing the queen in __[row, column]__ leads to a solution then return __true__. If placing queen doesn’t lead to a solution then unmark this __[row, column]__ then backtrack and try other rows.
- If all rows have been tried and valid solution is not found return __false__ to trigger backtracking.

</div>

> [!NOTE]
> We can also solve this problem by placing queens in rows as well.

<div align="justify">

__Time Complexity__: O(N!)

__Auxiliary Space__: O(N^2)

### Further Optimization in is_safe() function

The idea is not to check every element in the right and left diagonal, instead use the property of diagonals:

- The sum of __i__ and __j__ is constant and unique for each right diagonal, where i is the row of elements and __j__ is the column of elements. 
- The difference between __i__ and __j__ is constant and unique for each left diagonal, where __i__ and __j__ are row and column of element respectively.

__Complexity Analysis__

__Time Complexity__: O(N!)

__Auxiliary Space__: O(N)

</div>