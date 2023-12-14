import time
import unittest

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


class Funciones():

    def __init__(self,driver):
        self.driver = driver

    def Tiempo(self,tiempo):
        t=time.sleep(tiempo)
        return t

    def Navegar(self,url,Tiempo):
        self.driver.get(url)
        self.driver.maximize_window()
        t = time.sleep(Tiempo)
        return t


    def Texto_Mixto(self,tipo,selector,texto,Tiempo):
        if(tipo=="xpath"):
            try:
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, selector)))
                val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
                val = self.driver.find_element(By.XPATH, (selector))
                val.clear()
                val.send_keys(texto)
                print("El campo es {} de texto -> {}".format(selector,texto))
                t = time.sleep(Tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("no se encontro elemento" +selector)
                return t

        elif (tipo == "id"):
            try:
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, selector)))
                val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
                val = self.driver.find_element(By.ID, (selector))
                val.clear()
                val.send_keys(texto)
                print("El campo es {} de texto -> {}".format(selector, texto))
                t = time.sleep(Tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("no se encontro elemento" + selector)
                return t

    def Click_Mixto(self, tipo, selector, Tiempo):
        if (tipo == "xpath"):
            try:
                val=self.SEX(selector)
                val.click()
                print("dando click {}  -> {}".format(selector,selector))
                t = time.sleep(Tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("no se encontro elemento" + selector)
                return t

        elif (tipo == "id"):
             try:
                 val=self.SEI(selector)
                 val.click()
                 print("dando click {}  -> {}".format(selector,selector))
                 t = time.sleep(Tiempo)
                 return t
             except TimeoutException as ex:
                 print(ex.msg)
                 print("no se encontro elemento" + selector)
                 return t
