# This Selenium-Python script function is made to create a bot (without logging on twitch) and select a random stream
# Project by Chuma, Nepta, Dany with special participation of ChatGPT-3.
# ChatGPT-3 brought a lot of the core code, my friends and me are doing the code cleaning and testing.
# Here are the libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import random

# Since the intention of the bot is to keep running and watching the stream
# Here we will detach chrome.
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# It's important to setup chrome_options to give indication of the driver_path

driver_path= "chromedriver"


# Setting up Selenium web driver
driver = webdriver.Chrome(driver_path, options= chrome_options)
driver.maximize_window()


# Navigate to the Twitch home page
driver.get('https://www.twitch.tv/')

# Wait for the page to load
time.sleep(5)

# Find the list of streams on the home page
#streams = driver.find_elements(By.CSS_SELECTOR, 'a[data-a-target="preview-card-image-link"]')
streams = driver.find_elements(By.XPATH, '//a[@data-a-target="preview-card-image-link"]')

# Either method works, and it's similar, this will find an element based on a preview card image
# XPath and CSS Selector are almost brothers in function.

# Pick a random stream from the list
stream = random.choice(streams)
# Here the random library is called.


# Click on the stream to start watching it
stream.click()

# Wait for the stream to load
time.sleep(10)



# Left over codes from ChatGPT-3, basically the script would end with a python console command of just
# Inserting any key, we decided to use detach function as it is intended that the bot watches the stream

# There isn't any login in the page so no website TDA is being broken.

# Left over comment code.

# Wait for user input before closing the browser
# input('Press any key to exit')

# Close the browser window
# driver.quit()