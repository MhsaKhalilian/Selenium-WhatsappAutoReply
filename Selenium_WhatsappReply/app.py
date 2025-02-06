from selenium import webdriver  
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.common.by import By  
from colorama import init, Fore, Style, Back  
import time 
import os
from selenium.webdriver.chrome.service import Service

path = "your path to driver"

service = Service(path)
driver = webdriver.Chrome(service=service)

driver.get('https://web.whatsapp.com/')  
input("In\nRUN??\n\n") 
init()  
os.system('cls')  
message = input(Fore.LIGHTCYAN_EX + 'Enter a message: ' + Fore.WHITE)
time.sleep(0.3) 
names = input(Fore.LIGHTCYAN_EX + 'Enter Names [& splited]: ' + Fore.WHITE).split('&') 
time.sleep(0.3)
number_range = int(input(Fore.LIGHTCYAN_EX + 'Enter Number: ' + Fore.WHITE))
time.sleep(0.8)  
for name in names:
    driver.find_element(By.XPATH, f'//span[@title="{name}"]').click()  
    for number in range(number_range):
        driver.find_element(By.XPATH, '//div[@role="textbox" and @data-tab="10"]').send_keys(message + Keys.ENTER)  
    print(Fore.LIGHTGREEN_EX + '[+] -' + Fore.RED + name)
    
    input('\n\EXIT??\n\n')


