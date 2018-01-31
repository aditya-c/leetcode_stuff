import numpy as np
from scipy.spatial.distance import pdist, squareform
import matplotlib.pyplot as plt

# Create a new array from which we will select elements
a = np.arange(1, 13).reshape(4, 3)

print(a)  # prints "array([[ 1,  2,  3],
#                [ 4,  5,  6],
#                [ 7,  8,  9],
#                [10, 11, 12]])"

# Create an array of indices
b = np.array([0, 2, 0, 1])

# Select one element from each row of a using the indices in b
print("----\n", a[np.arange(4), b])  # Prints "[ 1  6  7 11]"

# Mutate one element from each row of a using the indices in b
a[np.arange(4), b] += 10

print("======\n", a)  # prints "array([[11,  2,  3],
#                [ 4,  5, 16],
#                [17,  8,  9],
#                [10, 21, 12]])

print("+++")

x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
v = np.array([1, 0, 1])
print(np.shape(v))
y = x + v  # Add v to each row of x using broadcasting
print(y)
print(v)


print(".....")
"""Broadcasting"""
w = np.array([4, 5])
x = np.array([[1, 2, 3], [4, 5, 6]])
# Add a vector to each column of a matrix
# x has shape (2, 3) and w has shape (2,).
# If we transpose x then it has shape (3, 2) and can be broadcast
# against w to yield a result of shape (3, 2); transposing this result
# yields the final result of shape (2, 3) which is the matrix x with
# the vector w added to each column. Gives the following matrix:
# [[ 5  6  7]
#  [ 9 10 11]]
print((x.T + w).T)
# Another solution is to reshape w to be a column vector of shape (2, 1);
# we can then broadcast it directly against x to produce the same
# output.
print(x + np.reshape(w, (2, 1)))


"""distance"""
print("'''''''''")
x = np.array([[0, 1], [1, 0], [2, 0]])
print(x)
d = squareform(pdist(x, 'euclidean'))
print(help(pdist))


######


# Compute the x and y coordinates for points on a sine curve
x = np.arange(0, 3 * np.pi, np.pi / 2)
y = np.sin(x)

# Plot the points using matplotlib
plt.plot(x, y)
plt.show()  # You must call plt.show() to make graphics appear.
