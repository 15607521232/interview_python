#coding=utf-8
from mock import mock
import unittest
import requests
import HtmlTestRunner

class UnittestDemo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("这是所有内容的前提条件")

    def setUp(self):
        print("这是每个用例的前提条件")
    @classmethod
    def tearDownClass(cls):
        print("这是所有内容的后置条件")

    def tearDown(self):
        print("这是每个用例的后置条件")

    def func_data(self):
        data_dict = {
            "name":"liguang",
            "age":"16"
        }
        return data_dict


    def test_cast1(self):
        
        data_j = {
            "name":"mock",
            "version":"0.0.1"
        }
        mock_data = mock.Mock(return_value=data_j)
        print(mock_data)
        requests.get = mock_data
        data = requests.get("http://127.0.0.1:5000/index")
        print(data)

        
        # status_data = data.status_code
        # print(data.json())
        # print(type(status_data))
        self.assertEqual(data['name'],"mock","接口请求成功")



if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(UnittestDemo('test_cast1'))
    # unittest.TextTestRunner().run(suite)
    runner = HtmlTestRunner.HTMLTestRunner(output="../reports/",report_name="case_report",open_in_browser=True,report_title="Interface_Test")
    runner.run(suite)
        
