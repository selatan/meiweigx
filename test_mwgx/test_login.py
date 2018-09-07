# -*- coding: utf-8 -*-

from appium import webdriver
import appium
import time
import unittest

# ————启动app并登录————success————

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
class LoginTest(unittest.TestCase):

    # setUp（）方法用于测试用例执行前的初始化工作。如测试用例中需要访问数据库，可以在setUp中建立数据库链接
    # 并进行初始化。如测试用例需要启动Appium服务，则需要在该方法内启动Appium服务。
    def setUp(self):
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

    # tearDown（）方法用于测试用例执行之后的善后工作。如关闭数据库连接，退出应用。
    # 无论这个方法写在哪里，都是最后才执行
    # def tearDown(self):
    #     self.driver.quit()

    # 具体的测试用例，必须要以test开头
    def test_start(self):
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
        # 滑动引导页，x、y分别是起点和终点坐标，duration是滑动时间
        self.driver.swipe(start_x=1000, start_y=1000, end_x=200, end_y=1000, duration=800)
        time.sleep(2)
        self.driver.swipe(start_x=1000, start_y=1000, end_x=200, end_y=1000, duration=800)
        time.sleep(2)
        self.driver.swipe(start_x=1000, start_y=1000, end_x=200, end_y=1000, duration=800)
        time.sleep(2)
        # 点击“立即体验”
        self.driver.find_element_by_xpath(
            '//android.widget.Button[@resource-id=\"com.meiweigx.customer:id/btn\"]').click()
        time.sleep(1)
        # 点击首页弹窗右上角的x按钮
        self.driver.find_element_by_id('com.meiweigx.customer:id/first_view_closeBtn').click()

        self.driver.find_element_by_xpath("//android.widget.TextView[@text='我的']").click()

        inp1 = self.driver.find_element_by_id("com.meiweigx.customer:id/edit_username")
        inp1.click()
        inp1.send_keys('18583688372')
        inp2 = self.driver.find_element_by_id("com.meiweigx.customer:id/edit_pwd")
        inp2.click()
        inp2.send_keys('123test')  #测试环境的登录密码
        # 点击登录按钮
        self.driver.find_element_by_id("com.meiweigx.customer:id/btn_login").click()
        time.sleep(1)

        # 获取登录后的昵称
        name = self.driver.find_element_by_id('com.meiweigx.customer:id/tv_username').text
        #print(name)
        try:
            assert "测试专用账号" in name
            # print("恭喜，登录成功~~~")
        except AssertionError as e:
            print("哦豁，登录失败~~~")


if __name__ == '__main__':
    # 构造测试集  defaultTestLoader（）即TestLoader（）测试用例加载器，包括多个加载测试用例的方法，返回一个测试套件
    # loadTestsFromTestCase（）根据给定的测试类，获取其中的所有测试方法，并返回一个测试套件
    suite = unittest.TestLoader.loadTestsFromTestCase(LoginTest)

    # unittest框架的TextTestRunner（）类，通过该类下面的run（）方法来运行suite所组装的测试用例，入参为suite测试套件
    unittest.TextTestRunner(verbosity=2).run(suite)

    # 上面两行代码可以换成下面一行
    # unittest.main()
