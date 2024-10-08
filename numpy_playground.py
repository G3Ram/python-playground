import numpy as np

# Single Dimensional array
a_arr = np.array([1, 2, 3])
print(a_arr)

b_arr = np.arange(3)
c_arr = np.arange(0, 10, 2)
d_arr = np.arange(0, 10, 3, dtype=float)
print(b_arr)
print(c_arr)
print(d_arr)

# linspace for equal spacing
e_arr = np.linspace(0, 20, 3)
print(e_arr)

e1_arr = np.linspace(0, 20, 4, dtype=int)
print(e1_arr)

char_arr = np.array(["hello world!"])
print(char_arr)
print(char_arr.dtype)

ones_arr = np.ones(20)
print(ones_arr)

ones_int_arr = np.ones(20, dtype=int)
print(ones_int_arr)

zeros_arr = np.zeros(20)
print(zeros_arr)

zeros_int_arr = np.zeros(20, dtype=int)
print(zeros_int_arr)

empty_arr = np.empty(20)
print("Empty Array initialization -> ", empty_arr)

empty_int_arr = np.empty(20, dtype=int)
print("Empty int Array initialization -> ", empty_int_arr)

# Note: cannot pass dtype for rand
rand_arr = np.random.rand(3)
print("Random array ->", rand_arr)

# Two dimensional arrays
two_dim_arr = np.array([[1, 2, 3], [2, 3, 4]])
print(two_dim_arr)
