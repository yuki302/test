import os
import pytest
import allure

@allure.title("setup")
@pytest.fixture()
def beifan():
    print("\nsetup")
    yield
    print("\nteardown123")
@allure.title("success")
@pytest.mark.fixture
def test_case1(beifan):
    assert 1 + 1 == 2

@allure.title("fail")
@pytest.mark.fixture
def test_bbp(beifan):
     assert 1+1 == 5

if __name__ == '__main__':
    # print("hello world")
    test_case1(beifan)