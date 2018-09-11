# -*- coding: utf-8 -*-

from appium import webdriver
import appium
import time
import unittest
from test_mwgx import test_login

# ————登录并加入购物车提交————success——

caps = {}
# Android7.0及以上系统需要加下面这一行参数
caps['automationName'] = 'UiAutomator2'
caps["platformName"] = "android"
caps["deviceName"] = "5142c29f"
caps["app"] = "C:\\Users\Administrator\Desktop\meiweigx.apk"
caps["platformVersion"] = "7.1.1"
caps['appPackage'] = 'com.meiweigx.customer'
caps['appActivity'] = 'com.meiweigx.customer.ui.LaunchActivity'
caps["moReset"] = True


# TestCase类，所有测试用例类 继承的基本类
class BuyTest(unittest.TestCase):

    # setUp（）方法用于测试用例执行前的初始化工作。如测试用例中需要访问数据库，可以在setUp中建立数据库链接
    # 并进行初始化。如测试用例需要启动Appium服务，则需要在该方法内启动Appium服务。
    def setUp(self):
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

    # tearDown（）方法用于测试用例执行之后的善后工作。如关闭数据库连接，退出应用。
    # 无论这个方法写在哪里，都是最后才执行
    # def tearDown(self):
    #     self.driver.quit()

    # 具体的测试用例，必须要以test开头
    def test_buy(self):
        # ★★★★★实例化test_login.py文件中LoginTest类的test_start()方法，进行启动、登录操作★★★★★
        a = test_login.LoginTest.test_start(self)
        time.sleep(2)

        # 点击“商城购物”
        self.driver.find_elements_by_id("com.meiweigx.customer:id/layout_tab_img")[2].click()
        time.sleep(1)

        # #点击搜索输入框并输入要搜索的内容，后面的搜索按钮不知道怎么定位了
        # inp = self.driver.find_element_by_xpath("//android.widget.TextView[@text='搜索食材']")
        # inp.click()
        # inp.send_keys('米')

        # 点击“伴手好礼”
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='伴手好礼']").click()
        time.sleep(1)

        # 点击第一个商品后的购物车按钮
        self.driver.find_elements_by_id("com.meiweigx.customer:id/btn_add")[0].click()
        time.sleep(1)

        # 点击第二个商品后的购物车按钮
        # self.driver.find_elements_by_id("com.meiweigx.customer:id/btn_add")[1].click()
        time.sleep(1)

        # 点击购物车按钮
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='购物车']").click()
        time.sleep(1)

        # 点击“结算”按钮
        self.driver.find_element_by_id("com.meiweigx.customer:id/text_pay").click()
        time.sleep(1)

        # 点击“提交订单“
        self.driver.find_element_by_id("com.meiweigx.customer:id/btn_buy").click()

        # ……


if __name__ == '__main__':
    unittest.main()
