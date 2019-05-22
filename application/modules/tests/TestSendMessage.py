import unittest
from selenium import webdriver
import time


class TestSendMessage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8080/")

    def test_message_marat(self):
        self.fieldName = self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/input[1]").send_keys("marat")
        self.fieldPassword = self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/input[2]").send_keys(
            "123")
        self.buttonAuth = self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/button").click()
        self.fieldMessage = self.driver.find_element_by_xpath("//*[@id='message']").send_keys("Привет")
        time.sleep(1)
        self.buttonSendMessage = self.driver.find_element_by_xpath("//*[@id='sendMessage']").click()
        time.sleep(1)
        assert "Привет" in self.driver.page_source

    def test_message_vasya(self):
        self.fieldName = self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/input[1]").send_keys("vasya")
        self.fieldPassword = self.driver.find_element_by_xpath("/html/body/ div[2]/div[1]/div/input[2]").send_keys(
            "123")
        self.buttonAuth = self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/button").click()
        self.fieldMessage = self.driver.find_element_by_xpath("//*[@id='message']").send_keys("Привет")
        time.sleep(1)
        self.buttonSendMessage = self.driver.find_element_by_xpath("//*[@id='sendMessage']").click()
        time.sleep(1)
        assert "Привет" in self.driver.page_source

    def test_empty_message(self):
        self.fieldName = self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/input[1]").send_keys("vasya")
        self.fieldPassword = self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/input[2]").send_keys(
            "123")
        self.buttonAuth = self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/button").click()
        self.buttonSendMessage = self.driver.find_element_by_xpath("//*[@id='sendMessage']").click()
        time.sleep(1)
        assert "Привет" not in self.driver.page_source

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
        unittest.main()
