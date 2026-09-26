from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Start Chrome
driver = webdriver.Chrome()

# Open locally hosted portfolio website
driver.get("http://localhost:8000")

driver.maximize_window()

# Find all links on the webpage
links = driver.find_elements(By.TAG_NAME, "a")

# Print total number of links
print("Total Links:", len(links))
print("--------------------------------")

# Print text and URL of every link
for link in links:

    text = link.text
    url = link.get_attribute("href")

    print("Link Text:", text)
    print("Link URL :", url)
    print("--------------------------------")

time.sleep(5)

driver.quit()