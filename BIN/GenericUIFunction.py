#common library file for Generic Ui functions

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import re
from selenium.webdriver.support.ui import Select
import time

class GenericUIFunction:

    def ClickElement(self,locator):
        ClickElement = self.driver.find_element_by_xpath(locator)
        ClickElement.click()

    def WaitUntilElementFound(self,locator):
        timeout = 30
        element_present = EC.presence_of_element_located((By.XPATH, locator))
        WebDriverWait(self.driver, timeout).until(element_present)

    def InputElement(self, locator, text):
        password = self.driver.find_element_by_xpath(locator)
        password.send_keys(text)

    def getTextUIElement(self,locator):
        landingpage = self.driver.find_element_by_xpath(locator)
        welcometxt = landingpage.text
        return welcometxt

    def mouse_over(self,locator):
        element_to_hover_over = self.driver.find_element_by_xpath(locator)
        hover = ActionChains(self.driver).move_to_element(element_to_hover_over)
        hover.perform()

    def get_matching_xpathcount(self,locator):
        matching_count = self.driver.find_elements_by_xpath(locator)
        len_match_count = len(matching_count) + 1
        return len_match_count

    def SelectElement(self, locator, text):
        Select_element = Select(self.driver.find_element_by_xpath(locator))
        Select_element.select_by_visible_text(text)

    def drag_and_drop_Element(self, locator_source, locator_destination):
        actionchains = ActionChains(self.driver)
        draggable = self.driver.find_element_by_xpath(locator_source)
        droppable = self.driver.find_element_by_xpath(locator_destination)
        time.sleep(6)
        actionchains.drag_and_drop(draggable, droppable).perform()

    def drag_and_drop_Element_by_offset(self, locator_source, locator_destination_xoffset,locator_destination_yoffset):
        actionchains = ActionChains(self.driver)
        draggable = self.driver.find_element_by_xpath(locator_source)
        time.sleep(6)
        actionchains.drag_and_drop_by_offset(draggable, locator_destination_xoffset,locator_destination_yoffset).perform()

    def drag_and_drop_Element_by_offset_click(self, locator_source, locator_destination_xoffset,locator_destination_yoffset):
        actionchains = ActionChains(self.driver)
        draggable = self.driver.find_element_by_xpath(locator_source)
        time.sleep(6)
        actionchains.context_click(draggable)
        time.sleep(2)
        actionchains.drag_and_drop_by_offset(draggable, locator_destination_xoffset,locator_destination_yoffset).perform()


    def get_dropdown_values(self,matchingLocator,incrementLocator):
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

    def click_specific_dropdown_value(self,matchingLocator,incrementLocator,UItext):
        list = []
        len_match_count = self.get_matching_xpathcount(matchingLocator)
        replace_string = incrementLocator
        for i in range(1, len_match_count):
            replace = re.sub("~", str(i), replace_string)
            GetEelem = self.getTextUIElement(replace)
            print "GetEelem {}, UItext {}".format(GetEelem,UItext)
            if GetEelem == UItext:
                self.ClickElement(replace)
                print "Successfully Clicked the Element {}".format(GetEelem)
                break

    



