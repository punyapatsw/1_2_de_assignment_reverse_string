from reverse_string import reverse_string
import pytest

class TestReverseString(object):
    def test_empty(self):
        assert reverse_string([])==[]

    def test_single_value(self):
        assert reverse_string(['1'])==['1']
        assert reverse_string(['a'])==['a']

    def test_normal_value(self):
        assert reverse_string(['a','b','c','d'])==['d','c','b','a']
        assert reverse_string(['1','2','3','4','5'])==['5','4','3','2','1']