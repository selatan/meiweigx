# ————合并test_login.py和test_openapp.py文件进行执行————success——

import unittest
from test_mwgx import test_openapp
from test_mwgx import test_login

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(test_openapp.OpenApp))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(test_login.LoginTest))

    # 这一步是在当前文件夹里自动生成一个测试报告，测试报告名称就叫：UnittestTextReport.txt.
with open('./UnittestTextReport.txt', 'a') as f:
    runner = unittest.TextTestRunner(stream=f, verbosity=2)
    runner.run(suite)
