# coding=utf-8

""""" 运行 “.” (当前)目录下的所有测试用例，并生成HTML测试报告 """""

import unittest
from src.lib import HTMLTestReportCN


class RunAllTests(object):

    def __init__(self):
        self.test_case_path = "."
        self.title = "自动化测试报告"
        self.description = "测试报告"

    def run(self):
        test_suite = unittest.TestLoader().discover(self.test_case_path)

        # 启动测试时创建文件夹并获取报告的名字
        daf = HTMLTestReportCN.DirAndFiles()
        daf.create_dir(title=self.title)
        report_path = HTMLTestReportCN.GlobalMsg.get_value("report_path")

        fp = open(report_path, "wb")

        runner = HTMLTestReportCN.HTMLTestRunner(stream=fp, title=self.title, description=self.description, tester=input("请输入你的名字："))
        runner.run(test_suite)
        fp.close()


if __name__ == "__main__":
    RunAllTests().run()
