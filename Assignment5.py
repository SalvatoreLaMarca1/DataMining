
# Assignment 5 - Data Mining 
#
# Author: Salvatore La Marca

import numpy as np
import pandas as pd

# Processor Speed
A = np.array([3.06, 500, 6])
p_sf = 1
A_scaled = A * p_sf

# Disk Size
B = np.array([2.68, 320, 4])
d_sf = 0.01
B_scaled = B * d_sf

# Main-memory
C = np.array([2.92, 640, 6])
m_sf = 0.5
C_scaled = C * m_sf

print("Data Mining Assignment 5 -- Salvatore La Marca")

# A, B, C vectors
print()
print("Vectors")
print("A: ", A)
print("B: ", B)
print("C: ", C)
print()
print("Scaled Vectors")
print("A: ", A_scaled)
print("B: ", B_scaled)
print("C: ", C_scaled)
print()
print("-----------------------------")
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
print("Scaled Cosine Similarity: A, B")
print(cosine_similarity(A_scaled, B_scaled))
print()
print("Scaled Cosine Similarity: A, C")
print(cosine_similarity(A_scaled, C_scaled))
print()
print("Scaled Cosine Similarity: B, C")
print(cosine_similarity(B_scaled, C_scaled))
print()
print("What can be said about similarity between A and B, A and C, and B and C?")
print("A and B: These share very close similarity with this value.")
print()
print("A and C: These share very close similarity with this value.")
print()
print("B and C: These share very close similartiy with this value.")
print()
print("-----------------------------")
print()

# Compute the Jaccard Distance with two entered NumPy Arrays
def jaccard_distance(X, Y):
    intersect = np.intersect1d(X, Y)
    denom = len(X) + len(Y) - len(intersect)
    jaccard_index = len(intersect) / denom
    
    return 1 - jaccard_index

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
print()
boolean_matrix = boolean_matrix.T

# 0 1 Matrix
print("0 1 Utility Matrix")
zero_one_matrix = boolean_matrix.replace(True, 1)
zero_one_matrix = zero_one_matrix.replace(False, 0) 
print(zero_one_matrix.T)
print()
print("-----------------------------")
print()

# Computer Jaccard distance for Boolean Utility Matrix
print("Jaccard Distance for User Pairs - Boolean Utility Matrix")
print("User A and B")
print(jaccard_distance(boolean_matrix['User A'], boolean_matrix['User B']))
print()
print("User A and C")
print(jaccard_distance(boolean_matrix['User A'], boolean_matrix['User C']))
print()
print("User B and C")
print(jaccard_distance(boolean_matrix['User B'], boolean_matrix['User C']))
print()

print("Jaccard Distance for User Pairs - 0 1 Utility Matrix")
print("User A and B")
print(jaccard_distance(zero_one_matrix['User A'], zero_one_matrix['User B']))
print()
print("User A and C")
print(jaccard_distance(zero_one_matrix['User A'], zero_one_matrix['User C']))
print()
print("User B and C")
print(jaccard_distance(zero_one_matrix['User B'], zero_one_matrix['User C']))
print()

print("Cosine Similarities - 0 1 Utility Matrix")
print("User A and B")
print(cosine_similarity(zero_one_matrix['User A'], zero_one_matrix['User A']))
print()
print("User A and C")
print(cosine_similarity(zero_one_matrix['User A'], zero_one_matrix['User C']))
print()
print("User B and C")
print(cosine_similarity(zero_one_matrix['User A'], zero_one_matrix['User C']))
print()
print("What can be said about similarity between A and B, A and C, and B and C?")
print("A and B: This value signals perfect similarity.")
print()
print("A and C: This value signals similar leaning results.")
print()
print("B and C: This value signals similar leaning results.")
print()