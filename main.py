#!/usr/bin/env python3

import requests
import os
from bs4 import BeautifulSoup

def isNotNone(*args):
  for arg in args:
    if arg is None:
      return (False);
  return (True);

def sendRequest(url, method = "get", params = None):
  try:
    session   = requests.Session()
    headers   = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.7113.93 Safari/537.36", 
        "Accept":     "text/html"
    }
    req = session.get(url, data=params, headers=headers)
    res = req.text
    req.close()
    return (res)
  except:
    print("Failed to connect to " + hostname(url) + ".\n")
    return (None)

url = "https://lite.duckduckgo.com/lite/?t=ffab&q=what+is+my+ip&atb=v373-1"
req = sendRequest(url, "get", None)
soup = BeautifulSoup(req, "html.parser")
answer = soup.findAll("td")[3]

if isNotNone(answer):
  print(answer.text.strip())
else:
  print("Your IP address is ")
  os.system("curl ifconfig.me -s")
  print(" (Location Unknown)");
