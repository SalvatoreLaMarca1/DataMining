
# Assignment 5 - Data Mining 
#
# Author: Salvatore La Marca

import numpy as np
import pandas as pd

# Processor Speed
A = np.array([3.06, 500, 6])
p_sf = 1

# Disk Size
B = np.array([2.68, 320, 4])
d_sf = 0.01

# Main-memory
C = np.array([2.92, 640, 6])
m_sf = 0.5

# A, B, C vectors
print()
print("Vectors")
print("A: ", A)
print("B: ", B)
print("C: ", C)
print()

# compute and return the cosine similarity of the two entered vectors -> enter as NumPy arrays
def cosine_similarity(X, Y):
    X = np.array(X)
    Y = np.array(Y)
    
    dot_product = np.dot(X, Y)
    norm_X = np.linalg.norm(X)
    norm_Y = np.linalg.norm(Y)
    
    return (dot_product / (norm_X * norm_Y))

print("Cosine Similarity: A, B")
print(cosine_similarity(A, B))
print()
print("Cosine Similarity: A, C")
print(cosine_similarity(A, C))
print()
print("Cosine Similarity: B, C")
print(cosine_similarity(B, C))
print()
print("-----------------------------")
print()

# Utility Matrix
u_matrix = {
    'User A': [4, 5, np.nan, 5, 1, np.nan, 3, 2],
    'User B': [np.nan, 3, 4, 3, 1, 2, 1, np.nan],
    'User C': [2, np.nan, 1, 3, np.nan, 4, 5, 3]
}
df = pd.DataFrame(u_matrix)
df = df.T
df.columns = [chr(65 + i) for i in range(len(df.columns))]
print("Utility Matrix")
print(df)
print()

# Boolean Matrix
print("Boolean Utility Matrix")
boolean_matrix = df.notna()
print(boolean_matrix)
