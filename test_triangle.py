import unittest
from triangle_solver import TriangleSolver, solve_triangle

class TestTriangleSolver(unittest.TestCase):
    
    def setUp(self):
        self.solver = TriangleSolver()
    
    def test_example_1(self):
        triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
        result = self.solver.minimum_path_sum(triangle)
        self.assertEqual(result, 11)
        
        min_sum, path = self.solver.find_actual_path(triangle)
        self.assertEqual(min_sum, 11)
        self.assertEqual(path, [2, 3, 5, 1])
    
    def test_example_2(self):
        triangle = [[-1], [2, 3], [1, -1, -3], [4, 2, 1, 3]]
        result = self.solver.minimum_path_sum(triangle)
        self.assertEqual(result, 0)
        
        min_sum, path = self.solver.find_actual_path(triangle)
        self.assertEqual(min_sum, 0)
        self.assertEqual(path, [-1, 3, -3, 1])
    
    def test_single_row(self):
        triangle = [[5]]
        result = self.solver.minimum_path_sum(triangle)
        self.assertEqual(result, 5)
        
        min_sum, path = self.solver.find_actual_path(triangle)
        self.assertEqual(min_sum, 5)
        self.assertEqual(path, [5])
    
    def test_two_rows(self):
        triangle = [[1], [2, 3]]
        result = self.solver.minimum_path_sum(triangle)
        self.assertEqual(result, 3)
        
        min_sum, path = self.solver.find_actual_path(triangle)
        self.assertEqual(min_sum, 3)
        self.assertEqual(path, [1, 2])
    
    def test_negative_numbers(self):
        triangle = [[-1], [-2, -3], [-4, -5, -6]]
        result = self.solver.minimum_path_sum(triangle)
        self.assertEqual(result, -10)
        
        min_sum, path = self.solver.find_actual_path(triangle)
        self.assertEqual(min_sum, -10)
        self.assertEqual(path, [-1, -3, -6])
    
    def test_optimized_solution(self):
        triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
        result_standard = self.solver.minimum_path_sum(triangle)
        result_optimized = self.solver.minimum_path_sum_optimized(triangle)
        self.assertEqual(result_standard, result_optimized)

if __name__ == '__main__':
    unittest.main()
