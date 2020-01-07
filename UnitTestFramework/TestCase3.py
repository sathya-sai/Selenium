"""
    :Summary This is python 3.7 supported usage of setUp,tearDown,setUpClass,tearDownClass,setUpModule,tearDownModule,

    :Since January 2020

    :Author Sathya Sai M

    :keyword Python, Selenium, Unittesting

"""
import unittest


def setUpModule():
    print("setup module")  # this will execute before all the test cases


def tearDownModule():
    print("tear down module")  # this will execute after all the test cases


class Test(unittest.TestCase):
    @classmethod
    def setUp(self):
        print("hi")  # this will execute before all the test cases

    @classmethod
    def tearDown(self):
        print("hello")  # this will execute after all the test cases

    @classmethod
    def setUpClass(cls):
        print("open")  # this will execute only once after the class is started

    @classmethod
    def tearDownClass(cls):
        print("close")  # this will execute only once after the class is ended

    def test_firstTest(self):
        print("This is my first unittest")

    def test_secondTest(self):
        print("This is my second unittest")

    def test_thirdTest(self):
        print("This is my third unittest")

    def test_forthTest(self):
        print("This is my forth unittest")


if __name__ == '__main__':
    unittest.main()
