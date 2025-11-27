import numpy as np


matrix = [
    [2, 3, 1, 4, 5, 6, 7],
    [8, 1, 3, 2, 2, 6, 8],
    [1, 4, 3, 1, 0, 2, 5],
    [4, 5, 0, 1, 3, 2, 1],
    [8, 7, 9, 1, 0, 2, 3]
]

np_matrix = np.array(matrix)
box1 = np_matrix[0:3, 0:2]
print (box1)
print(f"___________________")

np_matrix = np.array(matrix)
box2 = np_matrix[1:3, 3:5]
print (box2)
print(f"___________________")

np_matrix = np.array(matrix)
box3 = np_matrix[0:3, 5:6]
print (box3)
print(f"___________________")

np_matrix = np.array(matrix)
box4 = np_matrix[4:, 0:2]
print (box4)
print(f"___________________")


np_matrix = np.array(matrix)
box5 = np_matrix[3:5, 2:4]
print (box5)
print(f"___________________")

np_matrix = np.array(matrix)
box6 = np_matrix[3:4, 5:]
print (box6)
print(f"___________________")