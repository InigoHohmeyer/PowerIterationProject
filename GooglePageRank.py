# This is a sample Python script.
import numpy as np

from scipy import spatial

def power_iteration(A):
    #   Chooses a random vector
    b_k = np.random.rand(A.shape[1])
    #   Uses a recursive function to find
    answer = power_iteration_aux(A, b_k)

    return answer

def power_iteration_aux(A, b_k):


    #   if the vectors are close with the np.allclose
    #   also if we have gone more than 500 iterations because that is near the maximum number of recursions in python
    b_k1 = b_k - 1
    b_k1_norm = 1
    while not np.allclose(b_k, b_k1):
        # calculate the matrix-by-vector product Ab
        b_k1 = np.dot(A, b_k)

        # calculate the norm
        b_k1_norm = np.linalg.norm(b_k1)

        # re normalize the vector
        b_k = b_k1 / b_k1_norm
    return (b_k, b_k1_norm)

print(power_iteration(np.array([[7, 2], [-4, 1]])))
