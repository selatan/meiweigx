# -*- coding: utf-8 -*-

from appium import webdriver
import appium
import time
import unittest
from test_mwgx import test_config


# ————启动app并登录,进入“我的”页面————success————

# TestCase类，所有测试用例类 继承的基本类
class LoginTest(unittest.TestCase):

    # setUp（）方法用于测试用例执行前的初始化工作。如测试用例中需要访问数据库，可以在setUp中建立数据库链接
    # 并进行初始化。如测试用例需要启动Appium服务，则需要在该方法内启动Appium服务。
    #

    # tearDown（）方法用于测试用例执行之后的善后工作。如关闭数据库连接，退出应用。
    # 无论这个方法写在哪里，都是最后才执行
    # def tearDown(self):
    #     self.driver.quit()

    # 具体的测试用例，必须要以test开头
    def test_login(self):

        # 实例化
        a = test_config.SetConfig.test_install_open(self)

        time.sleep(2)

        # 点击“我的”
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
