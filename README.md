# Homogeneous System Solver

## Description
This Python program solves a homogeneous system of linear equations of the form Ax=0 and presents the solution in parametric vector form. It accepts input regarding the matrix size (number of rows and columns) and the matrix entries, either through a text file or hardcoded within the code.

## Input
The program takes input in the following formats:
- If using a text file:
    - The first line contains two space-separated integers denoting the number of rows and columns, respectively.
    - Subsequent lines contain the matrix entries, separated by spaces.
- If hardcoding the input:
    - Modify the values in the code directly in the `g` list, `r`, and `c` variables to represent the matrix size and entries.

## Algorithms Used
The program implements Gaussian elimination to transform the input matrix into its Reduced Row Echelon Form (RREF). After obtaining the RREF, it extracts the parametric vector form solution.

## How to Run
1. Provide input either via a text file or by modifying the hardcoded input section in the code.
2. Execute the Python script.
3. The program will display the RREF of the input matrix and the parametric vector form of the solution.

## Additional Notes
- The solution provided in parametric form excludes the trivial solution (where all variables are zero).
- Ensure the input matrix is a homogeneous system (where the constant terms are all zero).

## Demo
- Execute the program and observe the RREF matrix and the parametric form of the solution.

## Files
- `homogeneous_system_solver.py`: Python script containing the code.
- `maths_file.txt`: Sample text file format for input (can be replaced with your own).
