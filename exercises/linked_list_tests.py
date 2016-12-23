'''
Implement the required functions in linked_list.py,
then run "python linked_list_tests.py".
'''

import unittest
from linked_list import LinkedList


class MyTest(unittest.TestCase):
    def test_to_string(self):
        ll = LinkedList()

        self.assertEqual(str(ll), "")

    def test_add_values(self):
        ll = LinkedList()

        ll.add(1)
        ll.add(2)
        ll.add(3)

        self.assertEqual(str(ll), "1->2->3")

    def test_contains_value(self):
        ll = LinkedList()

        ll.add(1)
        ll.add(2)
        ll.add(3)

        self.assertTrue(ll.contains(1))
        self.assertTrue(ll.contains(2))
        self.assertTrue(ll.contains(3))

        self.assertFalse(ll.contains(10))

    def test_remove_value(self):
        ll = LinkedList()

        ll.add(1)
        ll.add(2)
        ll.add(3)

        self.assertEqual(str(ll), "1->2->3")

        ll.remove(2)

        self.assertEqual(str(ll), "1->3")


if __name__ == "__main__":
    unittest.main()
