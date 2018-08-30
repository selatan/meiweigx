# -*- coding:utf-8 -*-

from appium import webdriver
import time
import os
# import uiautomator2
import unittest

#import HTMLTestRunner
PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))


class mytest(unittest.TestCase):  # 继承unittest.TestCase
    def tearDown(self):
        print('————————用例执行后')  # 每个测试用例执行之后做该操作

    def setUp(self):
        print('————————用例执行前')  # 每个测试用例执行之前做该操作

    def test_info(self):
        desired_caps = {}
        # 7.0以下系统需要把这一行注释掉
        desired_caps['automationName'] = 'UiAutomator2'
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.1.1'
        desired_caps['deviceName'] = '5142c29f'  # 红色oppo5142c29f
        # apk包的路径
        desired_caps['app'] = PATH(r'C:\Users\Administrator\Desktop\meiweigx.apk')
        desired_caps['appPackage'] = 'com.meiweigx.customer'
        desired_caps['appActivity'] = 'com.meiweigx.customer.ui.LaunchActivity'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        time.sleep(5)

    def test_limit(self):
        # 点击“不允许后不再访问”
        self.driver.find_element_by_id('com.android.packageinstaller:id/do_not_ask_checkbox').click()
        time.sleep(1)
        # 点击始终允许
        self.driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
        time.sleep(1)
        # 第二个弹框点击始终允许
        self.driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
        time.sleep(1)
        # 点击“不允许后不再访问”
        self.driver.find_element_by_id('com.android.packageinstaller:id/do_not_ask_checkbox').click()
        time.sleep(1)
        # 第三个弹框点击始终允许
        self.driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
        time.sleep(1)

    def test_guide(self):
        self.driver.swipe(start_x=1000, start_y=1000, end_x=200, end_y=1000, duration=800)
        time.sleep(1)
        self.driver.swipe(start_x=1000, start_y=1000, end_x=200, end_y=1000, duration=800)
        time.sleep(1)
        self.driver.swipe(start_x=1000, start_y=1000, end_x=200, end_y=1000, duration=800)
        time.sleep(1)
        # 点击“立即体验”
        self.driver.find_element_by_xpath(
            '//android.widget.Button[@resource-id=\"com.meiweigx.customer:id/btn\"]').click()
        time.sleep(1)
        # 点击搜索框
        self.driver.find_element_by_id('com.meiweigx.customer:id/edit_search').click()
        time.sleep(2)

    def test_exit(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
