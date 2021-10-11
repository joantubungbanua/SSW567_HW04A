from typing import type 
from requests.api import get
import unittest
from unittest.mock import patch


import SSW567API
from SSW567API import getGithubRepoInfo

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestAPI(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    @patch('SSW567.getGithubRepoInfo')
    def testUsernameInput(self, mock_getGithubRepoInfo): 
        
        self.assertEqual(getGithubRepoInfo(""),'Username Missing')
    def testUsernameLength(self, mock_getGithubRepoInfo): 
        self.assertEqual(getGithubRepoInfo("sdafsdlakfjsdjasdflkmsdkflaksdfskladfklsjdaklflsadklfjlsajdkfjskadfsdklfjslafljsadfklsajdlkfjslkajdfljsaldjflksjdlfjsjdafkjsjdalfksajdfkljsadlkfjlksadjfljsadlkf"),'Invalid Username')
    def testPrintSuccess(self): 
        self.assertEqual(getGithubRepoInfo("joantubungbanua"),'Successfully Printed!')
    

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
