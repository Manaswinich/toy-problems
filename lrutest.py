import unittest


class lrutest(unittest.TestCase):
    # Test case 1
    put(1, "a")
    self.assertEqual(get(1), "a")

    # Test case 2
    put(1, "b")
    self.assertEqual(get(1), "b")

    # Test case 3
    put(2, "c")
    self.assertEqual(get(2), "c")

    # Test case 4
    self.assertEqual(get(3), -1)

    # Test case 5
    self.assertEqual(get_cache, (1, "b")(2, "c"))


if __name__ == '__main__':
    unittest.main()
