import unittest
# import pytest


class CashbackHackService:

    def __init__(self):
        self.__boundary = 1000

    def remain(self, amount):
        return self.__boundary - amount % self.__boundary


class TestUnittest(unittest.TestCase):
    def test_500(self):
        cashback_servise = CashbackHackService()
        actual = cashback_servise.remain(500)
        self.assertEqual(actual, 500)

    def test_1000(self):
        cashback_servise = CashbackHackService()
        actual = cashback_servise.remain(1000)
        self.assertEqual(actual, 0)


class TestPytest:
    def test_500(self):
        cashback_servise = CashbackHackService()
        actual = cashback_servise.remain(500)
        assert actual == 500

    def test_1000(self):
        cashback_servise = CashbackHackService()
        actual = cashback_servise.remain(1000)
        assert actual == 0
