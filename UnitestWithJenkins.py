import unittest
from junit_xml import TestSuite, TestCase
import urllib2



def GET_YNET():
    response = urllib2.urlopen('http://ynet.co.il')
    html = response.read()
    if 'ynet' in html.lower():
        return True
    else:
        return False


class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(GET_YNET(), True)



# test_cases = [TestCase('YnetTest',MyTest,10)]
# ts = TestSuite("my test suite", test_cases)
# print(TestSuite.to_xml_string([ts]))


