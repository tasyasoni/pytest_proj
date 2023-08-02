from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"
    assert arrs.get([1, 2, 3], -1, -2) == -2

def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([1, 2, 3], -1) == [3]
    assert arrs.my_slice([1, 2, 3], 0) == [1, 2, 3]
    assert arrs.my_slice([1, 2, 3], -1, -3) == []
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([1, 2, 3, 4], -3) == [2, 3, 4]
    assert arrs.my_slice([],) == []
    assert arrs.my_slice([1, 2, 3, 4], -5) == [1, 2, 3, 4]