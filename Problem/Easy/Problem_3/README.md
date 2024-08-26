<div align="justify">

# Mean of array using recursion

To find the mean of the elements of the array. 

```
Mean = (Sum of elements of the Array) / (Total no of elements in Array)
```

__Examples__

```
Input : 1 2 3 4 5
Output : 3

Input : 1 2 3
Output : 2
```

To find the mean using recursion assume that the problem is already solved for N-1 ie you have to find for n

```
Sum of first N-1 elements = (Mean of N-1 elements)*(N-1)

Mean of N elements = (Sum of first N-1 elements + N-th elements) / (N)
```

</div>

> [!NOTE]
> Since array indexing starts from 0, we access N-th element using A[N-1].

<div align="center">
<img src="https://media.geeksforgeeks.org/wp-content/uploads/4-3.jpg">
</div>