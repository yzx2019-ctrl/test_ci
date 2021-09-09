# -*- coding: utf-8 -*-

from selenium import webdriver
import time

driver_path = "C:\driver\chromedriver.exe"


class TestDemo(object):

    def setup_class(self):
        print("开始")
        self.driver = webdriver.Chrome(executable_path=driver_path)

    def teardown_class(self):
        self.driver.quit()
        print("结束")

    def test_open(self):
        self.driver.get("http://www.baidu.com")
        self.driver.find_element_by_id("kw").send_keys("宋春梅")
        self.driver.find_element_by_id("su").click()
        time.sleep(5)

    def test_hah(self):
        print("hahah")
