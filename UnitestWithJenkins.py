import time,unittest
from junit_xml import TestSuite, TestCase
import urllib2
from selenium import webdriver
from Params import *

from selenium.webdriver.common.keys import Keys

def NV_LOG_IN_OUT(nv_url,user,password):
    print 'log in out'
    try:
        driver = webdriver.Firefox()
        driver.get(nv_url)
        driver.find_element_by_name('username').send_keys(user)
        time.sleep(2)
        driver.find_element_by_name('password').send_keys(password)
        time.sleep(2)
        driver.find_element_by_id('loginButton').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="userDropdownWrapper"]/img[3]').click()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="logoutButton"]').click()
        time.sleep(5)
        driver.quit()
        return True
    except Exception,e:
        print e
        try:
            driver.quit()
        except:
            pass
        return False

def GET_YNET():
    print 'ynet'
    response = urllib2.urlopen('http://ynet.co.il')
    html = response.read()
    if 'ynet' in html.lower():
        return True
    else:
        return False





#test_cases = [TestCase('NV_UI_Testing',NV_Tests,10)]
#ts = TestSuite("my test suite", test_cases)

#print(TestSuite.to_xml_string([ts]))


