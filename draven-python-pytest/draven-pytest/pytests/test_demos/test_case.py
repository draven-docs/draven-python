import pytest
import sys

class TestCase():
    ''' def inc():
         return 1'''

    def test_answer(self):
        print("123456")
        assert 1 == 1


if __name__ == '__main__':
    # pytest.main("-v -x test_case.py")
    pytest.main(['-v', '-x', 'test_case.py'])
