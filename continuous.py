#This module is to continuously run the bot by creating a webserver
#using uptimerobot to send request to the server

from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
  return "Hi I'm alive"

def run():
  app.run(host = '0.0.0.0', port = 8080)

def keep_alive():
  t = Thread(target=run)
  t.start()