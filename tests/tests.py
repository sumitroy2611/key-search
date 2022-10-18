import src
from src.key_search import get_value
import unittest


# ========================================================================================================
# This is the unit test class to validate the functionality for the nested object key search utility
# ========================================================================================================
class Testing(unittest.TestCase):

    # test case function to check the search object function
    def test_0_search(self):
        search_object = '{"x":{"y":{"z":"a"}}}'
        search_key = 'x/y/z'

        print("Start search0 test with object %s and search key %s\n" %(search_object,search_key))

        expected_result = 'a'

        result = get_value(str(search_object), str(search_key))
        self.assertEqual(result,expected_result)

    # test case function to check the search object function
    def test_1_search(self):

        search_object = '{"a":{"b":{"c":"d"}}}'
        search_key = 'a/b/c'

        print("Start search1 test with object %s and search key %s\n" %(search_object,search_key))

        expected_result = 'd'

        result = get_value(str(search_object), str(search_key))
        self.assertEqual(result,expected_result)


    # test case function to check the search object function
    def test_2_search(self):
        search_object = '{"a":{"b":{"c":"d"}}}'
        search_key = 'a/b'

        print("Start search2 test with object %s and search key %s\n" %(search_object,search_key))

        expected_result = {'c':'d'}

        result = get_value(str(search_object), str(search_key))
        self.assertEqual(result,expected_result)

    # test case function to check the search object function
    def test_3_search(self):
        search_object = '{"x":{"y":{"z":"a"}}}'
        search_key = 'x'

        print("Start search3 test with object %s and search key %s\n" %(search_object,search_key))

        expected_result = {'y':{'z':'a'}}

        result = get_value(str(search_object), str(search_key))
        self.assertEqual(result,expected_result)

    # test case function to check the search object function
    def test_4_search(self):
        search_object = '{"x":{"y":{"z":"a"}}}'
        search_key = 'y/z'

        print("Start search4 test with object %s and search key %s\n" %(search_object,search_key))

        expected_result = None

        result = get_value(str(search_object), str(search_key))
        self.assertEqual(result,expected_result)

    # test case function to check the search object function
    def test_5_search(self):
        search_object = '{"x":{"y":{"z":"a"}}}'
        search_key = 'z'

        print("Start search5 test with object %s and search key %s\n" %(search_object,search_key))

        expected_result = None

        result = get_value(str(search_object), str(search_key))
        self.assertEqual(result,expected_result)

    if __name__ == '__main__':
        # begin the unittest.main()
        unittest.main()
 