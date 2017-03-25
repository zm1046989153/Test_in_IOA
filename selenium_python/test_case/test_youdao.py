#_*_ coding:utf-8 _*_

from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest,time,re


class Youdao(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome()
		self.driver.maximize_window()
		self.driver.implicitly_wait(3)
		self.base_url = "http://www.youdao.com"
		self.accept_next_alert = True

	def test_youdao_search(self):
		"""有道搜索"""
		#pass
		driver = self.driver 
		driver.get(self.base_url + "/")

		driver.find_element_by_id("translateContent").send_keys(u"selenium")
		driver.find_element_by_css_selector("#form > button").click()
		#driver.find_element_by_id("translateContent").send_keys(u"selenium")
        
        time.sleep(2)

	def tearDown(self):
		self.driver.quit()
		#pass


if __name__ == "__main__":
	unittest.main()