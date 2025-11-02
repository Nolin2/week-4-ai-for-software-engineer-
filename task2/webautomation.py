from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Launch Chrome browser
driver = webdriver.Chrome()
driver.get("https://google.com")

# Locate the Google search box
search_box = driver.find_element(By.NAME, "q")

# AI-like automation: perform a smart search
search_box.send_keys("climate change and AI impact")
time.sleep(1)
search_box.send_keys(Keys.RETURN)

# Wait for results and take a screenshot
time.sleep(3)
driver.save_screenshot("ai_google_search.png")

print("✅ AI automated search complete. Screenshot saved as ai_google_search.png")
driver.quit()

