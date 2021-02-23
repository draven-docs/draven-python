import pytest
import sys


def test_answer(login):
    print("test_answer")


def test_question():
    print("test_question")


if __name__ == '__main__':
    # pytest.main("-v -x test_case.py")
    pytest.main(['-v', '-x', 'test_case.py'])
