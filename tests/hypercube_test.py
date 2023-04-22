import unittest
from hypercube_utils import find_all_hypercubes

class TestHyperCube(unittest.TestCase):

    def test_min_all_dims(self):
        # Test cases for min_all_dims
        pass
    
    def test_find_coord(self):
        # Test cases for find_coord
        pass
    
    def test_gen_tst_pts(self):
        # Test cases for gen_tst_pts
        pass
    
    def test_test_pts(self):
        # Test cases for test_pts
        pass
    
    def test_line_in_list(self):
        # Test cases for line_in_list
        pass
    
    def test_hyper_cube_corners(self):
        # Test cases for hyper_cube_corners
        pass
    
    def test_find_lines(self):
        # Test cases for find_lines
        pass
    
    def test_find_all_cube_one_size(self):
        # Test cases for find_all_cube_one_size
        pass
    
    def test_find_all_hypercubes(self):
        # Test cases for find_all_hypercubes
        list_ = [[1,1], [1,2], [1,3], [2,1], [2,2], [2,3], [3,1], [3,2], [3,3], [4,1], [4,2], [4,3], [5,1], [5,2], [5,3]]
        self.assertEqual(find_all_hypercubes(list_),'11, {1: 8, 2: 3}')
    
if __name__ == '__main__':
    unittest.main()
