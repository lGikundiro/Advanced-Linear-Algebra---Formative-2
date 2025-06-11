## Creating Tests

### tests/test_matrix.py
import unittest
from alumathGroup26 import Matrix, multiply_matrices, add_matrices, subtract_matrices

class TestMatrix(unittest.TestCase):
    
    def test_matrix_creation(self):
        """Test matrix creation"""
        data = [[1, 2], [3, 4]]
        matrix = Matrix(data)
        self.assertEqual(matrix.rows, 2)
        self.assertEqual(matrix.cols, 2)
        self.assertEqual(matrix.data, data)
    
    def test_matrix_multiplication(self):
        """Test matrix multiplication"""
        matrix1 = Matrix([[1, 2], [3, 4]])
        matrix2 = Matrix([[5, 6], [7, 8]])
        result = multiply_matrices(matrix1, matrix2)
        expected = Matrix([[19, 22], [43, 50]])
        self.assertEqual(result.data, expected.data)
    
    def test_matrix_addition(self):
        """Test matrix addition"""
        matrix1 = Matrix([[1, 2], [3, 4]])
        matrix2 = Matrix([[5, 6], [7, 8]])
        result = add_matrices(matrix1, matrix2)
        expected = Matrix([[6, 8], [10, 12]])
        self.assertEqual(result.data, expected.data)
    
    def test_invalid_multiplication(self):
        """Test invalid matrix multiplication"""
        matrix1 = Matrix([[1, 2, 3]])  # 1x3
        matrix2 = Matrix([[1, 2], [3, 4]])  # 2x2
        with self.assertRaises(ValueError):
            multiply_matrices(matrix1, matrix2)

if __name__ == '__main__':
    unittest.main()