import unittest

from TestSuites.Package1.TC_LoginTest import LoginTest
from TestSuites.Package1.TC_SignupTest import SignupTest

from TestSuites.Package2.TC_PaymentTest import PaymentTest
from TestSuites.Package2.TC_PaymentReturnsTest import PaymentReturnTest

# get all the test from LoginTest, SignupTest, PaymentTest, PaymentReturnTest
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(SignupTest)
tc3 = unittest.TestLoader().loadTestsFromTestCase(PaymentTest)
tc4 = unittest.TestLoader().loadTestsFromTestCase(PaymentReturnTest)

# Creating Test Suites
sanityTestSuite = unittest.TestSuite([tc1, tc2])  # sanity test suite
functionalTestSuite = unittest.TestSuite([tc3, tc4])  # functional test suite
masterTestSuite = unittest.TestSuite([tc1, tc2, tc3, tc4])  # all the test cases

# unittest.TextTestRunner(verbosity=2).run(sanityTestSuite)  # this will execute only sanityTestSuite
# unittest.TextTestRunner(verbosity=2).run(functionalTestSuite)  # this will execute only functionalTestSuite
unittest.TextTestRunner(verbosity=2).run(masterTestSuite)  # this will execute only masterTestSuite
