from selenium import webdriver

browser = webdriver.Chrome()

browser.get('http://localhost:8080')

browser.quit()