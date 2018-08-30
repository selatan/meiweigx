# -*- coding:utf-8 -*-

# 登录
from appium import webdriver
import time
import os
import unittest
from test_mwgx import test_mwgx_001


class test_calss_02(unittest.TestCase):
    a = test_mwgx_001.test_class_01().driver

    # 未登录时跳转到登录页
    def test_02_gotologin(self):
        self.a.driver.find_element_by_xpath(
            '//android.widget.TextView[@text="我的"]').click()

    def test_03_login(self):
        self.a.driver.find_element_by_id('com.meiweigx.customer:id/edit_username').set_value('18583688372')
        # 正式环境账号密码
        self.a.driver.find_element_by_id('com.meiweigx.customer:id/edit_pwd').set_value('camera3600')
        # 测试环境账号密码
        self.a.driver.find_element_by_id('com.meiweigx.customer:id/edit_pwd').set_value('test123')
        self.a.driver.find_element_by_id('com.meiweigx.customer:id/btn_login').click()

    if __name__ == "__main__":
        # 此方法可以同时测试多个类
        suite1 = unittest.TestLoader().loadTestsFromTestCase(test_mwgx_001.test_class_01)
        suite2 = unittest.TestLoader().loadTestsFromTestCase(test_mwgx_002.test_class_02)
        suite = unittest.TestSuite([suite1, suite2])
        unittest.TextTestRunner(verbosity=2).run(suite)
