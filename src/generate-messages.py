import os
from utils import create_directories, extract_profile_data

# Directory path where LinkedIn profile data files are stored
profiles_directory = '../data/profiles/connection/'

# Directory path to store generated messages
messages_directory = '../data/messages/'

# Function to generate a personalized connection request message
def generate_connection_request_message(profile_data):
    # Extract relevant information (modify as needed)
    profile_name = profile_data.get('profile_name', 'N/A')
    profile_headline = profile_data.get('profile_headline', 'N/A')

    # Generate a personalized message
    message = f"Hi {profile_name},\n\nI noticed your profile on LinkedIn and was impressed by your {profile_headline}. " \
              f"I'd love to connect and learn more about your work and experiences. " \
              f"Looking forward to connecting with you!\n\nBest regards, [Your Name]"

    return message

# Loop through each profile file and generate a personalized message
for filename in os.listdir(profiles_directory):
    if filename.endswith('_profile.json'):
        profile_path = os.path.join(profiles_directory, filename)
        profile_data = extract_profile_data(profile_path)
        if profile_data:
            message = generate_connection_request_message(profile_data)

            # Save the generated message to a file (customize the filename as needed)
            message_filename = os.path.splitext(filename)[0] + '_message.txt'
            message_path = os.path.join(messages_directory, message_filename)

            with open(message_path, 'w') as message_file:
                message_file.write(message)

            print(f"Generated message for {filename}")

print("Message generation complete.")
