# Written in Python 3.7.2
# Last updated: April 7th 2021.
# Function: Email myself if /r/cryptocurrency MOONs are of noteworthy price.
# Note: You may need to turn on Less secure app access on sending gmail account.
# Note: It is not recommended to use personal email as the sender. (It's insecure)

# Imports for web scraping
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import urllib.request

# Imports for email
from email.message import EmailMessage
import smtplib

# Import time to wait between price checks
import time

def email(recommendation, info):
    send_from = "YOUR_BOT_EMAIL@gmail.com" # Email sender's email address
    send_to = "YOUR_EMAIL_HERE@wherever.com" # Email receiver's email address
    password = "YOUR_BOT_EMAIL_HERE" # Email sender's password

    # Create server and login
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(send_from, password)

    # Format message with information from check_moon_price() and send.
    message = 'Subject: {}\n\n{}'.format(recommendation, info)
    server.sendmail(send_from, send_to, message)
    

def check_moon_price():
    url = "https://www.coingecko.com/en/coins/moon"
    # Use headers to avoid ERROR 403 / being blocked.
    request = Request(url, headers={'User-Agent':'Mozilla/5.0'})
    # Scrape and parse the URL.
    soup = BeautifulSoup(urllib.request.urlopen(request).read(),'html.parser')
    # Find the exact data we want inside the CSS.
    moon_data = soup.find('span', class_='no-wrap')
    moon_price = moon_data.get_text() # Just take the text.
    moon_usd_value = float(moon_price[1:]) # Remove "$" and convert to float.
    recommendation = "Fix your broken code. D:" # Create value.
    moons_worth = "Moons are currently worth: ${0} USD.".format(moon_usd_value)

    # If price is noteworthy email myself. Otherwise do nothing.
    if moon_usd_value <= 0.0666:
        recommendation = "Buy!"
        email(recommendation, moons_worth)
    elif moon_usd_value > 0.12:
        recommendation = "Consider selling Moons."
        email(recommendation, moons_worth)
    elif moon_usd_value > 0.30:
        recommendation = "SELL MOONS NOW OH GOD IT'S HAPPENING!"
        email(recommendation, moons_worth)
    else:
        recommendation = "Do nothing."
        print('{0} {1}'.format(moons_worth, recommendation))

# Runs indefinitely
while True:
    check_moon_price()
    time.sleep(1200) # Wait 20 minutes
