import os
import json

# Function to load LinkedIn credentials from the config file
def load_linkedin_credentials(config_path='../config/config.json'):
    try:
        with open(config_path, 'r') as config_file:
            config = json.load(config_file)
            linkedin_email = config.get('linkedin_email')
            linkedin_password = config.get('linkedin_password')
            return linkedin_email, linkedin_password
    except FileNotFoundError:
        print("Config file not found. Please provide LinkedIn credentials in config.json.")
        return None, None

# Function to create directories if they don't exist
def create_directories(directories):
    for directory in directories:
        os.makedirs(directory, exist_ok=True)

# Function to extract profile data from a JSON file
def extract_profile_data(profile_path):
    try:
        with open(profile_path, 'r') as profile_file:
            return json.load(profile_file)
    except FileNotFoundError:
        print(f"Profile data not found: {profile_path}")
        return None

# Function to extract a LinkedIn profile URL from a JSON filename
def extract_profile_url(filename):
    try:
        return f'https://www.linkedin.com/in/{filename.split("_")[0]}'
    except Exception as e:
        print(f"Error extracting profile URL: {str(e)}")
        return None
