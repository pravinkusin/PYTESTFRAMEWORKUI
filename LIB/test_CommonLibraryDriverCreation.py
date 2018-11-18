#common library File for suite login and tear down

import unittest
from selenium import webdriver
import os
import json

fileDir = os.path.dirname(os.path.realpath('__file__'))
print fileDir
filename = os.path.join(fileDir, '../CONFIG/commonconfig.json')
with open(filename,"r") as f:
    config_json = json.load(f)

class test_CommonLibraryDriverCreation(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(config_json["UIDetails"]["quickfuseapps"])
        self.driver.maximize_window()


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()