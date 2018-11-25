"""Application Level File
Pytest Framework"""
import os
import sys
basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# encoding=utf8
reload(sys)
sys.setdefaultencoding('utf8')
import csv
import json
import re
import time
import logging
from robot.libraries.BuiltIn import BuiltIn as BI
from BIN.GenericUIFunction import GenericUIFunction


logging.basicConfig(format="%(levelname)s:%(name)s:%(message)s",level=logging.DEBUG)

fileDir = os.path.dirname(os.path.realpath('__file__'))
print fileDir
filename = os.path.join(fileDir, '../CONFIG/commonconfig.json')
with open(filename,"r") as f:
    config_json = json.load(f)

filenamedata = os.path.join(fileDir, '../DATA/Test_data_file.json')
with open(filenamedata,"r") as u:
    data_json = json.load(u)

filewrite = os.path.join(fileDir, '../DATA/alldata.csv')



class test_quickfuseapps(GenericUIFunction):

    def __init__(self):
        self.builtin = BI()

    def get_webdriver_instance(self):
        self.sel = self.builtin.get_library_instance("Selenium2Library")
        return self.sel._current_browser()

    def test_getting_reviews_in_excel(self):


        try:
            length = 0
            list = []
            listappend = []
            self.WaitUntilElementFound(config_json["XPATHFIRSTPAGE"]["reviewthisproduct"])
            self.move_to_element(config_json["XPATHFIRSTPAGE"]["reviewthisproduct"])
            while True:
                elems = self.driver.find_elements_by_xpath(config_json["XPATHFIRSTPAGE"]["show_more_reviews"])
                if len(elems) > 0 and elems[0].is_displayed():
                    self.WaitUntilElementFound(config_json["XPATHFIRSTPAGE"]["show_more_reviews"])
                    self.ClickElement(config_json["XPATHFIRSTPAGE"]["show_more_reviews"])
                    time.sleep(8)
                    print("FOUND THE LINK CREATE ACTIVITY! and Clicked it!")
                else:
                    print ("NO LINK FOUND")
                    break
            time.sleep(10)
            self.WaitUntilElementFound(config_json['XPATHFIRSTPAGE']['Iterator']) #iterator
            print "find len"
            length=self.get_matching_xpathcount(config_json['XPATHFIRSTPAGE']['MatchXpathcount']) #matchxpathcount
            print "len {}".format(length)
            replace_string_firstcell=config_json['XPATHFIRSTPAGE']['Reviewer'] #Reviewer
            replace_string_secondcell=config_json['XPATHFIRSTPAGE']['overall'] #overall
            replace_string_thirdcell=config_json['XPATHFIRSTPAGE']['summary'] #summary
            replace_string_fourthcell=config_json['XPATHFIRSTPAGE']['likelihood'] #likelihood
            replace_string_seventhcell=config_json['XPATHFIRSTPAGE']['Pros_Cons']#proscons
            for i in range(1,5):
                print i
                list=[]
                replace1 = re.sub("~", str(i), replace_string_firstcell)
                GetEelem1 = str(self.getTextUIElement(replace1))
                list.append(GetEelem1)

                replace2 = re.sub("~", str(i), replace_string_secondcell)
                GetEelem2 = str(self.getTextUIElement(replace2))
                list.append(GetEelem2)

                replace3 = re.sub("~", str(i), replace_string_thirdcell)
                GetEelem3 = str(self.getTextUIElement(replace3))
                list.append(GetEelem3)

                replace4 = re.sub("~", str(i), replace_string_fourthcell)
                GetEelem4 = str(self.getTextUIElement(replace4))




                result = GetEelem4.find("Recommend")
                print result
                if result != -1:
                    string=config_json['XPATHFIRSTPAGE']['Recommend']#recommend
                    replace=re.sub("~",str(i),string)
                    findelem=self.driver.find_element_by_xpath(replace)
                    value=findelem.get_attribute("alt")
                    list.append(value)
                else:
                    value="NA"
                    list.append(value)

                replace7 = re.sub("~", str(i), replace_string_seventhcell)
                GetEelem7 = str(self.getTextUIElement(replace7))
                list.append(GetEelem7)

                listappend.append(list)
            print listappend
            with open(filewrite, 'a') as outcsv:
                writer = csv.writer(outcsv)
                writer.writerow(['customer Details', 'Overall Ratings', 'summary', 'Likelihood', 'pros and cons'])
                for item in listappend:
                    writer.writerow([item[0], item[1], item[2], item[3], item[4]])
            time.sleep(10)
        except Exception,e:
            print "Exception is  {}".format(e)
            time.sleep(10)






