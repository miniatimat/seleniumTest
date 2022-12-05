from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#HTML search heirarchy: ID -> Name -> Class
PATH = "C:\Program Files (x86)/chromedriver.exe"
DRIVER = webdriver.Chrome(PATH)

def assignPromo(promoCode, user):
    DRIVER.get("https://tools.rubicon.vsslots.com/bob/login.php?r=https://tools.rubicon.vsslots.com/bob/applications/QA/WTR00/")
    WebDriverWait(DRIVER, 10).until(EC.presence_of_element_located((By.NAME, "username"))).send_keys("mateo.miniati")
    WebDriverWait(DRIVER, 10).until(EC.presence_of_element_located((By.NAME, "password"))).send_keys("09Sep1998")
    WebDriverWait(DRIVER, 10).until(EC.presence_of_element_located((By.NAME, "submit"))).click()

    #Go to assign Promotion
    DRIVER.get("https://tools.rubicon.vsslots.com/bob/applications/FRP/CIT00/#create")
    time.sleep(1)

    promoIDField = WebDriverWait(DRIVER, 10).until(EC.presence_of_element_located((By.ID, "CIT00_create_promotion_definition_id_chosen")))
    promoID = promoIDField.find_element(By.CSS_SELECTOR, "a")
    promoID.click()
    textbox = promoIDField.find_element(By.CSS_SELECTOR, "input")
    textbox.send_keys(promoCode)
    textbox.send_keys(Keys.ENTER)

    userField = WebDriverWait(DRIVER, 10).until(EC.presence_of_element_located((By.ID, "CIT00-create-user_identifier")))
    userField.send_keys(user)
    userField.send_keys(Keys.ENTER)


    time.sleep(5)
    DRIVER.quit()

assignPromo("MateoCodex", "mateo@VIBRA")