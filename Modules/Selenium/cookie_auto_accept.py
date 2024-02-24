from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

path = "C:\\Program Files\\Mozilla Firefox\\geckodriver.exe"

driver = webdriver.Firefox(executable_path=path)
driver.get("https://google.com")

sleep(3)

a = ActionChains(driver)
a.key_down(Keys.TAB)
a.key_up(Keys.TAB)
a.key_down(Keys.TAB)
a.key_up(Keys.TAB)
a.key_down(Keys.RETURN)
a.key_up(Keys.RETURN)
a.click()
a.perform()
