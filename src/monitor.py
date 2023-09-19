import os
import time
import re
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from utils import load_linkedin_credentials

# Load LinkedIn credentials from the config file
linkedin_email, linkedin_password = load_linkedin_credentials()

# Set up the Selenium WebDriver
driver = webdriver.Chrome()
time.sleep(2)
driver.get('https://www.linkedin.com')
time.sleep(5)

# Log in to LinkedIn
username_field = driver.find_element(By.ID, 'session_key')
password_field = driver.find_element(By.ID, 'session_password')

username_field.send_keys(linkedin_email)
time.sleep(3)
password_field.send_keys(linkedin_password)
time.sleep(5)
password_field.send_keys(Keys.RETURN)
time.sleep(5)

# Navigate to a competitor's LinkedIn page (modify the URL accordingly)
with open('../data/profiles/competitors/competitors.txt', 'r') as f:
    competitors_profile_url = f.readlines()

for competitor_profile_url in competitors_profile_url:
    driver.get(competitor_profile_url)
    time.sleep(3)
    # Click the 'Connections' tab to view their connections
    connections_tab = driver.find_element(By.XPATH, '//*[@class="artdeco-card ember-view pv-top-card"]/div/ul/li')
    connections_tab.click()

    # # Scroll down to load more connections (you may need to adjust this loop)
    # for _ in range(5):
    #     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #     time.sleep(2)
    time.sleep(3)
    # Extract and store the profiles of new connections
    connections = driver.find_elements(By.XPATH, '//*[@class="search-results-container"]/div/div/ul/li[@class="reusable-search__result-container"]')


    for connection in connections:
        # Extract and store the profile URL
        profile_url_element = connection.find_element(By.XPATH, './/div/div/div[2]/div[1]/div[1]/div/span[1]/span/a')
        profile_url = re.search(r"/in/([^/?]+)", profile_url_element.get_attribute('href'))[1]
        profile_name = connection.find_element(By.XPATH, './/div/div/div[2]/div[1]/div[1]/div/span[1]/span/a/span/span[1]').text
        profile_headline = connection.find_element(By.XPATH, './/div/div/div[2]/div[1]/div[2]/div[1]').text

        if profile_url:
            # Create a dictionary to store the profile URL
            profile_data = {
                "profile_url": profile_url,
                "profile_name": profile_name,
                "profile_headline": profile_headline
            }

            # Save the profile data to a JSON file
            profile_filename = profile_url + '_profile.json'
            profile_path = os.path.join('../data/profiles/connection/', profile_filename)

            with open(profile_path, 'w') as profile_file:
                json.dump(profile_data, profile_file, indent=4)

            print(f"Saved profile URL: {profile_url}")

# Close the web browser
driver.quit()