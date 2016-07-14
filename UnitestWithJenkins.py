import unittest,time
from junit_xml import TestSuite, TestCase
import urllib2
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def NV_LOG_IN_OUT(nv_url,user,password):
    driver = webdriver.Firefox()
    driver.get(nv_url)
    driver.find_element_by_name('username').send_keys(user)
    print 'User form filled'
    time.sleep(5)
    driver.find_element_by_name('password').send_keys(password)
    print 'Password form filled'
    time.sleep(5)
    driver.find_element_by_id('loginButton').click()
    print 'logIn Clicked'
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="userDropdownWrapper"]/img[3]').click()
    print 'User dropdown clicked'
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="logoutButton"]').click()
    print 'LogOut done'
    time.sleep(5)
    #driver.quit()

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



test_cases = [TestCase('YnetTest',MyTest,10)]
ts = TestSuite("my test suite", test_cases)

#print(TestSuite.to_xml_string([ts]))


