import unittest
from selenium import webdriver
import time


class TestAuthorization(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8080/")

    def test_auth_marat(self):
        self.fieldName = self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/input[1]").send_keys("marat")
        self.fieldPassword = self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/input[2]").send_keys("123")
        self.buttonAuth = self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/button").click()
        time.sleep(1)
        assert "Пользователь Зарипов Марат Наилевич подключился!" in self.driver.page_source

        # if self.driver.find_element_by_xpath("//*[@id='chat']")\
        #         .text == "Пользователь Зарипов Марат Наилевич подключился!":
        #     print('Авторизация Марата прошла успешно')
        # else:
        #     print('Авторизация Марата провалилась!!!')

    def test_auth_vasya(self):
        self.fieldName = self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/input[1]").send_keys("vasya")
        self.fieldPassword = self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/input[2]").send_keys("123")
        self.buttonAuth = self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/button").click()
        time.sleep(1)
        assert "Пользователь Иванов Василий Петрович подключился!" in self.driver.page_source
        # if self.driver.find_element_by_xpath("//*[@id='chat']")\
        #         .text == "Пользователь Иванов Василий Петрович подключился!":
        #     print('Авторизация Василий прошла успешно')
        # else:
        #     print('Авторизация Василия провалилась!!!')

    def test_auth_incorrect_password(self):
        self.fieldName = self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/input[1]").send_keys("vasya")
        self.fieldPassword = self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/input[2]").send_keys("322")
        self.buttonAuth = self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/button").click()
        assert "Неверные логин и(или) пароль!" in self.driver.page_source
        # if self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/p") \
        #         .text == "Неверные логин и(или) пароль!":
        #     print('Тест с некорректным паролем прошел')
        # else:
        #     print('Тест с некорректным паролем не прошел!!!')

    def test_auth_incorrect_login(self):
        self.fieldName = self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/input[1]").send_keys("vasya1")
        self.fieldPassword = self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/input[2]").send_keys("123")
        self.buttonAuth = self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/button").click()
        assert "Неверные логин и(или) пароль!" in self.driver.page_source
        # if self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/p") \
        #         .text == "Неверные логин и(или) пароль!":
        #     print('Тест с некорректным логином прошел')
        # else:
        #     print('Тест с некорректным логином не прошел!!!')

    def test_auth_incorrect_login_and_password(self):
        self.fieldName = self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/input[1]").send_keys("evgen")
        self.fieldPassword = self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/input[2]").send_keys("322")
        self.buttonAuth = self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/button").click()
        assert "Неверные логин и(или) пароль!" in self.driver.page_source
        # if self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/p") \
        #         .text == "Неверные логин и(или) пароль!":
        #     print('Тест с некорректным логином и паролем прошел')
        # else:
        #     print('Тест с некорректным логином и паролем не прошел!!!')

    def test_auth_empty_fields(self):
        self.fieldName = self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/input[1]").send_keys("")
        self.fieldPassword = self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/input[2]").send_keys("")
        self.buttonAuth = self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/button").click()
        assert "Не введен логин и(или) пароль!" in self.driver.page_source
        # if self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/p") \
        #         .text == "Не введен логин и(или) пароль!":
        #     print('Тест с пустыми полями прошел')
        # else:
        #     print('Тест с пустыми полями не прошел!!!')

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
