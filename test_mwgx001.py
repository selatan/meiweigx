# -*-coding:utf-8-*-
from appium import webdriver
import time
import uiautomator2
import unittest


class Mytest(unittest.TestCase):  # 继承unittest.TestCase
    def tearDown(self):
        print('用例执行后')  # 每个测试用例执行之后做该操作

    def setUp(self):
        print('用例执行前')  # 每个测试用例执行之前做该操作

    def test_setUp(self):
        desired_caps = {}
        desired_caps['automationName'] = 'UiAutomator2'  # 7.0以下系统需要把这一行注释掉
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.1.1'
        desired_caps['deviceName'] = '5142c29f'  # 红色oppo5142c29f
        desired_caps['appPackage'] = 'com.meiweigx.customer'
        desired_caps['appActivity'] = 'com.meiweigx.customer.ui.LaunchActivity'
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

        driver.find_element_by_id('com.android.packageinstaller:id/do_not_ask_checkbox').click()  # 点击“不允许后不再访问”
        time.sleep(2)
        driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()  # 点击始终允许


time.sleep(2)
driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()  # 第二个弹框点击始终允许
time.sleep(2)
driver.find_element_by_id('com.android.packageinstaller:id/do_not_ask_checkbox').click()  # 点击“不允许后不再访问”
time.sleep(2)
driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()  # 第三个弹框点击始终允许
time.sleep(2)

driver.swipe(start_x=1000, start_y=1000, end_x=200, end_y=1000, duration=800)
time.sleep(2)
driver.swipe(start_x=1000, start_y=1000, end_x=200, end_y=1000, duration=800)
time.sleep(2)
driver.swipe(start_x=1000, start_y=1000, end_x=200, end_y=1000, duration=800)
time.sleep(5)
driver.find_element_by_xpath('//android.widget.Button[@resource-id=\"com.meiweigx.customer:id/btn\"]').click()
# driver.find_element_by_id("com.meiweigx.customer:id/btn").click()
# driver.find_element_by_name('立即体验').click()
# driver.find_element_by_id('com.meiweigx.customer:id/btn').click()
# driver.find_element_by_class_name('android.widget.Button').click()
# driver.find_element_by_xpath("//android.widget.Button[@text='立即体验']").click()
# driver.find_element_by_android_uiautomator('newUiSelector().text("立即体验")').click()
# driver.tap([(225,1641),(855,1776),100])
time.sleep(2)
# driver.find_element_by_id('com.meiweigx.customer:id/edit_search').click()#点击搜索框
# time.sleep(2)
driver.quit()

if __name__ == '__main__':
    unittest.main()
