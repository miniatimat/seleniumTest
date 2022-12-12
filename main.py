import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from createPromo import create_promo
from assignPromo import assignPromo

#HTML search heirarchy: ID -> Name -> Class
DRIVER = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
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

    DRIVER.quit()


def test_game():
    originalWindow = DRIVER.current_window_handle
    DRIVER.switch_to.window(DRIVER.window_handles[1])
    print(DRIVER.title)
    game = WebDriverWait(DRIVER, 10).until(EC.presence_of_element_located((By.TAG_NAME, "canvas")))
    

def main():
    create_promo("SeleniumTest", ["chocolate", "salariazo"], "US Dollar")
    assignPromo("MateoCodex", "mateo@VIBRA")

main()
#Hablar con Diego Zamora o Fabio Quintana