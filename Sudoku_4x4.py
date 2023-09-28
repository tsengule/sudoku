# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np



values = [1, 2, 3, 4]
# random block generator 2x2
# Generates a random 2x2 matrix using the specified values without repetion
def gen_block(values):
    np.random.shuffle(values)
    gen_block = np.reshape(values, (2, 2))
    return gen_block

# Checks if each row has unique values
def check_unique_rows(matrix):
    for row in matrix:
        if len(set(row)) != len(row):
            return False
    return True


# def f_shuffle(y):
# # Step 2: Flatten the matrix
#     flattened_matrix = y.flatten()
# # Step 3: Shuffle the values
#     np.random.shuffle(flattened_matrix)
# # Step 4: Reshape the shuffled array back into a 2x2 matrix
#     new = flattened_matrix.reshape((2, 2))
# return new

# Generate starting first 2x2 block 
A = gen_block(values)
# print("1st Random 2x2 matrix with specified values:")
# print(A)


# Generates second block until rows in new 2x4 matrix have unique values
while True:
    B= gen_block(values)
    X = np.hstack((A, B))
    is_unique = check_unique_rows(X)
    if is_unique == True:
        break

# print("2nd Random 2x2 matrix with specified values:")
# print(B)

# print("Concatenated 2x4 matrix with specified values:")
# print(X)

# Generates third block until columns in new 4x2 matrix have unique values
while True:
    C= gen_block(values)
    Y = np.hstack((np.transpose(A),np.transpose(C)))
    is_unique = check_unique_rows(Y)
    if is_unique == True:
        break
    
# print("Concatenated Y 4x2 matrix with specified values:")
# print(np.transpose(Y))

# Generates the last block of Total sudoku matrix 4x4 randomly
counter = 0  # Initialize the counter
while True:
    D= gen_block(values)
    T = np.hstack((C, D))
    U = np.hstack((np.transpose(B),np.transpose(D)))
    is_unique1 = check_unique_rows(T)
    is_unique2 = check_unique_rows(U)
    counter += 1  # Increment the counter with each iteration
    if counter > 1000:
        print("Counter is bigger than 100. Restart the program.")
        break
    if ((is_unique1 == True) and (is_unique2 == True)):
        break

# print("Concatenated U 4x2 matrix with specified values:")
# print(np.transpose(U))


#Total sudoku matrix 4x4
print("4x4 Sudoku")
print(np.hstack((np.transpose(Y),np.transpose(U))))
print("Number of iterations:", counter)




