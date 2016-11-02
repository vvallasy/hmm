import sys
if sys.version_info[0] < 3:
  class urllib:
    request = __import__("urllib2")
else:
  import urllib.request
  
import json
import random

global bahasa, key
key = "17fddd72-b0b6-45f1-ae16-d99d9923b300" #### KASIH KEY LU #######
bahasa = "pt"

def set(x):
    global bahasa
    bahasa = x
    
def SimSimi(kalimat):
    g = ">///<"
    kata = kalimat.replace(" ","+")
    try:
        data = urllib.request.urlopen("http://sandbox.api.simsimi.com/request.p?key=%s&lc=%s&ft=1.0&text=%s" % (key, bahasa, kata)).read().decode('utf-8')
        jsondata = json.loads(data)
        respon = jsondata["response"]
        if "I HAVE NO RESPONSE" in respon:
            respon = g
    except Exception as e:
        respon = g
    return respon
