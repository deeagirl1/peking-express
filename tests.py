import ast
import json
import unittest
import JsonFiles

from PekingExpress import PekingExpress


# Function used for interpreting the json
def load_file(file):
    return PekingExpress(json.loads(file[0]))


class TestSortFunction(unittest.TestCase):

    # Test 1 Path
    def test_path_test1(self):
        # load file
        map1 = load_file(JsonFiles.test1)
        map1.solve()
        # get length
        length = map1.get_path()
        # assert
        self.assertEqual([3, 88], length)

    # Test 2 Path
    def test_path_test2(self):
        # load file
        map2 = load_file(JsonFiles.test2)
        map2.solve()
        # get length
        length = map2.get_path()
        # assert
        self.assertEqual([9, 7, 1, 4, 5, 3, 88], length)

    # Test 3 Path
    def test_path_test3(self):
        # load file
        map3 = load_file(JsonFiles.test3)
        map3.solve()
        # get length
        length = map3.get_path()
        # assert
        self.assertEqual([5, 88], length)

    # Test 4 Path
    def test_path_test4(self):
        # load file
        map4 = load_file(JsonFiles.test4)
        map4.solve()
        # get length
        length = map4.get_path()
        # assert
        self.assertIsNone(None, length)  # no path since, start point has no neighbours

    # Test 5 Path
    def test_path_test5(self):
        # load file
        map5 = load_file(JsonFiles.test5)
        map5.solve()
        # get length
        length = map5.get_path()
        # assert
        self.assertEqual([2, 5, 3, 88], length)

    # Test 6 Path
    def test_path_test6(self):
        # load file
        map6 = load_file(JsonFiles.test6)
        map6.solve()
        # get length
        length = map6.get_path()
        # assert
        self.assertEqual([15, 17, 3, 11, 12, 14, 88], length)

    # Test 7 Path
    def test_path_test7(self):
        # load file
        map7 = load_file(JsonFiles.test7)
        map7.solve()
        # get length
        length = map7.get_path()
        # assert
        self.assertEqual([11, 2, 22, 88], length)

    # Test 8 Path
    def test_path_test8(self):
        # load file
        map8 = load_file(JsonFiles.test8)
        map8.solve()
        # get length
        length = map8.get_path()
        # assert
        self.assertEqual([34, 14, 52, 38, 49, 21, 23, 61, 43, 63, 88], length)


if __name__ == '__main__':
    unittest.main()
