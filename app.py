from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

url = 'https://www.lacasadelosfamososmexico.tv/vota'
lista = [0, 1, 3, 7, 9, 0, 1, 3, 7, 9, 0, 1, 3, 7, 9, 0, 1, 3, 7, 9, 11, 6, 8]

votacionOn = True

def init_driver(url):
    # Set up Chrome options to open in incognito mode
    chrome_options = Options()
    chrome_options.add_argument("--incognito")

    chrome_beta_path = 'C:\Program Files\Google\Chrome Beta\Application\chrome.exe'

    # Specify the path to your ChromeDriver
    chrome_driver_path = "./chromedriver.exe"

    chrome_options.binary_location = chrome_beta_path

    # Create a WebDriver instance with the options
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=chrome_options)

    # Navigate to a webpage
    driver.get(url)

    return driver


# # # # # # # # #
#
#
#

while votacionOn:

    driver = init_driver(url)
    time.sleep(2)

    iframe = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, 'iframe'))
    )

    driver.switch_to.frame(0)

    div_msg = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, 'QWohSAgVBkmPS94lYtAO4'))
    )

    if("cerrada" in div_msg[0].text):
        print('=========================================================================')
        print('                         Ya se cerró la votación                         ')
        print('=========================================================================')
        break

    driver.quit()


    for el in lista:
        driver = init_driver(url)
        time.sleep(2)

        iframe = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, 'iframe'))
        )

        driver.switch_to.frame(0)

        elements = WebDriverWait(driver, 2).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, '_2iOcrrk9I4LxMSZo502VM6'))
        )

        elements[el].click()

        time.sleep(2)

        driver.quit()