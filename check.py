# Script to check a crypto value and Alert via Email
# By Felipe Ferreira
import requests
import pandas as pd
import smtplib
from dotenv import load_dotenv
import os 

btclowwarn = 35000


#Get sensitive info from .env local file
load_dotenv()
gmail_user = os.getenv('gmail_user')
gmail_password = os.getenv('gmail_password')
api_key = os.getenv('api_key')
email = os.getenv('email')

def sendEmail(subject,content):
 try: 
    server_ssl = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server_ssl.ehlo()   # optional
    server_ssl.login(gmail_user, gmail_password)
    server_ssl.sendmail(gmail_user, email, f"Subject: {subject}\n{content}")
    # ...send emails
 except:
    print ('ERROR - Something went wrong sending email...')
    quit()

def get_crypto_price(symbol):
    api_url = f'https://cloud.iexapis.com/stable/crypto/{symbol}/price?token={api_key}'
    raw = requests.get(api_url).json()
    price = raw['price']
    return float(price)

btc = get_crypto_price('btcusd')
msg = 'Price of 1 Bitcoin: {} USD'.format(btc)
print(msg)

if btc < btclowwarn:
  print("BTC is low")
  sendEmail('BTC is low', 'Bitcoin price is low ' )