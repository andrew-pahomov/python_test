import unittest
import cashback_service

class TestUnittest(unittest.TestCase):
    def test_500(self):
        cashback_servise = cashback_service.CashbackHackService()
        actual = cashback_servise.remain(500)
        self.assertEqual(actual, 500)

    def test_1000(self):
        cashback_servise = cashback_service.CashbackHackService()
        actual = cashback_servise.remain(1000)
        self.assertEqual(actual, 0)

if __name__ == "__main__":
    unittest.main()
    print("Everything passed")