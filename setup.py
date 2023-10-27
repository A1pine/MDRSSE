import os
import random
from kd_tree import build_kd_tree

# Assuming lambda is a predefined security parameter (bit length)
lambda_ = 128  # For example, 128 bits
threshold = 3 # gamma in the original paper

# Placeholder for the f_t function, which seems to generate a k-d tree (kdt)
def f_t(delta, depth):
    # Implement the actual k-d tree generation logic here
    # For now, we return a mock dictionary representing a k-d tree
    return {"node1": ["leaf1", "leaf2"], "node2": ["leaf3", "leaf4"]}

# Placeholder for the encryption function
def Enc_k(data):
    # Implement the actual encryption logic here
    return f"enc({data})"

# Placeholder for the F function, which seems to be a pseudorandom function (PRF)
def F(key, data):
    # Implement the actual PRF logic here
    return f"prf({key}, {data})"

# The EDS Setup function as described in the pseudo-code
def EDS_Setup(lambda_, I_t):
    random_list = [0, 1]
    T = {}  # Initialize an empty set T indexed by nodes' Tag
    K_s = random.choices(random_list, k = 1)  # Generate a random key of lambda bits
    K_t = random.choices(random_list, k = 1)  # Generate another random key of lambda bits
    EDS = {}

    for n_i in I_t:
        K_i = F(K_s, n_i)
        Tag_i = F(K_t, n_i)
        # y = len(I_t[n_i])  # Assuming y is the number of elements in I_t[n_i]
        for j in range(1, threshold):
            for elements in I_t[n_i]:
                c_i = Enc_k(elements)
                if Tag_i not in T:
                    T[Tag_i] = []
                T[Tag_i].append(c_i)
    
    EDS['T'] = T
    return EDS, K_s, K_t

# The Setup function as described in the pseudo-code
def Setup(mu, Lambda):
    kdt = f_t(mu, Lambda)  # Assuming delta and depth are represented by mu and Lambda
    I_t = kdt  # Assuming I_t is the k-d tree itself in this mock implementation
    EDS, K_s, K_t = EDS_Setup(lambda_, I_t)
    K = (K_s, K_t)
    kdt_prime = "kdt_without_leaf_nodes"  # Placeholder for kdt without leaf nodes
    # Data owner stores K and kdt_prime
    return EDS, K

# Example usage:
# mu = "example_mu"
# Lambda = "example_Lambda"
# EDS, K = Setup(mu, Lambda)
# print(EDS)
# print(K)

# Example
points = [
    (66, 430),
    (32, 120),
    (47, 110),
    (27, 200),
    (35, 470),
    (36, 280),
    (42, 250),
    (64, 210),
    (50, 365),
    (58, 510),
    (47, 540),
    (67, 620)
]
kd_tree = build_kd_tree(points, threshold=3)