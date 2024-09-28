import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import os
import wget

# Specify the path to chromedriver.exe (download and save on your computer)
driver = webdriver.Chrome()
# Set window size to ensure consistent element visibility
driver.set_window_size(1280, 800)
# Open the webpage
driver.get("http://www.instagram.com")

# Target username and password fields
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

# Enter username and password
username.clear()
username.send_keys("genduvikky")
password.clear()
password.send_keys("kanyawest")

# Target the login button and click it
button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

# We are logged in!
time.sleep(5)
alert = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Save info")]'))).click()
alert2 = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()

# Wait for the search input field to appear and be clickable
searchbox = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']"))
)
searchbox.clear()

# Search for the hashtag
keyword = "#traveldestination"
searchbox.send_keys(keyword)
time.sleep(5)
searchbox.send_keys(Keys.ENTER)
searchbox.send_keys(Keys.RETURN)
time.sleep(2)

driver.execute_script("window.scrollTo(0,4000);")
time.sleep(5)

# Scrape image URLs
images = driver.find_elements(By.TAG_NAME, 'img')
image_urls = [image.get_attribute('src') for image in images]

# Close the web driver
driver.quit()

# Download the images
output_directory = "travel_images"  # Changed from "cat_images" to "travel_images"
os.makedirs(output_directory, exist_ok=True)
for i, url in enumerate(image_urls):
    try:
        filename = os.path.join(output_directory, f"travel_image_{i}.jpg")  # Changed from "cat_image" to "travel_image"
        wget.download(url, filename)
        print(f"Downloaded image {i + 1}: {filename}")
    except Exception as e:
        print(f"Error downloading image {i + 1}: {e}")

print(f"Downloaded {len(image_urls)} travel images.")  # Changed from "cat images" to "travel images"
