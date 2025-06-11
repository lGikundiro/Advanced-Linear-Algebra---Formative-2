"""
AlumathGroup26 - A simple matrix calculator library
"""

from .matrix import Matrix
from .operations import multiply_matrices, add_matrices, subtract_matrices

__version__ = "0.1.0"
__authors__ = "Terry Manzi, Liliane Gikundiro, Fidele Ndihokubwayo, and Anissa Tagawende"
__email__ = "m.terry@alustudent.com, l.gikundiro@alustudent.com, f.ndihokubw1@alustudent.com, a.tagawende@alustudent.com"

__all__ = [
    "Matrix",
    "multiply_matrices", 
    "add_matrices",
    "subtract_matrices"
]