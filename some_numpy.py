import numpy as np

grid = np.zeros(shape=(10000,10000), dtype=float)

grid += 10

a = np.array([[1,2,3],[4,5,6],[7,8,9]])

print(a[1:3,1:3])

b = np.where(a<5, 0, a)
print(b) # [[0,0,0],[0,5,6],[7,8,9]]

# matrix: follows linear algebra rules of computation
m = np.matrix([[1,-2,3],[0,4,5],[7,8,-9]])
v = np.matrix([[2],[3],[4]])

print(m*v)