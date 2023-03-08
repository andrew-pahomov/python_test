import pytest
import cashback_service


class TestPytest:
    def test_500(self):
        cashback_servise = cashback_service.CashbackHackService()
        actual = cashback_servise.remain(500)
        assert actual == 500

    def test_1000(self):
        cashback_servise = cashback_service.CashbackHackService()
        actual = cashback_servise.remain(1000)
        assert actual == 0
