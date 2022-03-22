import ast
import json
import unittest

from PekingExpress import PekingExpress


# Function used for interpreting the json
def load_file(file):
    return PekingExpress(json.loads(file[0]))


class TestSortFunction(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Declaring file cases
        self.test1 = [
            '{"Locations": {"number": 4, "critical": [1]}, "Connections": {"source": [3, 3, 2, 3, 1], "target": [88, 2, 1, 1, 88], "price": [3, 4, 8, 3, 3]}, "StartLocation": 3, "Budget": 3, "OccupiedLocationsAfterEachTurn": [[88], [3, 1], [88, 2], [1], [3, 2], [3, 88], [3], [88], [3, 1], [1]]}']

        self.test2 = [
            '{"Locations": {"number": 10, "critical": [3, 6]}, "Connections": {"source": [3, 1, 4, 9, 8, 3, 1, 3, 2, 1], "target": [5, 8, 5, 7, 5, 88, 7, 8, 88, 4], "price": [1, 8, 1, 7, 2, 6, 5, 4, 3, 2]}, "StartLocation": 9, "Budget": 25, "OccupiedLocationsAfterEachTurn": [[5], [4], [1], [7], [1, 9], [8], [1, 5], [7], [1], [4]]}']

        self.test3 = [
            '{"Locations": {"number": 10, "critical": [5, 6, 4, 7]}, "Connections": {"source": [5, 6, 4, 6, 3, 5, 5, 9, 8, 7, 6, 1, 6, 3, 2, 7, 3, 2, 5, 5], "target": [2, 9, 88, 4, 6, 9, 1, 88, 1, 8, 88, 88, 1, 4, 6, 4, 8, 3, 88, 6], "price": [2, 9, 2, 8, 3, 7, 3, 3, 9, 7, 7, 6, 3, 7, 1, 5, 8, 8, 1, 2]}, "StartLocation": 5, "Budget": 2, "OccupiedLocationsAfterEachTurn": [[1, 5, 88], [2, 1, 6, 4], [6, 8, 7], [4], [3, 7, 6], [9, 3, 6], [9, 88, 1, 2], [6, 8], [2, 9], [3, 5, 88]]}']

        self.test4 = [
            '{"Locations": {"number": 40, "critical": [25, 18, 6, 33, 32, 5, 15, 20, 9, 1]}, "Connections": {"source": [11, 9, 8, 38, 23, 12, 27, 25, 24, 22, 9, 33, 5, 10, 29, 11, 11, 5, 15, 34], "target": [35, 31, 9, 10, 37, 14, 18, 26, 30, 7, 10, 23, 27, 88, 12, 10, 9, 23, 26, 31], "price": [3, 8, 1, 1, 7, 5, 5, 1, 9, 3, 3, 9, 1, 8, 4, 9, 1, 1, 7, 9]}, "StartLocation": 13, "Budget": 74, "OccupiedLocationsAfterEachTurn": [[5, 9, 88], [23, 10], [5, 37], [27], [18, 5], [23, 27], [18], [27], [5, 18], [27, 23]]}']

        self.test5 = [
            '{"Locations": {"number": 7, "critical": [5, 1]}, "Connections": {"source": [2, 5, 3, 6, 1, 4, 5, 3, 6, 3, 5], "target": [5, 3, 6, 1, 4, 88, 1, 88, 88, 1, 4], "price": [1, 6, 3, 6, 2, 8, 7, 1, 7, 2, 3]}, "StartLocation": 2, "Budget": 19, "OccupiedLocationsAfterEachTurn": [[4, 5], [4, 5], [4, 1], [1, 3], [4]]}']

        self.test6 = [
            '{"Locations": {"number": 20, "critical": [16, 19, 8, 10, 12, 3, 6, 5, 13, 2, 4, 7, 18, 9, 17]}, "Connections": {"source": [15, 17, 3, 11, 6, 14, 12, 4, 1, 9, 8, 13, 2, 5, 16, 18, 10, 7, 19, 6, 14, 8, 16, 11, 4], "target": [17, 3, 11, 6, 14, 12, 4, 1, 9, 8, 13, 2, 5, 16, 18, 10, 7, 19, 88, 4, 88, 88, 88, 12, 88], "price": [7, 9, 6, 7, 2, 7, 9, 9, 4, 1, 3, 5, 9, 1, 1, 2, 2, 8, 9, 5, 7, 6, 6, 1, 5]}, "StartLocation": 15, "Budget": 78, "OccupiedLocationsAfterEachTurn": [[9, 19, 14, 6, 8], [9, 13, 1, 6], [2, 8, 9, 4, 14, 1, 11], [8, 13, 9], [1, 2], [9, 13, 4, 5], [12, 8, 88], [14, 16, 19, 11, 13, 8], [9, 2, 8, 6, 18], [8, 5, 14], [88, 2, 9, 12, 13], [8], [88, 13, 9], [1, 4, 14, 16], [88, 9, 5, 6]]}']

        self.test7 = [
            '{"Locations": {"number": 50, "critical": [40, 26, 27, 12, 17, 37, 30, 24, 32, 25, 5, 14, 38, 33, 8, 41, 1, 49, 48, 29, 20, 2, 28, 31, 39, 7, 23, 15, 44, 11]}, "Connections": {"source": [11, 2, 3, 18, 41, 49, 36, 37, 38, 9, 30, 25, 31, 35, 27, 5, 20, 12, 29, 47, 46, 26, 14, 32, 19, 44, 42, 10, 22, 4, 7, 45, 16, 40, 48, 34, 8, 23, 17, 6, 24, 21, 43, 39, 33, 28, 13, 15, 1, 38, 20, 40, 39, 41, 33, 38, 12, 37, 28, 26, 13, 17, 19, 31, 16, 24, 20, 47, 35, 37, 20, 15, 36, 34, 36, 44, 2, 31, 2, 9, 3, 44, 3, 24, 8, 16, 38, 18, 26, 6, 24, 18, 45, 32, 22, 44, 22, 30, 38, 10], "target": [2, 3, 18, 41, 49, 36, 37, 38, 9, 30, 25, 31, 35, 27, 5, 20, 12, 29, 47, 46, 26, 14, 32, 19, 44, 42, 10, 22, 4, 7, 45, 16, 40, 48, 34, 8, 23, 17, 6, 24, 21, 43, 39, 33, 28, 13, 15, 1, 88, 88, 1, 23, 1, 20, 1, 4, 24, 42, 15, 6, 88, 33, 10, 7, 33, 33, 40, 13, 44, 13, 15, 88, 47, 43, 14, 33, 28, 44, 22, 33, 49, 6, 44, 28, 21, 43, 40, 43, 44, 13, 88, 30, 6, 44, 88, 22, 34, 42, 19, 45], "price": [5, 2, 9, 2, 4, 4, 5, 4, 4, 2, 5, 7, 4, 3, 5, 4, 3, 8, 6, 1, 5, 7, 6, 1, 3, 6, 8, 4, 1, 6, 2, 2, 6, 6, 6, 4, 4, 6, 8, 1, 2, 6, 6, 3, 6, 5, 3, 9, 6, 6, 3, 4, 8, 5, 5, 8, 1, 2, 9, 6, 1, 8, 9, 6, 9, 7, 7, 4, 3, 1, 6, 3, 4, 5, 4, 2, 3, 1, 1, 6, 4, 8, 8, 6, 9, 3, 2, 6, 7, 6, 5, 7, 3, 9, 3, 9, 1, 5, 2, 9]}, "StartLocation": 11, "Budget": 167, "OccupiedLocationsAfterEachTurn": [[49, 14, 43, 88, 38], [13, 32, 37, 36, 24], [49, 12, 38, 14, 36], [20, 19, 37, 40, 47], [10, 36, 29, 44, 23], [26, 22, 37, 12, 6], [34, 13, 6, 26, 14], [43, 6, 44, 24, 36], [47, 18, 88, 37, 33], [15, 30, 28, 38, 36], [40, 1, 33, 47, 28], [38, 39, 23, 9, 20], [8, 5, 4, 15, 41], [34, 27, 13, 88, 28], [43, 2, 24, 8, 6], [13, 26, 45, 33, 21], [46, 88, 1, 44, 10], [33, 47, 15, 26, 31], [24, 46, 13, 6, 7], [26, 21, 12, 47, 24], [8, 36, 44, 33, 43], [23, 21, 47, 17, 6], [26, 40, 46, 17, 29], [20, 46, 44, 48, 47], [1, 40, 42, 29, 5], [15, 10, 27, 30, 20], [88, 12, 18, 5, 13], [28, 20, 30, 29, 15], [1, 28, 47, 12, 41], [2, 29, 33, 24, 39]]}']

        self.test8 = [
            '{"Locations": {"number": 70, "critical": [11, 38, 35, 32, 24, 40, 53, 2, 22, 18]}, "Connections": {"source": [34, 14, 52, 38, 49, 24, 37, 4, 53, 20, 28, 6, 13, 16, 32, 39, 7, 30, 35, 19, 2, 64, 58, 10, 46, 25, 15, 51, 11, 17, 65, 29, 56, 3, 23, 21, 48, 27, 61, 43, 22, 9, 50, 55, 69, 26, 54, 60, 57, 47, 42, 67, 59, 5, 33, 18, 1, 41, 40, 68, 45, 36, 31, 8, 44, 12, 62, 63, 66, 40, 69, 41, 10, 8, 56, 47, 11, 62, 69, 44, 39, 60, 27, 49, 43, 45, 27, 29, 23, 56, 43, 63, 39, 58, 28, 30, 15, 54, 43, 7], "target": [14, 52, 38, 49, 24, 37, 4, 53, 20, 28, 6, 13, 16, 32, 39, 7, 30, 35, 19, 2, 64, 58, 10, 46, 25, 15, 51, 11, 17, 65, 29, 56, 3, 23, 21, 48, 27, 61, 43, 22, 9, 50, 55, 69, 26, 54, 60, 57, 47, 42, 67, 59, 5, 33, 18, 1, 41, 40, 68, 45, 36, 31, 8, 44, 12, 62, 63, 66, 88, 88, 54, 66, 26, 62, 54, 59, 40, 66, 66, 66, 8, 62, 36, 21, 55, 62, 1, 43, 61, 26, 60, 88, 50, 18, 31, 42, 31, 66, 63, 11], "price": [2, 3, 9, 5, 4, 2, 9, 4, 1, 3, 5, 9, 4, 9, 9, 6, 6, 6, 6, 1, 9, 3, 6, 4, 3, 4, 8, 5, 1, 8, 1, 8, 9, 7, 7, 7, 3, 1, 6, 7, 6, 6, 1, 4, 9, 4, 6, 4, 9, 2, 6, 8, 1, 4, 1, 5, 7, 7, 7, 4, 6, 1, 2, 4, 6, 4, 2, 5, 4, 7, 6, 7, 6, 3, 3, 4, 6, 8, 8, 7, 6, 1, 5, 9, 7, 6, 4, 1, 2, 7, 3, 1, 1, 2, 7, 5, 7, 9, 2, 1]}, "StartLocation": 34, "Budget": 150, "OccupiedLocationsAfterEachTurn": [[8], [62, 39, 44], [60], [54, 43, 57], [29, 22]]}']

    # Test 1 Path
    def test_path_test1(self):
        # load file
        map1 = load_file(self.test1)
        map1.solve()
        # get length
        length = map1.get_path()
        # assert
        self.assertEqual([3, 88], length)

    # Test 2 Path
    def test_path_test2(self):
        # load file
        map2 = load_file(self.test2)
        map2.solve()
        # get length
        length = map2.get_path()
        # assert
        self.assertEqual([9, 7, 1, 4, 5, 3, 88], length)

    # Test 3 Path
    def test_path_test3(self):
        # load file
        map3 = load_file(self.test3)
        map3.solve()
        # get length
        length = map3.get_path()
        # assert
        self.assertEqual([5, 88], length)

    # Test 4 Path
    def test_path_test4(self):
        # load file
        map4 = load_file(self.test4)
        map4.solve()
        # get length
        length = map4.get_path()
        # assert
        self.assertIsNone(None, length)  # no path since, start point has no neighbours

    # Test 5 Path
    def test_path_test5(self):
        # load file
        map5 = load_file(self.test5)
        map5.solve()
        # get length
        length = map5.get_path()
        # assert
        self.assertEqual([2, 5, 3, 88], length)

    # Test 6 Path
    def test_path_test6(self):
        # load file
        map6 = load_file(self.test6)
        map6.solve()
        # get length
        length = map6.get_path()
        # assert
        self.assertEqual([15, 17, 3, 11, 12, 14, 88], length)

    # Test 7 Path
    def test_path_test7(self):
        # load file
        map7 = load_file(self.test7)
        map7.solve()
        # get length
        length = map7.get_path()
        # assert
        self.assertEqual([11, 2, 22, 88], length)

    # Test 8 Path
    def test_path_test8(self):
        # load file
        map8 = load_file(self.test8)
        map8.solve()
        # get length
        length = map8.get_path()
        # assert
        self.assertEqual([34, 14, 52, 38, 49, 21, 23, 61, 43, 63, 88], length)


if __name__ == '__main__':
    unittest.main()
