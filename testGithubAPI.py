import unittest
from SSW567API import getGithubRepoInfo
import SSW567API
from unittest.mock import patch


# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestAPI(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    @patch('SSW567API.getGithubRepoInfo')
    def testUsernameInput(self, mock_getGithubRepoInfo): 
        mock_getGithubRepoInfo.returnValue = 'Username is Missing'
        repos = SSW567API.getGithubRepoInfo('')
        self.assertEqual(getGithubRepoInfo(""),'Username Missing')
    @patch('SSW567API.getGithubRepoInfo')
    def testUsernameLength(self,mock_getGithubRepoInfo): 
        mock_getGithubRepoInfo.returnValue = 'Invalid Username'
        repos = SSW567API.getGithubRepoInfo('sdafsdlakfjsdjasdflkmsdkflaksdfskladfklsjdaklflsadklfjlsajdkfjskadfsdklfjslafljsadfklsajdlkfjslkajdfljsaldjflksjdlfjsjdafkjsjdalfksajdfkljsadlkfjlksadjfljsadlkf')
        self.assertEqual(getGithubRepoInfo("sdafsdlakfjsdjasdflkmsdkflaksdfskladfklsjdaklflsadklfjlsajdkfjskadfsdklfjslafljsadfklsajdlkfjslkajdfljsaldjflksjdlfjsjdafkjsjdalfksajdfkljsadlkfjlksadjfljsadlkf"),'Invalid Username')
        
    
    

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()