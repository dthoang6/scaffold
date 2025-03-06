from hello import add


def test_hello():
    assert add(1, 2) == 3
    assert add(1, -1) == 0
