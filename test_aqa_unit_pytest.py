import cashback_service


def test_500():
    cashback = cashback_service.CashbackHackService()
    actual = cashback.remain(500)
    assert actual == 500


def test_1000():
    cashback = cashback_service.CashbackHackService()
    actual = cashback.remain(1000)
    assert actual == 0

