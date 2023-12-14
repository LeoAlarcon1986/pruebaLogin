
'''PRUEBA LOGIN GMAIL'''


'''IDE: Phycharm
Lenguaje: Python
Framework: Selenium
Libreria: Unittest'''

from selenium import webdriver
from selenium.webdriver.common.keys import keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
import time

class prueba_gmail(unittest.TestCase):

def	setUp(self):
	self.GM=webdriver.Chrome(executable_path="ruta del chrome o gecko driver")
	t=2
    
def test_login1(self):
	GM=self.driver
	GM.get("https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&emr=1&followup=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ifkv=ASKXGp0wHzgUPXKa2hPTrHwEs-5xLgj9Ww-dRdxRcoaRjPiIYioKRbHImfaAmLhhn9hllS98t1FI&osid=1&passive=1209600&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S973780683%3A1702506334006070&theme=glif")
	GM.maximize_window()
	nom=GM.find.element_by_xpath("//input[contains(@id,'identifierId')]")
	btn=GM.find.element_by_xpath("//span[contains(.,'Siguiente')]")
	pass=GM.find.element_by_xpath("//input[contains(@type,'password')]")
	btn2=GM.find.element_by_xpath("//span[contains(.,'Siguiente')]")
	nom.send_keys("leonardo77710@gmail.com")
	btn.click()
	pass.send_keys("123456789")
	btn2.click()
	time.sleep(3)

'''todo lo que tiene "def test_login1(self):" se puede copiar todo y se cambia la informacion de las variables
nom y btn y asi se generan los escenarios de prueba'''

def tearDown(self):
	GM=self.GM
	GM.close

if __name__=='__main__':
	unittest.main()