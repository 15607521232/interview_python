#coding=utf-8


import unittest

class FirstCase(unittest.TestCase):



    @classmethod
    def setUpClass(cls) -> None:
        print("这是所有case的前置")

    @classmethod
    def tearDownClass(cls) -> None:
        print("这是所有case的后置")


    def setUp(self) -> None:
        print("这是case的前置条件")


    def tearDown(self) -> None:
        print("这是case的后置条件")


    def testcase01(self):
        print("这是第一条case")


    def testcase02(self):
        print("这是第二条case")

    @unittest.skip("不执行第三条")
    def testcase03(self):
        print("这是第三条case")





if __name__ == '__main__':
    # fc = FirstCase()
    # fc.testcase01()
    # fc.testcase02()
    # unittest.main()


    #容器
    suite = unittest.TestSuite()
    suite.addTest(FirstCase('testcase02'))
    suite.addTest(FirstCase('testcase01'))
    suite.addTest(FirstCase('testcase03'))
    unittest.TextTestRunner().run(suite)