from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
chromeOptions=webdriver.ChromeOptions()
chromeOptions.add_argument('--incognito') #gizli sekme


mailim=""
sifre=""

driver=webdriver.Chrome(options=chromeOptions)
driver.maximize_window()

driver.get("https://www.trendyol.com/giris?cb=%2Fapple%2Fiphone-11-64-gb-beyaz-cep-telefonu-aksesuarsiz-kutu-apple-turkiye-garantili-p-65149494")

driver.find_element(By.ID, 'login-email').send_keys(mailim)
driver.find_element(By.ID, 'login-password-input').send_keys(sifre)
driver.find_element(By.CLASS_NAME,'submit').click()
sleep(35)
