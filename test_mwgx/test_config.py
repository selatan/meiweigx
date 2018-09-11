# -*- coding: utf-8 -*-

from appium import webdriver
import appium
import time
import unittest
from test_mwgx import test_login


# ————安装并启动app进首页————success——

class SetConfig(unittest.TestCase):

    # tearDown（）方法用于测试用例执行之后的善后工作。如关闭数据库连接，退出应用。
    # 无论这个方法写在哪里，都是最后才执行
    # def tearDown(self):  #退出程序
    #     self.driver.quit()

    def test_install_open(self):
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
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

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
        time.sleep(1)
        # 滑动引导页，x、y分别是起点和终点坐标，duration是滑动时间
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
        # 点击首页弹窗右上角的x按钮
        self.driver.find_element_by_id('com.meiweigx.customer:id/first_view_closeBtn').click()

        # 一个断言（0是热销商品，1是新品推荐，2是特价促销，以此类推）
        a = self.driver.find_elements_by_id("com.meiweigx.customer:id/sub_menu_title")[0].text
        # print(a)
        # 热销商品不等于a时，打印出“没有找到热销商品”的信息，等于则不打印
        self.assertEqual("热销商品", a, "没有找到热销商品")

        # ————找到“com.meiweigx.customer:id/sub_menu_title”对应的一组元素的text内容并打印出来————
        # for i in range(5):
        #     l = self.driver.find_elements_by_id('com.meiweigx.customer:id/sub_menu_title')[i].text
        #     print("下标 %d 对应的栏目是 %s."%(i,l))
        #     print(i)
        #     print(l)


if __name__ == '__main__':
    # # 构造测试集  defaultTestLoader（）即TestLoader（）测试用例加载器，包括多个加载测试用例的方法，返回一个测试套件
    # # loadTestsFromTestCase（）根据给定的测试类，获取其中的所有测试方法，并返回一个测试套件
    # suite = unittest.TestLoader.loadTestsFromTestCase(SetConfig)
    #
    # # unittest框架的TextTestRunner（）类，通过该类下面的run（）方法来运行suite所组装的测试用例，入参为suite测试套件
    # unittest.TextTestRunner(verbosity=2).run(suite)

    # 上面两行代码可以换成下面一行
    unittest.main()
