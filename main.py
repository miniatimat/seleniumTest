from selenium import webdriver

PATH = "C:\Program Files (x86)/chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://emulator.rubicon.vsslots.com/")
print(driver.title)
driver.close()