<div align="justify">

# Algorithm to Solve Sudoku | Sudoku Solver

Given a partially filled 9×9 2D array ‘grid[9][9]’, the goal is to assign digits (from 1 to 9) to the empty cells so that every row, column, and subgrid of size 3×3 contains exactly one instance of the digits from 1 to 9. 

<div align="center">
<ig src="https://media.geeksforgeeks.org/wp-content/uploads/20240730112454/sudoku.jpg">
</div>

__Examples__

```
Input: grid
{ {3, 0, 6, 5, 0, 8, 4, 0, 0},
{5, 2, 0, 0, 0, 0, 0, 0, 0},
{0, 8, 7, 0, 0, 0, 0, 3, 1},
{0, 0, 3, 0, 1, 0, 0, 8, 0},
{9, 0, 0, 8, 6, 3, 0, 0, 5},
{0, 5, 0, 0, 9, 0, 6, 0, 0}, 
{1, 3, 0, 0, 0, 0, 2, 5, 0},
{0, 0, 0, 0, 0, 0, 0, 7, 4},
{0, 0, 5, 2, 0, 6, 3, 0, 0} }
Output:
3 1 6 5 7 8 4 9 2
5 2 9 1 3 4 7 6 8
4 8 7 6 2 9 5 3 1
2 6 3 4 1 5 9 8 7
9 7 4 8 6 3 1 2 5
8 5 1 7 9 2 6 4 3
1 3 8 9 4 7 2 5 6
6 9 2 3 5 1 8 7 4
7 4 5 2 8 6 3 1 9
Explanation: Each row, column and 3*3 box of the output matrix contains unique numbers.

Input: grid
{ { 3, 1, 6, 5, 7, 8, 4, 9, 2 },
{ 5, 2, 9, 1, 3, 4, 7, 6, 8 },
{ 4, 8, 7, 6, 2, 9, 5, 3, 1 },
{ 2, 6, 3, 0, 1, 5, 9, 8, 7 },
{ 9, 7, 4, 8, 6, 0, 1, 2, 5 },
{ 8, 5, 1, 7, 9, 2, 6, 4, 3 },
{ 1, 3, 8, 0, 4, 7, 2, 0, 6 },
{ 6, 9, 2, 3, 5, 1, 8, 7, 4 },
{ 7, 4, 5, 0, 8, 6, 3, 1, 0 } };
Output:
3 1 6 5 7 8 4 9 2 
5 2 9 1 3 4 7 6 8 
4 8 7 6 2 9 5 3 1 
2 6 3 4 1 5 9 8 7
9 7 4 8 6 3 1 2 5
8 5 1 7 9 2 6 4 3
1 3 8 9 4 7 2 5 6
6 9 2 3 5 1 8 7 4
7 4 5 2 8 6 3 1 9 
Explanation: Each row, column and 3*3 box of the output matrix contains unique numbers.
```

### Naive Approach

> The naive approach is to generate all possible configurations of numbers from 1 to 9 to fill the empty cells. Try every configuration one by one until the correct configuration is found, i.e. for every unassigned position fill the position with a number from 1 to 9. After filling all the unassigned positions check if the matrix is safe or not. If safe print else recurs for other cases.

__Follow the steps below to solve the problem:__

__Step 1__: Create a function that checks if the given matrix is valid sudoku or not. Keep Hashmap for the row, column and boxes. If any number has a frequency greater than 1 in the hashMap return false else return true;

__Step 2__: Create a recursive function that takes a grid and the current row and column index.

__Step 3__: Check some base cases.

- If the index is at the end of the matrix, i.e. i=N-1 and j=N then check if the grid is safe or not, if safe print the grid and return true else return false.
- The other base case is when the value of column is N, i.e j = N, then move to next row, i.e. i++ and j = 0.

__Step 4__: If the current index is not assigned then fill the element from 1 to 9 and recur for all 9 cases with the index of next element, i.e. i, j+1. if the recursive call returns true then break the loop and return true.

__Step 5__: If the current index is assigned then call the recursive function with the index of the next element, i.e. i, j+1

__Complexity Analysis__

__Time complexity__: O(9^(N*N)), For every unassigned index, there are 9 possible options so the time complexity is O(9^(n*n)).

__Space Complexity__: O(N*N), To store the output array a matrix is needed.

### Sudoku using Backtracking

Like all other Backtracking problems, Sudoku can be solved by assigning numbers one by one to empty cells. Before assigning a number, check whether it is safe to assign. 

Check that the same number is not present in the current row, current column and current 3X3 subgrid. After checking for safety, assign the number, and recursively check whether this assignment leads to a solution or not. If the assignment doesn’t lead to a solution, then try the next number for the current empty cell. And if none of the number (1 to 9) leads to a solution, return false and print no solution exists.

__Follow the steps below to solve the problem:__

__Step 1__: Create a function that checks after assigning the current index the grid becomes unsafe or not. Keep Hashmap for a row, column and boxes. If any number has a frequency greater than 1 in the hashMap return false else return true; hashMap can be avoided by using loops.

__Step 2__: Create a recursive function that takes a grid.

__Step 3__: Check for any unassigned location.

- If present then assigns a number from 1 to 9.
- Check if assigning the number to current index makes the grid unsafe or not. 
- If safe then recursively call the function for all safe cases from 0 to 9.
- If any recursive call returns true, end the loop and return true. If no recursive call returns true then return false.

__Step 4__: If there is no unassigned location then return true.

__Complexity Analysis__

__Time complexity__: O(9^(N*N)), For every unassigned index, there are 9 possible options so the time complexity is O(9^(n*n)). The time complexity remains the same but there will be some early pruning so the time taken will be much less than the naive algorithm but the upper bound time complexity remains the same.

__Space Complexity__: O(N*N), To store the output array a matrix is needed.

### Sudoku using Bit Masks

> This method is a slight optimization to the above 2 methods.  For each row/column/box create a bitmask and for each element in the grid set the bit at position ‘value’ to 1 in the corresponding bitmasks, for O(1) checks.

Follow the steps below to solve the problem:

- Create 3 arrays of size N (one for rows, columns, and boxes).
- The boxes are indexed from 0 to 8. (in order to find the box index of an element we use the following formula: __row / 3 * 3 + column / 3__).
- Map the initial values of the grid first.
- Each time we __add/remove__ an element to/from the grid set the bit to __1/0__ to the corresponding bitmasks.

__Complexity Analysis__

__Time complexity__: O(9^(N*N)). For every unassigned index, there are 9 possible options so the time complexity is O(9^(n*n)). The time complexity remains the same but checking if a number is safe to use is much faster, O(1).

__Space Complexity__: O(N*N). To store the output array a matrix is needed, and 3 extra arrays of size n are needed for the bitmasks.

### Sudoku using Cross-Hatching with backtracking

> This method is an optimization of the above method 2. It runs 5X times faster than method 2. Like we used to fill sudoku by first identifying the element which is almost filled. It starts with identifying the row and column where the element should be placed. Picking the almost-filled elements first will give better pruning.

Follow the steps below to solve the problem:

- Build a graph with pending elements mapped to row and column coordinates where they can be fitted in the original matrix.
- Pick the elements from the graph sorted by fewer remaining elements to be filled.
- Recursively fill the elements using a graph into the matrix. Backtrack once an unsafe position is discovered.

__Complexity Analysis__

__Time complexity__: O(9^(n*n)).  Due to the element that needs to fit in a cell will come earlier as we are filling almost filled elements first, it will help in less number of recursive calls. So the time taken will be much less than the naive approaches but the upper bound time complexity remains the same.

__Auxiliary Space__: O(n*n).  A graph of the remaining positions to be filled for the respected elements is created.

</div>