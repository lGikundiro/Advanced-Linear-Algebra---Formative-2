# Advanced-Linear-Algebra---Formative-2
# AlumathGroup26 - Matrix Calculator Library Guide

# Description
A simple and efficient matrix calculator library for Python.

## Features

- Create and manipulate matrices
- Matrix multiplication with dimension validation

## Additional Features & Perks
- Matrix addition and subtraction
- Matrix transpose
- Easy-to-use API

## Installation Process

```bash
pip install alumathGroup26
from alumath import Matrix, multiply_matrices, add_matrices, subtract_matrices

# Create matrices
a = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

# Multiply matrices
mult = multiply_matrices(a, b)
print("Multiplication: \n", mult)

# Add matrices
add = add_matrices(a, b)
print("Subtraction: \n", add)

# Subtract matrices
sub = subtract_matrices(a, b)
print("Subtraction: \n", sub)
