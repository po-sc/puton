import pytest
from bucketsort_input import bucketsort

@pytest.mark.parametrize("input_data, k, expected", [
    ([3, 2, 1, 0], 4, [0, 1, 2, 3]),
    ([1, 0, 1, 0], 2, [0, 0, 1, 1]),
    ([], 4, []),
    ([1, 2, 3, 1], 4, [1, 1, 2, 3])
])
def test_bucketsort(input_data, k, expected):
    assert bucketsort(input_data, k) == expected

def test_user_input(monkeypatch):
    inputs = iter(["3 2 1 0", "4"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    import bucketsort_input
    assert bucketsort_input.bucketsort([3, 2, 1, 0], 4) == [0, 1, 2, 3]

if __name__ == "__main__":
    pytest.main()
