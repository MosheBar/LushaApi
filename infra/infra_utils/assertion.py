import enum
from asserts import *


class Assert:

    def equal(self, a, b, free_text=None):
        assert_equal(a, b, "failed to compare equal " + str(free_text) if free_text else '')

    def not_equal(self, a, b, free_text=None):
        assert_not_equal(a, b, "failed to compare not equal " + str(free_text) if free_text else '')

    def assert_contain(self, a, b, free_text=None):
        assert_true(a in b, "failed to validate in between " + str(free_text) if free_text else '')

    def assert_not_contain(self, a, b, free_text=None):
        assert_true(a not in b, "failed to validate not in between " + str(free_text) if free_text else '')

    def assert_true(self, expected, free_text=None):
        assert_true(expected, "failed to validate expected to be True " + str(free_text) if free_text else '')

    def compare_json(self, a, b, free_text=None):
        assert_true(self.ordered(a) == self.ordered(b), "failed to validate Jsons " + str(free_text) if free_text else '')

    @classmethod
    def ordered(cls, obj):
        if isinstance(obj, dict):
            return sorted((k, cls.ordered(v)) for k, v in obj.items())
        if isinstance(obj, list):
            return sorted(cls.ordered(x) for x in obj)
        else:
            return obj


class Compare(enum.Enum):
    """
    compare enum to select the comparison method
    """
    equal = Assert().equal
    contain = Assert().assert_contain
    compare_json = Assert().compare_json