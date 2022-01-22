
import requests
import pandas as pd
import smtplib
from dotenv import load_dotenv
import os 

btclowwarn = 35000
email = 'fel.h2o@gmail.com'

load_dotenv()



gmail_user = os.getenv('gmail_user')
gmail_password = os.getenv('gmail_password')

def sendEmail(subject,content):
 try: 
    server_ssl = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server_ssl.ehlo()   # optional
    server_ssl.login(gmail_user, gmail_password)
    server_ssl.sendmail(gmail_user, email, f"Subject: {subject}\n{content}")
    # ...send emails
 except:
    print ('Something went wrong sending email...')
    

def get_crypto_price(symbol):
    api_key = 'pk_54cdad9a8f4b411680cddc40467dd04d'
    api_url = f'https://cloud.iexapis.com/stable/crypto/{symbol}/price?token={api_key}'
    raw = requests.get(api_url).json()
    price = raw['price']
    return float(price)

btc = get_crypto_price('btcusd')
print('Price of 1 Bitcoin: {} USD'.format(btc))

if btc < btclowwarn:
  print("BTC is low")
  sendEmail('Test Email', 'OK email works')