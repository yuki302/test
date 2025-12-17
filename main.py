import os
import pytest
@pytest.fixture()
def beifan():
    print("\nsetup")
    yield
    print("\nteardown")

@pytest.mark.fixture
def test_case1(beifan):
    assert 1 + 1 == 2

# @pytest.mark.fixture
# def test_bbp(beifan):
#     assert 1+1 == 5

if __name__ == '__main__':
    # print("hello world")
    test_case1(beifan())