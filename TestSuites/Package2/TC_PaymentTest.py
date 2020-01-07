import unittest


class PaymentTest(unittest.TestCase):

    def test_paymentindollor(self):
        print("This is payment in dollor Test")
        self.assertTrue(True)

    def test_paymentinrupees(self):
        print("This is payment in rupees")
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
