'''Archivo con estructura POM y lo complementa el archivo Funciones'''

'''PRUEBA LOGIN GMAIL'''


'''IDE: Phycharm
Lenguaje: Python
Framework: Selenium'''

import time
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from Funciones import Funciones


class Funciones_login():

    def __init__(self,driver):
        self.driver = driver

    def L1(self,email, clave,t=2):
        global driver
        driver = webdriver.Chrome(executable_path="C:\webdriver\chrome\chromedriver.exe")
        # driver = webdriver.Chrome(executable_path="C:\webdriver\firefox\geckodriver.exe")

        f = Funciones(driver)
        f.Navegar("https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&emr=
	1&followup=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ifkv=ASKXGp3YirEWJqYd8Awbn3HpKXgIWzpABSZR0QutBiFQnmx-PrwXo2aypI
	bWrGxeRqAu-Z1Km7pFuw&osid=1&passive=1209600&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S487548529%3A170
	2560587592091&theme=glif)
        driver.maximize_window()
        f.Texto_Mixto("id", "Email", email, 2)
	f.Click_Mixto("xpath", "//span[contains(.,'Siguiente')]", 2)
        f.Texto_Mixto("id", "Password", clave, 2)
        f.Click_Mixto("xpath", "//span[contains(.,'Siguiente')]", 2)
        
        driver.close()