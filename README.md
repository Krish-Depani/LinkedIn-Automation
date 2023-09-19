# LinkedIn Automation for Connection Requests

## Overview

This project provides a Python-based automation system for monitoring competitors' LinkedIn activity and sending hyper-personalized connection requests to their new connections. It uses Selenium for web automation and includes the following functionalities:

- Monitoring competitor profiles and connections.
- Extracting profile data
- Generating personalized connection request messages.
- Sending connection requests with personalized messages.

## Table of Contents

- [Setup](#setup)
- [Usage](#usage)
- [Documentation](#documentation)
- [Directory Structure](#directory-structure)
- [Libraries Used](#libraries-used)

## Setup

1. **Clone the Repository**: Clone this GitHub repository to your local machine.

   ```bash
   git clone https://github.com/yourusername/linkedin-automation.git
   ```

2. **Install Dependencies**: Install the dependencies listed in the [requirements.txt](requirements.txt) file.

   ```bash
   cd linkedin-automation
   pip install -r requirements.txt
   ```

3. **Download ChromeDriver**: Download the [ChromeDriver](https://chromedriver.chromium.org/downloads) for your Chrome version and operating system. Extract the downloaded file and move the `chromedriver` executable to the `drivers` directory.

4. **LinkedIn credentials**: In config.py, add your LinkedIn credentials to the `linkedin_email` and `linkedin_passowrd` variables.


## Usage

1. **Add Competitors**: Add the LinkedIn profiles of your competitors to the data/profiles/competitors/competitors.txt file. Each profile should be on a new line.

   ```text
   https://www.linkedin.com/in/competitor1/
   https://www.linkedin.com/in/competitor2/
   https://www.linkedin.com/in/competitor3/
   ```

2. **Run the Bot**: Run the bot using the following command:

   ```bash
   python src/monitor.py
   ```

   The bot will start monitoring the profiles of your competitors and will send connection requests to their new connections.

3. **Run Message Generator**: Run the message generator using the following command:

   ```bash
   python src/generate-messages.py
   ```

   The message generator will generate personalized connection request messages for the new connections of your competitors.

4. **Send Connection Requests**: Run the connection request sender using the following command:

   ```bash
   python src/send-requests.py
   ```

   The connection request sender will send connection requests to the new connections of your competitors.

## Documentation

### Approach
- The project uses Selenium for web automation to interact with the LinkedIn website.
- Competitor profiles are monitored to extract new connections and profile data.
- Personalized connection request messages are generated based on profile data.
- Connection requests are sent with personalized messages.

#### Libraries Used
- Selenium: Used for web automation to interact with the LinkedIn website.
- JSON: Used to handle JSON data for configuration and profile storage.
- os: Used for file and directory operations.
- time: Used for adding delays to ensure proper page loading.
- re: Used for regular expressions to extract data from URLs.

#### Directory Structure

```text
linkedin-automation
├── config
│   └── config.json
├── data
│   ├── profiles
│   │   ├── competitors
│   │   │   └── competitors.txt
│   │   └── connection
│   └── messages
├── src
│   ├── generate-messages.py
│   ├── monitor.py
│   ├── utils.py
│   └── send-requests.py
├── README.md
└── requirements.txt
```
