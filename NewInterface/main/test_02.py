from main.main_01 import RunTest
import unittest

import os
print(os.getcwd())
class Test1(unittest.TestCase):

    def test_001(self):

        global rn
        rn = RunTest()
        return rn.go_no_run(1)

    def test_002(self):
        print("fdsafdsa")


if __name__ == '__main__':
    run = Test1()
    print(run.test_002())
