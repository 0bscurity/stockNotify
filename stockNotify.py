# stockNotify.py
from datetime import date
from time import sleep
import sqlite3

# data source
import yfinance as yf

# sms capability
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Database connection
conn = sqlite3.connect('C:/Users/Andrew/PycharmProjects/stockNotify/limitHitDB.db')

email = "smsgatewaytest1@gmail.com"
password = "pythonsmstest"

sms_gateway = "4432318834@mmst5.tracfone.com"
smtp = "smtp.gmail.com"
port = 587
server = smtplib.SMTP(smtp, port)
server.starttls()
server.login(email, password)

alert = MIMEMultipart()
alert['From'] = email
alert['To'] = sms_gateway

desired_price = int(input("Enter Desired Price Limit: "))

stock = yf.Ticker("PYPL")


def check_price():
    latest_price = stock.history(period='1d')['Close'][0]
    return latest_price


def gold():

    INSERT INTO LIMITHITDB values ()

    alert['Subject'] = "STOCK NOTIFICATION\n"
    body = "PYPL hit the desired price\n"
    alert.attach(MIMEText(body, 'plain'))

    sms = alert.as_string()
    server.sendmail(email, sms_gateway, sms)

    server.quit()


while check_price() < desired_price:
    check_price()
    sleep(15)
    print("waiting")


gold()
