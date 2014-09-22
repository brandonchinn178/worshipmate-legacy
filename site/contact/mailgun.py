import requests
import os

def send_simple_message(name, email, message):
    return requests.post(
        "https://api.mailgun.net/v2/worshipdatabase.info/messages",
        auth=("api", os.environ['MAILGUN_KEY']),
        data={"from": name + " <" + email + ">",
              "to": "Brandon Chinn <brandonchinn178@gmail.com>",
              "subject": "[Worship Song Database] Contact Form",
              "text": message})