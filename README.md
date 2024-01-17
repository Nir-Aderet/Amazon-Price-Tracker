# Amazon-Price-Tracker

---Project Overview:
The Amazon Price Tracker is a Python script designed to monitor the prices of items on Amazon. Users can easily track multiple product pages and receive email notifications when prices drop below a specified threshold.

This Python script allows you to track the prices of items on Amazon and receive email notifications when the prices drop below a certain threshold. It uses web scraping to extract item names and prices from Amazon product pages.

---Prerequisites:
Before using the script, make sure you have the following:
-Python 3 installed on your computer.
-Required Python packages installed (you can install them using pip install package_name):
    ~requests
    ~BeautifulSoup (bs4)
    ~pandas
    ~smtplib (for sending email notifications)

---Usage:
Open the script and locate the DATA dictionary. This is where you can add the URLs of the Amazon product pages you want to track. You can add as many URLs as needed.

DATA = {'URL': [
    'https://www.amazon.com/example-url-1',
    'https://www.amazon.com/example-url-2',
    # Add more URLs here
]}

Configure the HEADERS dictionary with your user-agent information to make requests to Amazon.
HEADERS = {"User-Agent": 'Your User-Agent String Here'}

Set up your Gmail account credentials in the send_mail function to receive email notifications.
server.login('your_email@gmail.com', 'your_password')
Note: Using your Gmail password directly in the script is not recommended. Consider using an app-specific password or a more secure method for sending emails.

Run the script using the following command:
python price_tracker.py

The script will do the following:
    ~Retrieve item names and prices from the specified Amazon product pages.
    ~Calculate a discounted price (e.g., 70% of the original price).
    ~Store the data in a CSV file named url_data.csv.
    ~Check if the current price is less than or equal to the alert price (e.g., the discounted price).
     If the price is lower, it will send an email notification with a link to the product page.

---Customization:
You can customize the script further by adjusting the threshold for price alerts or adding more data columns to the CSV file, depending on your requirements.

Please be aware of Amazon's terms of service and scraping policies, and use the script responsibly to avoid potential issues.

---Disclaimer:
This script is provided for educational purposes only and may require updates or adjustments due to changes in website structures or policies. Use it at your own discretion and risk.
