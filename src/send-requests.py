import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from utils import load_linkedin_credentials

# Set up the Selenium WebDriver
driver = webdriver.Chrome()
time.sleep(2)
driver.get('https://www.linkedin.com')
time.sleep(5)

# Load LinkedIn credentials from the config file
linkedin_email, linkedin_password = load_linkedin_credentials()

# Log in to LinkedIn
username_field = driver.find_element(By.ID, 'session_key')
password_field = driver.find_element(By.ID, 'session_password')

username_field.send_keys(linkedin_email)
time.sleep(3)
password_field.send_keys(linkedin_password)
time.sleep(5)
password_field.send_keys(Keys.RETURN)
time.sleep(5)

# Directory path where generated messages are stored
messages_directory = '../data/messages/'

# Loop through each generated message and send connection requests
for filename in os.listdir(messages_directory):
    if filename.endswith('_message.txt'):
        message_path = os.path.join(messages_directory, filename)

        with open(message_path, 'r') as message_file:
            message = message_file.read()

        # Extract the LinkedIn profile URL from the message filename
        profile_url = f'https://www.linkedin.com/in/{filename.split("_")[0]}'

        # Navigate to the profile URL
        driver.get(profile_url)
        time.sleep(3)

        # Click the "More" button to reveal the "Connect" option
        try:
            more_button = driver.find_element(By.XPATH,
                                              '/html/body/div[4]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[3]/div/div[2]/button')
            more_button.click()
        except Exception as e:
            pass
        time.sleep(3)

        # Click the "Connect" button
        try:
            connect_button = driver.find_element(By.XPATH,
                                                 '/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[3]/div/div[2]/div/div/ul/li[7]/div/span')
        except Exception as e:
            connect_button = driver.find_element(By.XPATH,
                                                 '/html/body/div[4]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[3]/div/div[2]/div/div/ul/li[3]/div/span')
        finally:
            driver.find_element(By.XPATH,
                                '/html/body/div[4]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[3]/div/button')
        connect_button.click()
        time.sleep(3)

        # Add a personalized message to the connection request
        add_note_button = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[3]/button[1]/span')
        add_note_button.click()
        time.sleep(1)
        note_textarea = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div[1]/textarea')
        note_textarea.send_keys(message)

        # Send the connection request
        send_button = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[3]/button[2]/span')
        send_button.click()

        # Wait for a moment before sending the next request (adjust as needed)
        time.sleep(3)

print("Connection requests sent.")
# Close the web browser
driver.quit()
