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

import logging


from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import re
import os
from selenium.webdriver.support.ui import Select
import time


from robot.libraries.BuiltIn import BuiltIn as BI



logging.basicConfig(format="%(levelname)s:%(name)s:%(message)s",level=logging.DEBUG)


with open(basedir + "/CONFIG/commonconfig.json","r") as f, open(basedir + "/DATA/Test_data_file.json") as u:
    config_json = json.load(f)
    data_json = json.load(u)
print config_json
print data_json


filewrite = os.path.join(basedir + '/DATA/alldata.csv')



class DataCollection():
    def __init__(self):
        self.builtin = BI()

    def get_webdriver_instance(self):
        self.sel = self.builtin.get_library_instance("Selenium2Library")
        return self.sel._current_browser()

    def ClickElement(self, driver, locator):
        ClickElement = driver.find_element_by_xpath(locator)
        ClickElement.click()

    def WaitUntilElementFound(self, driver, locator):
        timeout = 30
        element_present = EC.presence_of_element_located((By.XPATH, locator))
        WebDriverWait(driver, timeout).until(element_present)

    def InputElement(self, driver, locator, text):
        password = driver.find_element_by_xpath(locator)
        password.send_keys(text)

    def getTextUIElement(self, driver,locator):
        landingpage = driver.find_element_by_xpath(locator)
        welcometxt = landingpage.text
        return welcometxt

    def mouse_over(self, driver,locator):
        element_to_hover_over = driver.find_element_by_xpath(locator)
        hover = ActionChains(driver).move_to_element(element_to_hover_over)
        hover.perform()

    def get_matching_xpathcount(self, driver, locator):
        matching_count = driver.find_elements_by_xpath(locator)
        len_match_count = len(matching_count) + 1
        return len_match_count

    def SelectElement(self, driver, locator, text):
        Select_element = Select(driver.find_element_by_xpath(locator))
        Select_element.select_by_visible_text(text)

    def drag_and_drop_Element(self, driver, locator_source, locator_destination):
        actionchains = ActionChains(driver)
        draggable = driver.find_element_by_xpath(locator_source)
        droppable = driver.find_element_by_xpath(locator_destination)
        time.sleep(6)
        actionchains.drag_and_drop(draggable, droppable).perform()

    def drag_and_drop_Element_by_offset(self, driver, locator_source, locator_destination_xoffset,
                                        locator_destination_yoffset):
        actionchains = ActionChains(driver)
        draggable = driver.find_element_by_xpath(locator_source)
        time.sleep(6)
        actionchains.drag_and_drop_by_offset(draggable, locator_destination_xoffset,
                                             locator_destination_yoffset).perform()

    def drag_and_drop_Element_by_offset_click(self, driver, locator_source, locator_destination_xoffset,
                                              locator_destination_yoffset):
        actionchains = ActionChains(driver)
        draggable = driver.find_element_by_xpath(locator_source)
        time.sleep(6)
        actionchains.context_click(draggable)
        time.sleep(2)
        actionchains.drag_and_drop_by_offset(draggable, locator_destination_xoffset,
                                             locator_destination_yoffset).perform()

    def get_dropdown_values(self, driver, matchingLocator, incrementLocator):
        list = []
        len_match_count = self.get_matching_xpathcount(matchingLocator)
        replace_string = incrementLocator
        for i in range(1, len_match_count):
            replace = re.sub("~", str(i), replace_string)
            GetEelem = self.getTextUIElement(replace)
            print GetEelem
            list.append(GetEelem)
        print list
        return list

    def move_to_element(self, driver, locator):
        element = driver.find_element_by_xpath(locator)
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()

    def click_specific_dropdown_value(self, driver, matchingLocator, incrementLocator, UItext):
        list = []
        len_match_count = self.get_matching_xpathcount(matchingLocator)
        replace_string = incrementLocator
        for i in range(1, len_match_count):
            replace = re.sub("~", str(i), replace_string)
            GetEelem = self.getTextUIElement(replace)
            print "GetEelem {}, UItext {}".format(GetEelem, UItext)
            if GetEelem == UItext:
                self.ClickElement(replace)
                print "Successfully Clicked the Element {}".format(GetEelem)
                break

    def getting_reviews_in_excel(self,driver):


        try:
            length = 0
            list = []
            listappend = []
            self.WaitUntilElementFound(driver,config_json["XPATHFIRSTPAGE"]["reviewthisproduct"])
            self.move_to_element(driver,config_json["XPATHFIRSTPAGE"]["reviewthisproduct"])
            while True:

                elems = driver.find_elements_by_xpath(config_json["XPATHFIRSTPAGE"]["show_more_reviews"])
                if len(elems) > 0 and elems[0].is_displayed():
                    self.WaitUntilElementFound(driver,config_json["XPATHFIRSTPAGE"]["show_more_reviews"])
                    self.ClickElement(driver,config_json["XPATHFIRSTPAGE"]["show_more_reviews"])
                    time.sleep(8)
                    print("FOUND THE LINK CREATE ACTIVITY! and Clicked it!")
                else:
                    print ("NO LINK FOUND")
                    break
            time.sleep(10)
            self.WaitUntilElementFound(driver,config_json['XPATHFIRSTPAGE']['Iterator']) #iterator
            print "find len"
            length=self.get_matching_xpathcount(driver,config_json['XPATHFIRSTPAGE']['MatchXpathcount']) #matchxpathcount
            print "len {}".format(length)
            replace_string_firstcell=config_json['XPATHFIRSTPAGE']['Reviewer'] #Reviewer
            replace_string_secondcell=config_json['XPATHFIRSTPAGE']['overall'] #overall
            replace_string_thirdcell=config_json['XPATHFIRSTPAGE']['summary'] #summary
            replace_string_fourthcell=config_json['XPATHFIRSTPAGE']['likelihood'] #likelihood
            replace_string_seventhcell=config_json['XPATHFIRSTPAGE']['Pros_Cons']#proscons
            for i in range(1,length-1):
                print i
                list=[]
                replace1 = re.sub("~", str(i), replace_string_firstcell)
                GetEelem1 = str(self.getTextUIElement(driver,replace1))
                list.append(GetEelem1)

                replace2 = re.sub("~", str(i), replace_string_secondcell)
                GetEelem2 = str(self.getTextUIElement(driver,replace2))
                list.append(GetEelem2)

                replace3 = re.sub("~", str(i), replace_string_thirdcell)
                GetEelem3 = str(self.getTextUIElement(driver,replace3))
                list.append(GetEelem3)

                replace4 = re.sub("~", str(i), replace_string_fourthcell)
                GetEelem4 = str(self.getTextUIElement(driver,replace4))




                result = GetEelem4.find("Recommend")
                print result
                if result != -1:
                    string=config_json['XPATHFIRSTPAGE']['Recommend']#recommend
                    replace=re.sub("~",str(i),string)
                    findelem=driver.find_element_by_xpath(replace)
                    value=findelem.get_attribute("alt")
                    list.append(value)
                else:
                    value="NA"
                    list.append(value)

                replace7 = re.sub("~", str(i), replace_string_seventhcell)
                GetEelem7 = str(self.getTextUIElement(driver,replace7))
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






