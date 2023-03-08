import cashback_service


class TestPytest:
    def test_500(self):
        cashback = cashback_service.CashbackHackService()
        actual = cashback.remain(500)
        assert actual == 500

    def test_1000(self):
        cashback = cashback_service.CashbackHackService()
        actual = cashback.remain(1000)
        assert actual == 0
