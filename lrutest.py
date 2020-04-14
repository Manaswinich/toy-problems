
# obj = __import__("lrucache.py"
from lrucache import lrucache


def main():
    lr = lrucache(3)
    # Test case 1
    lr.put(1, "a")
    assert lr.get(1) == "a"

    # Test case 2
    lr.put(1, "b")
    assert lr.get(1) == "b"

    # Test case 3
    lr.put(2, "c")
    assert lr.get(2) == "c"

    # Test case 4
    assert lr.get(3) == -1

    # Test case 5
    lr.put(3, "f")
    assert lr.get(3) == "f"
    assert lr.get_cache() == {1: "b", 2: "c", 3: "f"}

    # Test case 6
    lr.put(4, "a")
    assert lr.get(4) == "a"

    # Test case 7
    assert lr.get_cache() == {2: "c", 3: "f", 4: "a"}

    print("Test cases passsed!")


if __name__ == '__main__':
    main()
