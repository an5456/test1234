import time
from selenium import webdriver
import json
import re

from util.operation_json import OperationJson


class GetCookies():
    def __init__(self, url, username, password, code):
        self.url = url
        self.user_name = username
        self.passoord = password
        self.code = code
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)
        time.sleep(3)

    def get_cookies(self):
        user_name = self.driver.find_element_by_name("username")
        password = self.driver.find_element_by_name("password")
        code = self.driver.find_element_by_name("captcha")
        login = self.driver.find_element_by_id("login")
        user_name.send_keys(self.user_name)
        password.send_keys(self.passoord)
        code.send_keys(int(self.code))
        login.click()
        cookie = self.driver.get_cookies()
        # self.driver.close()
        for cook in cookie:
            a = json.dumps(cook)
            ab = re.findall('"value": "(.*)"}', a)[0]
            print(ab)
            op = OperationJson()
            ab = {
                "SESSION": ab
            }
            op.write_data(ab)
            time.sleep(2)


if __name__ == '__main__':
    gc = GetCookies(url='http://scm.csjmro.com/', username='serviceadmin@csjscm.com', password='Aa12345678', code='1234')
    gc.get_cookies()
