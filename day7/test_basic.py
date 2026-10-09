import pytest


def add(a: int, b: int) -> int:
    return a + b

@pytest.mark.parametrize(
    "a,b,expected",
    [
        (1,2,3),
        (2,3,5),
        (10,20,30),
        (0,0,0),
    ],
)


def test_add(a,b,expected):
    assert add(a, b) == expected


