# This is a sample Python script.
import numpy as np


def power_iteration(A):
    #   Chooses a random vector
    b_k = np.random.rand(A.shape[1])
    #   Uses a recursive function to find
    answer = power_iteration_aux(A, b_k, 0)

    return answer


def power_iteration_aux(A, b_k, iter):
    # multiplies the vector times the matrix
    b_k1 = np.dot(A, b_k)

    # calculate the norm
    b_k1_norm = np.linalg.norm(b_k1)

    # re normalize the vector
    b_k = b_k1 / b_k1_norm
    #   if the vectors are close this means that we have converged
    iter += 1
    if np.allclose(b_k, b_k1) or iter > 900:
        return b_k, b_k1_norm
    else:
        return power_iteration_aux(A, b_k, iter)


print(power_iteration(np.array([[7, 2], [-4, 1]])))
