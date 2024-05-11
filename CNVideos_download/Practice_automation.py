from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
chrome_options = Options()
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
chrome_driver_path = ChromeDriverManager().install()

# Create a Service object for ChromeDriver
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()

driver.get("https://www.saucedemo.com/")
try:
    username = WebDriverWait(driver,10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Username']"))
    )
    print("trying to find element")
# input_field = driver.find_element(By.XPATH, '//input[@title = "Search for Products, Brands and More"]')
    print("element found")
    username.clear()
    username.send_keys("standard_user")
except Exception as e:
    print("error",e)

try:
    password = WebDriverWait(driver,5).until(
        EC.element_to_be_clickable((By.XPATH,"//input[@placeholder='Password']" ))
        )
    password.clear()
    password.send_keys("secret_sauce")
    password.submit()
except Exception as e:
    print("error",e)

print("logged in successfully")

items_element = driver.find_elements(By.XPATH, "//div[@class='inventory_item_name ']")
prices_element = driver.find_elements(By.XPATH, "//div[@class='inventory_item_price']")
items = [item.text for item in items_element]
prices = [price.text for price in prices_element]

item_prices_pair = zip(items, prices)

for item,price in item_prices_pair:
    print(f"{item} : {price}")

for item in items:
    if "sauce" not in item.lower():
        add_to_cart_button = driver.find_element(By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)")
        add_to_cart_button.click()
        print("added into cart")

        
