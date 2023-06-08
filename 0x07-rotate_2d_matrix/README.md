# Rotate 2D-Matrix
Given an n x n 2D matrix, rotate it 90 degrees clockwise.

- Prototype: def rotate_2d_matrix(matrix):
- Do not return anything. The matrix must be edited in-place.
- You can assume the matrix will have 2 dimensions and will not be empty

# Explanation

1. The function takes the input matrix as an argument and calculates the size of the matrix, n, by using the length of the matrix.
2. It performs the rotation in two steps: transposing the matrix and reversing each row.
3. In the transposition step, we iterate over the upper triangle of the matrix (excluding the diagonal) and swap the elements with their corresponding elements across the diagonal.
   -  For example, if matrix[i][j] is the current element, we swap it with matrix[j][i].
   -  This step effectively reflects the elements along the main diagonal of the matrix.
4. After transposing, we iterate over each row of the matrix and reverse the elements in-place using slicing with [::-1].
   -  This step reverses the order of elements in each row, effectively rotating the matrix 90 degrees clockwise.
5. Since the matrix is edited in-place, there is no need to return anything.