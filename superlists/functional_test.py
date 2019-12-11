from selenium import webdriver

path = "/home/abc/Downloads/geckodriver"
browser = webdriver.Firefox(executable_path =path)
browser.get('http://localhost:8000')
assert 'Django' in browser.title
