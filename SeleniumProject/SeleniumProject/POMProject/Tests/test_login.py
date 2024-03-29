import time
import unittest
from selenium import webdriver
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))
from POMProject.Pages.loginPage import LoginPage
from POMProject.Pages.homePage import HomePage
import HtmlTestRunner


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
            executable_path="C:/Users/Milad Zolfaghari/PycharmProjects/SeleniumProject/driver/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_01_login_valid(self):
        driver = self.driver

        driver.get("https://www.wesat.co/")

        login = LoginPage(driver)
        login.click_home_login()
        login.enter_username("milad@wesaturate.com")
        login.enter_password("Samar9889")
        login.click_login()

        homepage = HomePage(driver)
        homepage.click_avatar()
        homepage.click_logout()

        time.sleep(2)

    def test_02_login_invalid_username(self):
        driver = self.driver

        driver.get("https://www.wesat.co/")

        login = LoginPage(driver)
        login.click_home_login()
        login.enter_username("milad@turate.com")
        login.enter_password("Samar9889")
        login.click_login()
        message = driver.find_elements_by_xpath("")
        self.assertEqual(message, "Invalid login credentials")

        time.sleep(2)

    # search for mountains
    # SearchBar = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[1]/div/div[3]/form/input')
    # SearchBar.send_keys("Mountains")
    # SearchBar.send_keys(Keys.ENTER)

    # Join Wesat (create a user)
    # Join = driver.find_element_by_link_text('Join')
    # Join.click()
    # driver.find_element_by_name("firstName").send_keys("AutoTestFirstName")
    # driver.find_element_by_name("lastName").send_keys("AutoTestLastName")
    # driver.find_element_by_name("email").send_keys("milad.zolfaghari98@gmail.com")
    # driver.find_element_by_name("username").send_keys("autotest123")
    # driver.find_element_by_name("password").send_keys("Test123!")

    # Go to get pro
    # GetPro = driver.find_element_by_link_text('Get Pro')
    # GetPro.click()

    @classmethod
    def tearDown(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")




if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(report_title= "Wesat Testing Results", output='C:/Users/Milad Zolfaghari/PycharmProjects/SeleniumProject/reports'))


