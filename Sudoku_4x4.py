# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
from itertools import permutations


values = [1, 2, 3, 4]
# random block generator 2x2
# Generates a random 2x2 matrix using the specified values without repetion
def gen_block(val):
    np.random.shuffle(val)
    f1 = np.reshape(val, (2, 2))
    return f1

# Checks if each row has unique values
def check_unique_rows(matrix):
    for row in matrix:
        if len(set(row)) != len(row):
            return False
    return True

# Generates blocks until rows in new 2x4 matrix have unique values
def row_add(val):  
    A = gen_block(val)  
    while True:
        B = gen_block(val)
        X = np.hstack((A, B))
        is_uniquex = check_unique_rows(X)
        if is_uniquex == True:
            break
    while True:
        C=  gen_block(val)
        Y = np.hstack((np.transpose(A),np.transpose(C)))
        is_uniquey = check_unique_rows(Y)
        if is_uniquey == True:
            break
    return A, B, C, X, Y


A, B, C, X, Y = row_add(values)
# Generates the last block of Total sudoku matrix 4x4 via previous results
# Generate all permutations of the values
all_permutations = sorted(permutations(values))
counter = 0  # Initialize the counter

for i, perm in enumerate(all_permutations, start=1):
    # Create a 2x2 numpy array with int32 type
    D = np.array([[perm[0], perm[1]], [perm[2], perm[3]]], dtype=np.int32)
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
        
#Total sudoku matrix 4x4
print("4x4 Sudoku")
print(np.hstack((np.transpose(Y),np.transpose(U))))
print("Number of iterations:", counter)
