# Homework 2
from cProfile import label

import numpy as np
import matplotlib.pyplot as plt

A = np.array([[1,2],
     [3,4],
     [5,6]])

B = np.array([[7,8],
     [9,10],
     [11,12]])

C = np.array([[1,3],
     [2,4]])

D = A + B
print("D:",D)

E = A - B
print("E:",E)

F = np.dot(A,C)
print("F:",F)

G = 2* A
print("G:",G)

# Systems of Equations
a = np.array([[2,3],
              [4,1]])
b = np.array([[5],
              [6]])
x = np.linalg.solve(a,b)
print("x:", x)

# Step 1
# Use parametric equation to create circle values
theta = np.linspace(0, 2 * np.pi, 100)
radius = 1
a = radius * np.cos(theta)
b = radius * np.sin(theta)

# Pair x values with y values
circPoints = zip(a,b)

# Set up plot
fig, ax = plt.subplots(1)
ax.plot(a,b)
ax.set_xlim([-5,5])
ax.set_ylim([-5,5])
ax.set_aspect(1)
ax.grid()

A = np.array([[3, -2], [1,0]])

# Step 2
# Multiply AX and plot points
for x,y in circPoints:
    print(f"x, {x} -- y, {y}")
    c = np.array([[x],[y]])
    sol = np.dot(A, c)
    ax.plot(sol[0], sol[1], 'bo')

# Step 3
ev1  = np.array([[1],[2]])
ev2  = np.array([[1],[1]])
ax.plot(ev1[0], ev1[1], 'mo', label="eigen vector 1")
ax.plot(ev2[0], ev2[1], 'mo', label="eigen vector 2")


# Step 4
v1 = ev1 * 2
av1 = np.dot(A, ev1)
av2 = np.dot(A, ev2)

ax.plot(v1[0],v1[1], 'r+', label=r'$\lambda$1v1')
ax.plot(ev2[0],ev2[1], 'c+', label=r'$\lambda$2v2')
ax.plot(av1[0],av1[1], 'b+', label="Av1")
ax.plot(av2[0],av2[1], 'g+', label="Av2")

handles, labels = ax.get_legend_handles_labels()
fig.legend(handles, labels, loc='upper right')

plt.title("Unit Circle X Multiplied by Matrix A")
plt.show()



