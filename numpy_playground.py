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
