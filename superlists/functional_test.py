from selenium import webdriver
import unittest

path = "/home/abc/Downloads/geckodriver"

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox(executable_path =path)
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_start_list_and_retrieve_it_later(self):
		#to check it home page
		self.browser.get("http://localhost:8000")

		self.assertIn('To-Do',self.browser.title)
		self.fail('Finsh the test!')



if __name__ == '__main__':
	unittest.main(warnings='ignore')
