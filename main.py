import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from datetime import date
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#HTML search heirarchy: ID -> Name -> Class
PATH = "C:\Program Files (x86)/chromedriver.exe"
DRIVER = webdriver.Chrome(PATH)
def open_game(name):
    DRIVER.get("https://emulator.rubicon.vsslots.com/")
    DRIVER.maximize_window()
    print(DRIVER.title)
    time.sleep(5)
    try:
        userID = WebDriverWait(DRIVER, 10).until(EC.presence_of_element_located((By.ID, "txtUserId")))
        gameID = WebDriverWait(DRIVER, 10).until(EC.presence_of_element_located((By.ID, "txtGameId")))
        brokerLocation = WebDriverWait(DRIVER, 10).until(EC.presence_of_element_located((By.ID, "txtBrokerLocation")))
        casinoButton = WebDriverWait(DRIVER, 10).until(EC.presence_of_element_located((By.ID, "iconCasino")))
        musicButton = WebDriverWait(DRIVER, 10).until(EC.presence_of_element_located((By.ID, "iconMusicOn")))
        sfxButton = WebDriverWait(DRIVER, 10).until(EC.presence_of_element_located((By.ID, "iconSFXOn")))
        gameID.send_keys(name)
        brokerLocation.click()
        musicButton.click()
        sfxButton.click()
        casinoButton.click()
    except:
        DRIVER.quit()

    DRIVER.close()


def test_game():
    originalWindow = DRIVER.current_window_handle
    DRIVER.switch_to.window(DRIVER.window_handles[1])
    print(DRIVER.title)
    game = WebDriverWait(DRIVER, 10).until(EC.presence_of_element_located((By.TAG_NAME, "canvas")))
    
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
    modes = modesField.find_elements(By.CSS_SELECTOR, "li")
    modes[0].click()

    #input number of plays (By default is 10)
    WebDriverWait(DRIVER, 10).until(EC.presence_of_element_located((By.ID, "CMP00-create-plays_total"))).send_keys(10)

    #Input bet ammount (By default is 100)
    WebDriverWait(DRIVER, 10).until(EC.presence_of_element_located((By.ID, "CMP00-create-total_bet"))).send_keys(100)

    #Input currency, (By default is USD)
    currencyField = WebDriverWait(DRIVER, 10).until(EC.presence_of_element_located((By.ID, "CMP00_create_currency_id_chosen")))
    currencySelector = currencyField.find_element(By.CSS_SELECTOR, "a")
    currencySelector.click()
    currencies = currencyField.find_elements(By.CSS_SELECTOR, "li")
    currencies[116].click() #USD

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
    time.sleep(5)
    DRIVER.quit()

def assignPromo(promoCode, users):
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
    userField.send_keys(users[0])
    for user in users:
        userField.send_keys(user)
        userField.send_keys(Keys.ENTER)


    time.sleep(5)
    DRIVER.quit()


assignPromo("MateoCodex", ["mateo@VIBRA"])
#create_promo("promoTest", ["chocolate", "salariazo"], "US Dollar")

#Hablar con Diego Zamora o Fabio Quintana