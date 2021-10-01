import chromedriver_autoinstaller
from selenium import webdriver
import shutil
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]

try:
    ch_driver = webdriver.Chrome('./chromedriver/chromedriver.exe', options = options)
    print('chrome check OK')
    time.sleep(0.2)
    ch_driver.quit()
except:
    print('chrome is not updated version')
    chromedriver_autoinstaller.install(True)
    ch_driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options = options)
    shutil.copy2(f'./{chrome_ver}/chromedriver.exe', './chromedriver/chromedriver.exe')
    print('chrome update complete')
    time.sleep(0.2)
    ch_driver.quit()