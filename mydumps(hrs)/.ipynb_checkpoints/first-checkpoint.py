import numpy as np

# Get the number of equations and variables
n = int(input("Enter the number of equations/variables: "))

# Initialize the coefficients matrix and constants vector
A = []
b = []

# Get the coefficients and constants from the user
for i in range(n):
    A.append(list(map(float, input(f"Enter coefficients of equation {i+1}: ").split())))
    b.append(float(input(f"Enter constant of equation {i+1}: ")))

# Check if the number of coefficients in each equation matches the number of variables
for equation in A:
    if len(equation) != n:
        print("Error: The number of coefficients in each equation must match the number of variables.")
        exit()

# Convert lists to numpy arrays
A = np.array(A)
b = np.array(b)

# Solve the system of equations
solution = np.linalg.solve(A, b)

print('Solution: ', solution)