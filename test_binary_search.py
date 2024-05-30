import pytest
from binary_search import binary_search

@pytest.mark.parametrize("arr, x, expected", [
    ([1, 2, 3, 4, 5], 3, 2),
    ([1, 2, 3, 4, 5], 6, -1),
    ([], 1, -1),
    ([1], 1, 0)
])
def test_binary_search(arr, x, expected):
    assert binary_search(arr, x) == expected

if __name__ == "__main__":
    pytest.main()
