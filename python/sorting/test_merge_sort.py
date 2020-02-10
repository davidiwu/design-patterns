import unittest
from unittest.mock import patch
from merge_sort import merge_sort

# run this unit test by below command if no unitest.main() running
# python -m unittest test_merge_sort.py
# https://docs.python.org/3/library/unittest.html

class TestMergeSort(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # only run once when the test started
        print('setup for class')

    @classmethod
    def tearDownClass(cls):
        # only run once when all the tests finished.
        print('tear down class')

    def setUp(self):
        # set up testing variables here
        # run before each test case
        print('setup')

    def tearDown(self):
        # run after each test case
        print('tear down')

    def test_merge_sort(self):
        # arrange
        arr = [12,2,44,4,1,17,12]
        expected = [1,2,4,12,12,17,44]

        # action
        actual = merge_sort(arr)

        # assert
        self.assertListEqual(actual, expected)

    def test_merge_sort_null(self):
        # arrange
        arr = []
        expected = []

        # action
        actual = merge_sort(arr)

        # assert
        self.assertListEqual(actual, expected)

    def test_merge_sort_one(self):
        # arrange
        arr = [1]
        expected = [1]

        # action
        actual = merge_sort(arr)

        # assert
        self.assertListEqual(actual, expected)

    def test_merge_sort_error(self):
        # arrange
        arr = 'good morning'

        # action & assert
        with self.assertRaises(TypeError):
            merge_sort(arr)

    # this is an exampe of mocking method used by the module we are testing
    def test_mock_obj(self):

        with patch('merge_sort._merge') as mocked_merge:

            mocked_merge.return_value = [1,2,3,4]
            arr = [2,3,1]
            actual = merge_sort(arr)
            self.assertListEqual(actual, [1,2,3,4])

if __name__ == '__main__':
    unittest.main()