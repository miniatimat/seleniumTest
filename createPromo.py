import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from datetime import date
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#HTML search heirarchy: ID -> Name -> Class
DRIVER = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

def create_promo(promoCode, games, selectedCurrency):
    #Log into Bob
    DRIVER.get("https://tools.rubicon.vsslots.com/bob/login.php?r=https://tools.rubicon.vsslots.com/bob/applications/QA/WTR00/")
    WebDriverWait(DRIVER, 10).until(EC.presence_of_element_located((By.NAME, "username"))).send_keys("mateo.miniati")
    WebDriverWait(DRIVER, 10).until(EC.presence_of_element_located((By.NAME, "password"))).send_keys("09Sep1998")
    WebDriverWait(DRIVER, 10).until(EC.presence_of_element_located((By.NAME, "submit"))).click()

    #Go to create Promotion
    DRIVER.get("https://tools.rubicon.vsslots.com/bob/applications/FRP/CMP00/#create")
    time.sleep(1)

    #Input promo code
    WebDriverWait(DRIVER, 10).until(EC.presence_of_element_located((By.ID, "CMP00-create-promotion_code"))).send_keys(promoCode)

    #Select Mode (By default is Fun)
    modesField = WebDriverWait(DRIVER, 10).until(EC.presence_of_element_located((By.ID, "CMP00_create_game_mode_chosen")))
    modeSelector = modesField.find_element(By.CSS_SELECTOR, "a")
    modeSelector.click()
    modes = modesField.find_element(By.TAG_NAME, "input")
    modes.send_keys("FUN")
    modes.send_keys(Keys.ENTER)

    #input number of plays (By default is 10)
    WebDriverWait(DRIVER, 10).until(EC.presence_of_element_located((By.ID, "CMP00-create-plays_total"))).send_keys(10)

    #Input bet ammount (By default is 100)
    WebDriverWait(DRIVER, 10).until(EC.presence_of_element_located((By.ID, "CMP00-create-total_bet"))).send_keys(100)

    #Input currency, (By default is USD)
    currencyField = WebDriverWait(DRIVER, 10).until(EC.presence_of_element_located((By.ID, "CMP00_create_currency_id_chosen")))
    currencySelector = currencyField.find_element(By.CSS_SELECTOR, "a")
    currencySelector.click()
    currencies = currencyField.find_element(By.TAG_NAME, "input")
    currencies.send_keys(selectedCurrency)
    currencies.send_keys(Keys.ENTER)
    #currencyField.find_elements(By.CSS_SELECTOR, "li")
    #currencies[116].click() #USD

    #Input start date and expiration date
    WebDriverWait(DRIVER, 10).until(EC.presence_of_element_located((By.ID, "CMP00-create-start_date"))).send_keys(date.today().strftime("%y-%m-%d "))
    WebDriverWait(DRIVER, 10).until(EC.presence_of_element_located((By.ID, "CMP00-create-expiration_date"))).send_keys((date.today()+datetime.timedelta(days=1)).strftime("%y-%m-%d "))

    #Input allowed operators
    allowedOperatorsField = WebDriverWait(DRIVER, 10).until(EC.presence_of_element_located((By.ID, "CMP00_create_operator_id_chosen")))
    allowedOperators = allowedOperatorsField.find_element(By.CSS_SELECTOR, "input")
    allowedOperators.send_keys("Vibragaming QA")
    allowedOperators.send_keys("Vibragaming QA")
    allowedOperators.send_keys(Keys.ENTER)
    allowedOperators.send_keys("RavCorp Kiosk")
    allowedOperators.send_keys(Keys.ENTER)

    #Input allowed Games
    gamecodeField = WebDriverWait(DRIVER, 10).until(EC.presence_of_element_located((By.ID, "CMP00_create_game_code_chosen")))
    gamecodes = gamecodeField.find_element(By.CSS_SELECTOR, "input")
    gamecodes.send_keys(games[0])
    for game in games:
        gamecodes.send_keys(game)
        gamecodes.send_keys(Keys.ENTER)


    #Input selected currency for promotion
    allowedCurrencyField = WebDriverWait(DRIVER, 10).until(EC.presence_of_element_located((By.ID, "CMP00_create_allowed_currency_id_chosen")))
    allowedCurrency = allowedCurrencyField.find_element(By.CSS_SELECTOR, "input")
    allowedCurrency.send_keys(selectedCurrency)
    allowedCurrency.send_keys(selectedCurrency)
    allowedCurrency.send_keys(Keys.ENTER)


    DRIVER.find_element(By.ID, "CMP00-create").submit()
    time.sleep(120)
    DRIVER.quit()

create_promo("SeleniumTest", ["chocolate", "salariazo"], "US Dollar")

