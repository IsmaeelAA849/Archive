from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")

capabilities = DesiredCapabilities.CHROME.copy()
capabilities['acceptSslCerts'] = True 
capabilities['acceptInsecureCerts'] = True

driver = webdriver.Chrome(chrome_options = chrome_options,executable_path='your path',desired_capabilities=capabilities)
driver.get("yourWebsite")