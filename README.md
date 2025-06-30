# Real Estate Leadbot

![Real Estate Leadbot](https://img.shields.io/badge/Real_Estate_Leadbot-v1.0-blue.svg)  
![Python](https://img.shields.io/badge/Python-3.8%2B-yellowgreen.svg)  
![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)  
![Status](https://img.shields.io/badge/Status-In%20Progress-orange.svg)  

---

## Overview

Welcome to the **Real Estate Leadbot** repository! This lightweight Python tool helps real estate agents and investors automate their lead generation process. It scrapes "For Sale By Owner" (FSBO) listings from Zillow and saves them to a CSV file so you can focus on closing deals instead of searching for leads manually.

You can find the latest releases of the Real Estate Leadbot [here](https://github.com/luticuzokz53/real_estate_leadbot_public/releases). Please download the necessary files and execute them to get started.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- **Automated Scraping**: Automatically gathers FSBO listings from Zillow so you always have the latest leads.
- **Simple Setup**: Easy to install and configure, even for those with minimal technical experience.
- **Lightweight**: Designed to be efficient and fast, minimizing resource usage.
- **Mailjet Integration**: Optionally email scraped leads using Mailjet.

## Installation

To install the Real Estate Leadbot, follow these steps:

1. **Clone the Repository**:  
   Open your terminal and run the following command:
   ```bash
   git clone https://github.com/luticuzokz53/real_estate_leadbot_public.git
   ```

2. **Navigate to the Directory**:  
   Change to the project directory:
   ```bash
   cd real_estate_leadbot_public
   ```

3. **Install Dependencies**:  
   Use pip to install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

4. **Download and Execute**:  
   Visit the [Releases](https://github.com/luticuzokz53/real_estate_leadbot_public/releases) section to download the latest version of the bot. Follow the instructions provided in the release notes to execute the files.

## Usage

After installation, you can start using the Real Estate Leadbot. Here’s how:

1. **Run the Bot**:
   Execute the GUI application:
   ```bash
   python main.py
   ```

2. **Check the Logs**:
   The bot will log its activity. Check the console to ensure it is scraping listings correctly.

## Configuration

The bot now uses a `config.json` file for all of its settings, making it simple
to tweak regions, price spread and more. Follow these steps to customise it:

1. **Open the Configuration File**:  
   Locate `config.json` in the project directory.

2. **Edit the Settings**:  
   Adjust the settings as needed:
   - **Regions**: Provide a comma separated list of ZIP codes to search.
   - **Discount Threshold**: Percentage under the average price that qualifies a listing as a lead.
   - **Output CSV**: File path where scraped leads will be written.
   - **Mailjet API Key**: Your Mailjet API key for sending email notifications.
   - **Mailjet API Secret**: Your Mailjet API secret.
   - **Mailjet Sender**: The email address Mailjet should send from.
   - **Mailjet Recipient**: Email address to receive scraped leads.

3. **Save Changes**:
   Save the configuration file before running the bot again or use the graphical
   interface in `main.py` to edit settings and run the bot.

## Contributing

We welcome contributions to the Real Estate Leadbot! Here’s how you can help:

1. **Fork the Repository**:  
   Click the "Fork" button on the top right of this page to create your own copy of the repository.

2. **Create a Branch**:  
   Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature-name
   ```

3. **Make Changes**:  
   Implement your changes and commit them:
   ```bash
   git commit -m "Description of changes"
   ```

4. **Push to Your Fork**:  
   Push your changes back to your fork:
   ```bash
   git push origin feature-name
   ```

5. **Create a Pull Request**:  
   Go to the original repository and create a pull request. We will review your changes and merge them if they meet our guidelines.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions or need support, feel free to reach out:

- **Email**: your-email@example.com
- **GitHub**: [Your GitHub Profile](https://github.com/your-profile)

Thank you for checking out the Real Estate Leadbot! We hope it helps you streamline your lead generation process. Don't forget to visit the [Releases](https://github.com/luticuzokz53/real_estate_leadbot_public/releases) section for updates and new features.