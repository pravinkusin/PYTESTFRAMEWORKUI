"""Application Level File
Pytest Framework"""

import json
import unittest
from LIB.test_CommonLibraryDriverCreation import test_CommonLibraryDriverCreation
from BIN.GenericUIFunction import GenericUIFunction
import os
import pytest
import sys
import time

fileDir = os.path.dirname(os.path.realpath('__file__'))
print fileDir
filename = os.path.join(fileDir, '../CONFIG/commonconfig.json')
with open(filename,"r") as f:
    config_json = json.load(f)

filenamedata = os.path.join(fileDir, '../DATA/Test_data_file.json')
with open(filenamedata,"r") as u:
    data_json = json.load(u)


class test_quickfuseapps(test_CommonLibraryDriverCreation,unittest.TestCase,GenericUIFunction):
    def test_creation_of_SMTP_Messaging_App(self):
        try:
            #Creating the workflow of application

            self.ClickElement(config_json["XPATHFIRSTPAGE"]["create_an_app"])
            self.WaitUntilElementFound(config_json["XPATHFIRSTPAGE"]["Lets_Get_Started"])
            self.ClickElement(config_json["XPATHFIRSTPAGE"]["Lets_Get_Started"])
            self.WaitUntilElementFound(config_json["XPATHFIRSTPAGE"]["New_Page"])
            self.ClickElement(config_json["XPATHFIRSTPAGE"]["New_Page"])
            self.WaitUntilElementFound(config_json["XPATHFIRSTPAGE"]["Enter_New_Page"])
            self.InputElement(config_json["XPATHFIRSTPAGE"]["Enter_New_Page"],"test")
            self.ClickElement(config_json["XPATHFIRSTPAGE"]["Create_button"])
            self.WaitUntilElementFound(config_json["XPATHFIRSTPAGE"]["Messaging"])
            self.ClickElement(config_json["XPATHFIRSTPAGE"]["Messaging"])
            self.WaitUntilElementFound(config_json["XPATHFIRSTPAGE"]["Send_an_SMS"])
            self.drag_and_drop_Element(config_json["XPATHFIRSTPAGE"]["Send_an_SMS"],config_json["XPATHFIRSTPAGE"]["workflow_page"])
            time.sleep(5)
            self.WaitUntilElementFound(config_json["XPATHFIRSTPAGE"]["Start_Sender"])
            self.drag_and_drop_Element(config_json["XPATHFIRSTPAGE"]["Start_Sender"],config_json["XPATHFIRSTPAGE"]["Send_an_sms_reciever"])
            self.WaitUntilElementFound(config_json["XPATHFIRSTPAGE"]["Send_an_email"])
            time.sleep(5)
            self.drag_and_drop_Element(config_json["XPATHFIRSTPAGE"]["Send_an_email"],config_json["XPATHFIRSTPAGE"]["workflow_page"])
            time.sleep(5)
            self.WaitUntilElementFound(config_json["XPATHFIRSTPAGE"]["Basic"])
            self.ClickElement(config_json["XPATHFIRSTPAGE"]["Basic"])
            self.ClickElement(config_json["XPATHFIRSTPAGE"]["Hangup_Exit"])
            self.drag_and_drop_Element_by_offset(config_json["XPATHFIRSTPAGE"]["Send_an_email_workflow"],350,0)
            self.drag_and_drop_Element_by_offset(config_json["XPATHFIRSTPAGE"]["Hangup_Exit_Drag"],-200,+200)
            self.ClickElement(config_json["XPATHFIRSTPAGE"]["Hangup_Exit"])
            self.drag_and_drop_Element_by_offset(config_json["XPATHFIRSTPAGE"]["Hangup_Exit_Drag1"],610,280)
            self.ClickElement(config_json["XPATHFIRSTPAGE"]["Hangup_Exit"])
            self.drag_and_drop_Element_by_offset(config_json["XPATHFIRSTPAGE"]["Hangup_Exit_Drag2"],0,+300)
            self.drag_and_drop_Element(config_json["XPATHFIRSTPAGE"]["Send_sms_module2_left"],config_json["XPATHFIRSTPAGE"]["Exit_app_module4"])
            self.drag_and_drop_Element(config_json["XPATHFIRSTPAGE"]["Send_sms_module2_right"],config_json["XPATHFIRSTPAGE"]["send_email_reciever"])
            self.drag_and_drop_Element(config_json["XPATHFIRSTPAGE"]["Send_email_module2_left"],config_json["XPATHFIRSTPAGE"]["Exit_app_module6"])
            self.drag_and_drop_Element(config_json["XPATHFIRSTPAGE"]["Send_email_module2_right"],config_json["XPATHFIRSTPAGE"]["Exit_app_module5"])

            #Adding the test Data in all the fields

            self.InputElement(config_json["XPATHFIRSTPAGE"]["send_an_sms_text_input"],data_json["TestData"]["send_an_sms_text_input"])
            self.InputElement(config_json["XPATHFIRSTPAGE"]["send_an_sms_phone_input_message"],data_json["TestData"]["send_an_sms_phone_input_message"])
            self.InputElement(config_json["XPATHFIRSTPAGE"]["send_an_email_smtp_url"],data_json["TestData"]["send_an_email_smtp_url"])
            self.InputElement(config_json["XPATHFIRSTPAGE"]["send_an_email_port"],data_json["TestData"]["send_an_email_port"])
            self.ClickElement(config_json["XPATHFIRSTPAGE"]["send_an_email_ssl"])
            self.InputElement(config_json["XPATHFIRSTPAGE"]["send_an_email_username"],data_json["TestData"]["send_an_email_username"])
            self.InputElement(config_json["XPATHFIRSTPAGE"]["send_an_email_password"],data_json["TestData"]["send_an_email_password"])
            self.InputElement(config_json["XPATHFIRSTPAGE"]["send_an_email_from"],data_json["TestData"]["send_an_email_from"])
            self.InputElement(config_json["XPATHFIRSTPAGE"]["send_an_email_to"],data_json["TestData"]["send_an_email_to"])
            self.InputElement(config_json["XPATHFIRSTPAGE"]["send_an_email_subject"],data_json["TestData"]["send_an_email_subject"])
            self.InputElement(config_json["XPATHFIRSTPAGE"]["send_an_email_input_message"],data_json["TestData"]["send_an_email_input_message"])

            time.sleep(10) #just to check screen for final result

        except Exception,e:
            print "ERROR {}".format(e)
            raise Exception



if __name__ == "__main__":
    unittest.main()





