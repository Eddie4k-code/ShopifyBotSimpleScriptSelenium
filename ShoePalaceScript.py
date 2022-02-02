from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from tkinter import *
from tkinter import messagebox
import time



PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

def start():


    user_start = str(input('Please enter key words: '))
    time.sleep(5)
    main_link = driver.get(f"https://www.shoepalace.com/search?q={user_start}")

start()


time.sleep(2)
try:

    select = driver.find_element_by_class_name("spf-product-card__inner")
    select.click()
    print('Product Found')

except:
    print('PRODUCT NOT FOUND')

#Billing Info
email = 'test123@gmail.com'
first_name = 'John'
last_name = 'Smith'
address = '7474 Lake Road'
city = 'new york city'
country = 'United States'
state = 'NY'
phone = '111-111-1111'
zip_code = '14304'
time.sleep(2)

#Payment Info
credit = '5555555555554444'
credit1 = '3333'
credit2 = '3333'
credit3 = '3333'
name_card = 'John Smith'
exp_date = '03'
exp_date2 = '2'
ssn = '123'



def add_to_cart(cart):

    cart = driver.find_element_by_class_name("productForm-buttons")
    cart.click()

add_to_cart('cart')
print('Adding To cart....')

#print(driver.page_source)

time.sleep(2)

def checkout(out):
    driver.get("https://www.shoepalace.com/checkout")



checkout('out')
print('Hitting checkout.....')

#time.sleep(20) Activate if captcha to give yourself enough time to solve captcha


print('Filling billing info')
#Email
email_grab = driver.find_element_by_name("checkout[email]")
email_grab.send_keys(email)

#First Name
first_name_grab = driver.find_element_by_name("checkout[shipping_address][first_name]")
first_name_grab.send_keys(first_name)


#Last Name
last_name_grab = driver.find_element_by_name("checkout[shipping_address][last_name]")
last_name_grab.send_keys(last_name)

#Address
address_grab = driver.find_element_by_name("checkout[shipping_address][address1]")
address_grab.send_keys(address)

#City
city_grab = driver.find_element_by_name("checkout[shipping_address][city]")
city_grab.send_keys(city)

#Country
country_grab = driver.find_element_by_name("checkout[shipping_address][country]")
country_grab.send_keys(country)

#State
state_grab = driver.find_element_by_name("checkout[shipping_address][province]")
state_grab.send_keys(state)

#ZIP CODE
zip_grab = driver.find_element_by_name("checkout[shipping_address][zip]")
zip_grab.send_keys(zip_code)

#Phone
phone_grab = driver.find_element_by_name("checkout[shipping_address][phone]")
phone_grab.send_keys(phone)


#terms
terms = driver.find_element_by_name("checkout[attributes][I agree to the Terms and Conditions]")
terms.click()

#Continue
cont = driver.find_element_by_id("continue_button")
cont.click()
print('Hitting continue payment')
#Contine to paymet
cont_payment = driver.find_element_by_id("continue_button")
cont_payment.click()

time.sleep(3)


#Credit Card / Debit Card
cc_grab = driver.find_element_by_xpath('//iframe[@title="Field container for: Card number"]').send_keys(credit)
cc_grab1 = driver.find_element_by_xpath('//iframe[@title="Field container for: Card number"]').send_keys(credit1)
cc_grab2 = driver.find_element_by_xpath('//iframe[@title="Field container for: Card number"]').send_keys(credit2)
cc_grab3 = driver.find_element_by_xpath('//iframe[@title="Field container for: Card number"]').send_keys(credit3)





#Name on card
name_card_grab = driver.find_element_by_xpath('//iframe[@title="Field container for: Name on card"]')
name_card_grab.send_keys(name_card)

#Exp date
exp_date_grab = driver.find_element_by_xpath('//iframe[@title="Field container for: Expiration date (MM / YY)"]')
exp_date_grab.send_keys(exp_date)
exp_date_grab.send_keys(exp_date2)

#Security Code
ssn_grab = driver.find_element_by_xpath('//iframe[@title="Field container for: Security code"]')
ssn_grab.send_keys(ssn)

#Submit Payment

time.sleep(2)


try:
    payment = driver.find_element_by_id("continue_button")
    payment.click()
except:
    print('Payment error')

time.sleep(6)

try:
    driver.find_elements_by_class_name("notice__text")
    print('Payment Failed, Invalid Payment Information.')
except:
    print('Payment Success')













