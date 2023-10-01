# 4x4 Sudoku Board Generator 

The program is currently generating solved 4x4 Sudoku board.

## How Program works;

1. The program first generates A matrix (2x2) with random values which are basically 1,2,3 and 4.
2. Then B and C matrices are generated randomly until all the rows and columns have unique values

---------
| A | B |
---------
| C | D |
---------

> Definition of some variables in the code.
- X=A+B
- Y=A+C
- T=C+D
- U=B+D

3. All permutations (total 24 for a 2x2 grid) are generated for the last matrix, D, and I call them one by one to check if Sudoku board have a unique solution.
You may feel surprised but all possible permutations may not produce the expected result for matrix D. That's why I resume and reproduce A, B and C until D matrix from all permutions meets the 4x4 Sudoku board constraints.



  
