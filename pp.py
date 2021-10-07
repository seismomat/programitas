import unittest
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

options=webdriver.ChromeOptions()
options.add_argument('--start-maximized')

chrome_driver=webdriver.Chrome("chromedriver",options=options)
chrome_driver.get("https://web.fciencias.unam.mx/acceder")

correo=chrome_driver.find_element_by_name("username")
correo.send_keys("309033453")

correo=chrome_driver.find_element_by_name("password")
correo.send_keys("Matematico10")

time.sleep(2)

correo.send_keys(Keys.ENTER)
time.sleep(2)

## entrar a grupos
WebDriverWait(chrome_driver,5)\
.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
'#apps-container > div:nth-child(1) > ul:nth-child(2) > li:nth-child(1) > a')))\
.click()

time.sleep(2)

### entrar a lista en manejo de datos
WebDriverWait(chrome_driver,5)\
.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
'#info-contenido > div:nth-child(7) > ul > li:nth-child(2) > a')))\
.click()

time.sleep(2)

# Picar boton de herramientas
WebDriverWait(chrome_driver,15)\
.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
'#pagetools > h5 > a')))\
.click()

time.sleep(2)

## extraer EXcel
WebDriverWait(chrome_driver,15)\
.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
'#pagetools > div > ul > li:nth-child(2) > a')))\
.click()
