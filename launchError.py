from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files (x86)/chromedriver.exe"
DRIVER = webdriver.Chrome(PATH)

def launchError():
    DRIVER.get("https://tools.rubicon.vsslots.com/bob/login.php?r=https://tools.rubicon.vsslots.com/bob/applications/QA/WTR00/")
    WebDriverWait(DRIVER, 10).until(EC.presence_of_element_located((By.NAME, "username"))).send_keys("mateo.miniati")
    WebDriverWait(DRIVER, 10).until(EC.presence_of_element_located((By.NAME, "password"))).send_keys("09Sep1998")
    WebDriverWait(DRIVER, 10).until(EC.presence_of_element_located((By.NAME, "submit"))).click()

    #Go to assign Promotion
    DRIVER.get("https://tools.rubicon.vsslots.com/bob/applications/FRP/CIT00/#create")
    time.sleep(1)

