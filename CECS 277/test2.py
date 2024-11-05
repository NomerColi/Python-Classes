import numpy as np
import matplotlib.pyplot as plt

# Define the grid for x and y
x = np.linspace(-5, 5, 20)
y = np.linspace(-5, 5, 20)
X, Y = np.meshgrid(x, y)

# Compute the magnitude function f(x, y) = sqrt(x^2 + y^2)
F = np.sqrt(X**2 + Y**2)

# Compute the components of the gradient of f(x, y)
Fx = X / F  # Partial derivative with respect to x
Fy = Y / F  # Partial derivative with respect to y

# Plot the vector field
plt.figure(figsize=(8, 8))
plt.quiver(X, Y, Fx, Fy, color='teal')
plt.xlabel('x')
plt.ylabel('y')
plt.title(r'Vector Field of $\nabla f(x, y) = \sqrt{x^2 + y^2}$')
plt.grid(True)
plt.axis('equal')
plt.show()