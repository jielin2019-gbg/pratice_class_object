import unittest
from HTMLTestRunner import HTMLTestRunner
import os

file_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
dir = os.path.join(file_path,"cases")
# suite = unittest.defaultTestLoader.discover('./cases','*case*.py')
suite = unittest.defaultTestLoader.discover(dir,'*case*.py')
print(suite)

file = 'HTMLreport.html'
with open(file,'wb') as f:
    runner = HTMLTestRunner(f,2,'测试报告','python 3.6.8')
    # runner = HTMLTestRunner(f)
    runner.run(suite)