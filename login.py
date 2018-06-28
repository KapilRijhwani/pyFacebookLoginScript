from selenium import webdriver
from time import sleep

usr = input('Please enter your facebook email Id : ')
pwd = input('Please enter your facebook password : ')

# Change the Chrome Webdriver location in your laptop
driver = webdriver.Chrome('C:\\Users\\krijhwan\\PycharmProjects\\pythonBegg2\\chromedriver.exe')
driver.get('https://www.facebook.com/')
print('opened facebook')
sleep(1)

username_box = driver.find_element_by_id('email')
username_box.send_keys(usr)
print('Email entered')
sleep(1)

password_box = driver.find_element_by_id('pass')
password_box.send_keys(pwd)
print('Password entered')

login_box = driver.find_element_by_id('loginbutton')
login_box.click()

input('Press anything to quit')
driver.quit()
print('Finished')
