import unittest

from SSW567API import getGithubRepoInfo

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestAPI(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testUsernameInput(self): 
        self.assertEqual(getGithubRepoInfo(""),'Username Missing')
    def testUsernameLength(self): 
        self.assertEqual(getGithubRepoInfo("sdafsdlakfjsdjasdflkmsdkflaksdfskladfklsjdaklflsadklfjlsajdkfjskadfsdklfjslafljsadfklsajdlkfjslkajdfljsaldjflksjdlfjsjdafkjsjdalfksajdfkljsadlkfjlksadjfljsadlkf"),'Invalid Username')
    def testPrintSuccess(self): 
        self.assertEqual(getGithubRepoInfo("joantubungbanua"),'Successfully Printed!')
    

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

