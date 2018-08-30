# -*- coding:utf-8 -*-

# 安装app并启动进首页
from appium import webdriver
import time
import os
import unittest

# import HTMLTestRunner


PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))


class test_class_01(unittest.TestCase):  # 继承unittest.TestCase
    def setUp(self):
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
        time.sleep(2)

    # def tearDown(self):
    #     self.driver.close_app()
    #     self.driver.quit()
    #     print('————————用例执行后')  # 每个测试用例执行之后做该操作

    def test_1_start(self):
        # 点击“不允许后不再访问”
        self.driver.find_element_by_id('com.android.packageinstaller:id/do_not_ask_checkbox').click()
        # 点击始终允许
        self.driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
        # 第二个弹框点击始终允许
        self.driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
        # 点击“不允许后不再访问”
        self.driver.find_element_by_id('com.android.packageinstaller:id/do_not_ask_checkbox').click()
        # 第三个弹框点击始终允许
        self.driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
        time.sleep(2)
        self.driver.swipe(start_x=1000, start_y=1000, end_x=200, end_y=1000, duration=800)
        time.sleep(2)
        self.driver.swipe(start_x=1000, start_y=1000, end_x=200, end_y=1000, duration=800)
        time.sleep(2)
        self.driver.swipe(start_x=1000, start_y=1000, end_x=200, end_y=1000, duration=800)
        time.sleep(2)
        # 点击“立即体验”
        self.driver.find_element_by_xpath(
            '//android.widget.Button[@resource-id=\"com.meiweigx.customer:id/btn\"]').click()
        time.sleep(5)

        # 点击“我的”
        # self.driver.find_element_by_xpath(
        #     '//android.widget.TextView[@text="我的"]').click()

        # self.driver.find_element_by_id('com.meiweigx.customer:id/edit_search').click()#点击搜索框
        print('已执行完test_1_start')
        time.sleep(5)

    # def test_exit(self):
    #     self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestLoader.loadTestsFromTestCase(test_class_01)
    unittest.TextTestRunner(verbosity=2).run(suite)
    # unittest.main()
