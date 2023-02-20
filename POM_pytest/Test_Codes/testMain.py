#testMain.py -Main Executable file
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from Test_Locators import locators
from Test_Data import data
import pytest

# ORANGE HRM
class Test_Orange:
   
   #Generator Function
    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        yield
        
   #CODE for Test case ID:TC_Login_01
        
    def test_login(self, booting_function):
       self.driver.get(data.Orange_Data().url)
       self.driver.implicitly_wait(4)
       self.driver.find_element(by=By.NAME, value=locators.Orange_Locators().username_inputBox).send_keys(data.Orange_Data().username)
       self.driver.find_element(by=By.NAME, value=locators.Orange_Locators().password_inputBox).send_keys(data.Orange_Data().password)
       self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().LoginButton).click()
       assert self.driver.title == self.driver.title
       print("SUCCESS : The user Logged in successfully with Username {a} and Password {b}". format(a=data.Orange_Data.username, b=data.Orange_Data.password))
       
   #CODE for Test case ID:TC_Login_02
       
    def test_invalid(self, booting_function):
       self.driver.get(data.Orange_Data().url)
       self.driver.implicitly_wait(4)
       self.driver.find_element(by=By.NAME, value=locators.Orange_Locators().username_inputBox).send_keys(data.Orange_Data().username1)
       self.driver.find_element(by=By.NAME, value=locators.Orange_Locators().password_inputBox).send_keys(data.Orange_Data().password1)
       self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().LoginButton).click()
       assert self.driver.title == self.driver.title
       print("SUCCESS: Invalid Credentials of Username {a} and Password {b}". format(a=data.Orange_Data.username1, b=data.Orange_Data.password1))
       
       
   #CODE for Test case ID:TC_PIM_01

    def test_employee_module(self, booting_function):
       self.driver.get(data.Orange_Data().url)
       self.driver.implicitly_wait(4)
       self.driver.find_element(by=By.NAME, value=locators.Orange_Locators().username_inputBox).send_keys(data.Orange_Data().username)
       self.driver.find_element(by=By.NAME, value=locators.Orange_Locators().password_inputBox).send_keys(data.Orange_Data().password)
       self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().LoginButton).click()
       self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().pim_button).click()
       self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().add_employee).click()
       self.driver.find_element(by=By.NAME, value=locators.Orange_Locators().employee_first).send_keys(data.Orange_Data().employee_first_input)
       self.driver.find_element(by=By.NAME, value=locators.Orange_Locators().employee_last).send_keys(data.Orange_Data().employee_last_input)
       self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().save_button1).click()
       assert self.driver.title == self.driver.title
       print("SUCCESS: Added new employee details with Username {a} and Password {b}". format(a=data.Orange_Data.username, b=data.Orange_Data.password))
       
   #CODE for Test case ID:TC_PIM_02       
       
    def test_Edit_employee(self, booting_function):
       self.driver.get(data.Orange_Data().url)
       self.driver.implicitly_wait(4)
       self.driver.find_element(by=By.NAME, value=locators.Orange_Locators().username_inputBox).send_keys(data.Orange_Data().username)
       self.driver.find_element(by=By.NAME, value=locators.Orange_Locators().password_inputBox).send_keys(data.Orange_Data().password)
       self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().LoginButton).click()
       self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().pim_button).click()
       self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().employee_fullname).send_keys(data.Orange_Data().employee_name)
       self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().search_button).click()
       self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().edit_button).click()
       self.driver.find_element(by=By.NAME, value=locators.Orange_Locators().mid_name).send_keys(data.Orange_Data().middle_name1)
       self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().save_button).click()
       assert self.driver.title == self.driver.title
       print("SUCCESS: Edited employee with Midname{a}". format(a=data.Orange_Data.middle_name1))
       
   #CODE for Test case ID:TC_PIM_03   
    def test_Delete_employee(self, booting_function):
       self.driver.get(data.Orange_Data().url)
       self.driver.implicitly_wait(4)
       self.driver.find_element(by=By.NAME, value=locators.Orange_Locators().username_inputBox).send_keys(data.Orange_Data().username)
       self.driver.find_element(by=By.NAME, value=locators.Orange_Locators().password_inputBox).send_keys(data.Orange_Data().password)
       self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().LoginButton).click()
       self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().pim_button).click()
       self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().employee_fullname).send_keys(data.Orange_Data().employee_name1)
       self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().search_button).click()
       self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().delete_button).click()
       self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().yes_button).click()
       assert self.driver.title == self.driver.title
       print("SUCCESS: Successfully Deleted the Employee Info")
       
       





