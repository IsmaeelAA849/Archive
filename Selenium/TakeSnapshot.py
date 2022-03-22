
#from Screenshot import Screenshot_clipping
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#mobile_emulation = { "deviceName": "iPhone 12" }
mobile_emulation = {
   "deviceMetrics": { "width": 428, "height": 926, "pixelRatio": 3.0 },
   "userAgent": "Mozilla/5.0 (iPhone 12 Pro Max; CPU iPhone OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1" }
chrome_options = Options()
chrome_options.add_argument("--headless")

chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
#chrome_options.add_argument("screenshot")
chrome_options.add_argument("window-size=1980,960")
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://archive.org/details/pastpages-usa-today-2016-09")

driver.save_screenshot('test.png')
driver.quit()