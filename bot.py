
#################################################################################################################
import ch
import random
import sys
import re
import json
import time
import datetime
import os
import urllib
import urllib.request
import urllib.parse
import __future__
import mal
from urllib.parse import quote
from xml.etree import cElementTree as ET
if sys.version_info[0] > 2:
  import urllib.request as urlreq
else:
  import urllib2 as urlreq

print("Loading whois")
whois = dict()
f = open("whois.txt", 'r')
for line in f.readlines():
  try:
    if len(line.strip())>0:
      uid, names = json.loads(line.strip())
      whois[uid] = names
  except:pass
f.close()
botname = 'Reabot' ##isi idnya
password = 'Sankarea01' ##isi paswordnya

##nick names
def sntonick(username):
    user = username.lower()
    if user in nicks:
        nick = json.loads(nicks[user])
        return nick
    else:
        return user

#### Returns the number of seconds since the program started.
################################################################
def getUptime():
    # do return startTime if you just want the process start time
    return time.time() - startTime

def reboot():
    output = ("rebooting server . . .")
    os.popen("sudo -S reboot")
    return output

#### SYSTEM UPTIME
def uptime():
 
     total_seconds = float(getUptime())
 
     # Helper vars:
     MINUTE  = 60
     HOUR    = MINUTE * 60
     DAY     = HOUR * 24
 
     # Get the days, hours, etc:
     days    = int( total_seconds / DAY )
     hours   = int( ( total_seconds % DAY ) / HOUR )
     minutes = int( ( total_seconds % HOUR ) / MINUTE )
     seconds = int( total_seconds % MINUTE )
 
     # Build up the pretty string (like this: "N days, N hours, N minutes, N seconds")
     string = ""
     if days > 0:
         string += str(days) + " " + (days == 1 and "day" or "days" ) + ", "
     if len(string) > 0 or hours > 0:
         string += str(hours) + " " + (hours == 1 and "hour" or "hours" ) + ", "
     if len(string) > 0 or minutes > 0:
         string += str(minutes) + " " + (minutes == 1 and "minute" or "minutes" ) + ", "
     string += str(seconds) + " " + (seconds == 1 and "second" or "seconds" )
 
     return string;

## DEFINITIONS
dictionary = dict() 
f = open("definitions.txt", "r")
for line in f.readlines():
  try:
    if len(line.strip())>0:
      word, definition, name = json.loads(line.strip())
      dictionary[word] = json.dumps([definition, name])
  except:
    print("[ERROR]Cant load definition: %s" % line)
f.close()
##nicks
nicks=dict()#empty list
f=open ("nicks.txt","r")#r=read w=right
for line in f.readlines():#loop through eachlinimporte and read each line
    try:#try code
        if len(line.strip())>0:#strip the whitespace checkgreater than 0
            user , nick = json.loads(line.strip())
            nicks[user] = json.dumps(nick)
    except:
        print("[Error]Can't load nick %s" % line)
f.close()
##Rooms
rooms = []
f = open("rooms.txt", "r") # read-only
for name in f.readlines():
  if len(name.strip())>0: rooms.append(name.strip())
f.close()
##owners
owners = []
try:
    file = open("owners.txt", "r")
    for name in file.readlines():
        if len(name.strip()) > 0:
            owners.append(name.strip())
    print("[INFO]Owners loaded...")
    file.close()
except:
    print("[ERROR]no file named owners")
    print("2 second to read the error")
    time.sleep(2)
    exit()
time.sleep(1)

###admin
admin = []
try:
    file = open("admin.txt", "r")
    for name in file.readlines():
        if len(name.strip()) > 0:
            admin.append(name.strip())
    print("[INFO]Admin loaded...")
    file.close()
except:
    print("[ERROR]no file named admin")
    print("2 second to read the error")
    time.sleep(2)
    exit()
time.sleep(1)
##archknight
archknight = []
try:
    file = open("archknight.txt", "r")
    for name in file.readlines():
        if len(name.strip()) > 0:
            archknight.append(name.strip())
    print("[INFO]archknight loaded...")
    file.close()
except:
    print("[ERROR]no file named archknight")
    print("2 second to read the error")
    time.sleep(2)
    exit()
time.sleep(1)
##whitelist
whitelist = []
try:
    file = open("whitelist.txt", "r")
    for name in file.readlines():
        if len(name.strip()) > 0:
            whitelist.append(name.strip())
    print("[INFO]whitelist loaded...")
    file.close()
except:
    print("[ERROR]no file named whitelist")
    print("2 second to read the error")
    time.sleep(2)
    exit()
time.sleep(1)

#END#
#Dlist
dlist = []
f = open("dlist.txt", "r") # read-onlyimport
for name in f.readlines():
  if len(name.strip())>0: dlist.append(name.strip())
f.close()
#END#
#SN TRY
sn = dict()
try:
  f = open('note.txt','r')
  sn = eval(f.read())
  f.close()
except:pass
#put after def onMessage

## Send Notes
sasaran = dict()
f = open ("notes.txt", "r") #read-only
for line in f.readlines():
  try:
    if len(line.strip())>0:
      to, body, sender = json.loads(line.strip())
      sasaran[to] = json.dumps([body, sender])
  except:
    print("[Error] Notes load fails : %s" % line)
f.close()
# SN Notifs
notif = []
f = open("notif.txt", "r")
for name in f.readlines():
  if len(name.strip())>0: notif.append(name.strip())
f.close

blacklist = []
f = open("blacklist.txt", "r")
for name in f.readlines():
  if len(name.strip())>0: blacklist.append(name.strip())
f.close()

def tube(args):
  """
  #In case you don't know how to use this function
  #type this in the python console:
  >>> tube("pokemon dash")
  #and this function would return this thing:
  {'title': 'TAS (DS) Pokémon Dash - Regular Grand Prix', 'descriptions': '1st round Grand Prix but few mistake a first time. Next Hard Grand Prix will know way and few change different Pokémon are more faster and same course Cup.', 'uploader': 'EddieERL', 'link': 'http://www.youtube.com/watch?v=QdvnBmBQiGQ', 'videoid': 'QdvnBmBQiGQ', 'viewcount': '2014-11-04T15:43:15.000Z'}
  """
  search = args.split()
  url = urlreq.urlopen("https://www.googleapis.com/youtube/v3/search?q=%s&part=snippet&key=AIzaSyBSnh-sIjd97_FmQVzlyGbcaYXuSt_oh84" % "+".join(search))
  udict = url.read().decode('utf-8')
  data = json.loads(udict)
  rest = []
  for f in data["items"]:
    rest.append(f)
  
  d = random.choice(rest)
  link = "http://www.youtube.com/watch?v=" + d["id"]["videoId"]
  videoid = d["id"]["videoId"]
  title = d["snippet"]["title"]
  uploader = d["snippet"]["channelTitle"]
  descript = d["snippet"]['description']
  count    = d["snippet"]["publishedAt"]
  return "%s" % (link)

def gis(cari):
  argss = cari
  args = argss.split()
  headers = {}
  headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
  req = urllib.request.Request("https://www.google.co.id/search?hl=en&authuser=0&site=imghp&tbm=isch&source=hp&biw=1366&bih=623&q=" + "+".join(args), headers = headers)
  resp = urllib.request.urlopen(req).read().decode("utf-8").replace('\n','').replace('\r','').replace('\t','').replace('http://','gis:').replace('https://','gis:').replace('.jpg','.jpg:end').replace('.gif','.gif:end').replace('.png','.png:end')
  anjay = re.findall('<div class="rg_meta">(.*?)</div>', resp)
  setter = list()
  la = "".join(anjay)
  a = re.findall('"ou":"gis:(.*?):end","ow"', la)
  q = 1
  for result in a:
    if ".jpg" in result or ".gif" in result or ".png" in result:
     if "vignette" not in result and "mhcdn.net" not in result and "wikia.nocookie" not in result and "twimg.com" not in result:
      setter.append('(<b>%s</b>). http://%s' % (q, result))
      q += 1
  return "resultados para a pesquisa... <b>"+cari+"</b>:<br/><br/>"+"<br/>".join(setter[0:5])

def gs(args):
  args = args.split()
  headers = {}
  headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
  req = urllib.request.Request("https://www.google.co.id/search?q=" + "+".join(args), headers = headers)
  resp = urllib.request.urlopen(req).read().decode("utf-8").replace('\n','').replace('\r','').replace('\t','').replace('http://','gs:').replace('https://','gs:')
  anjay = re.findall('<h3 class="r">(.*?)</h3>', resp)
  setter = list()
  la = "".join(anjay)
  a = re.findall('<a href="gs:(.*?)" onmousedown="(.*?)">(.*?)</a>', la)
  q = 1
  for link, fak, title in a:
      setter.append('<br/>[%s] %s : http://%s' % (q, title.capitalize(), link))
      q += 1
  return "<br/><br/>".join(setter[0:4])
#Myanimelist
def myanimelistanime(args):
  try:
    s = args.split(" ", 1)
    args = s[1]
    val = s[0]
    try:
      val = int(val)
    except:
      args = " ".join(s)
      val = 1
  except:
      args = args
      val = 1
  val = val - 1
  if val < 0:
    val = 0
    anime = mal.anime(args, 0, val)
  else: return "Anime: %s" % anime
     

def myanimelistanime(args):
  try:
    s = args.split(" ", 1)
    args = s[1]
    val = s[0]
    try:
      val = int(val)
    except:
      args = " ".join(s)
      val = 1
  except:
      args = args
      val = 1
  val = val - 1
  if val < 0:
    val = 0
  anime = mal.anime(args, 0, val)
  return anime

def myanimelistmanga(args):
  try:
    s = args.split(" ", 1)
    args = s[1]
    val = s[0]
    try:
      val = int(val)
    except:
      args = " ".join(s)
      val = 1
  except:
    args = args
    val = 1
  val = val - 1
  if val < 0:
    val = 0
  manga = mal.manga(args, 0, val)
  return manga

def myanimelist1(args):
  try:
    s = args.split(" ", 1)
    args = s[1]
    val = s[0]
    try:
      val = int(val)
    except:
      args = " ".join(s)
      val = 1
  except:
    args = args
    val = 1
  val = val - 1
  if val < 0:
    val = 0
  anime = mal.anime(args, 1, val)
  return anime

def myanimelist2(args):
  try:
    s = args.split(" ", 1)
    args = s[1]
    val = s[0]
    try:
      val = int(val)
    except:
      args = " ".join(s)
      val = 1
  except:
    args = args
    val = 1
  val = val - 1
  if val < 0:
    val = 0
  manga = mal.manga(args, 1, val)
  return manga

def tli(args, tl):
  headers = {}
  headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
  req = urlreq.Request("http://mymemory.translated.net/api/get?q="+"+".join(args.split())+"&langpair=PT|ID", headers = headers)
  resp = urlreq.urlopen(req).read().decode("utf-8").replace('\n','') .replace('\r','').replace('\t','')
  data = json.loads(resp)
  translation = data['responseData']['translatedText']
  if not isinstance(translation, bool):
    return translation
  else:
    matches = data['matches']
    for match in matches:
     if not isinstance(match['translation'], bool):
      next_best_match = match['translation']
      break

def tip(args, tl):
  headers = {}
  headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
  req = urlreq.Request("http://mymemory.translated.net/api/get?q="+"+".join(args.split())+"&langpair=ID|PT", headers = headers)
  resp = urlreq.urlopen(req).read().decode("utf-8").replace('\n','') .replace('\r','').replace('\t','')
  data = json.loads(resp)
  translation = data['responseData']['translatedText']
  if not isinstance(translation, bool):
    return translation
  else:
    matches = data['matches']
    for match in matches:
     if not isinstance(match['translation'], bool):
      next_best_match = match['translation']
      break

def tle(args, tl):
  headers = {}
  headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
  req = urlreq.Request("http://mymemory.translated.net/api/get?q="+"+".join(args.split())+"&langpair=PT|EN", headers = headers)
  resp = urlreq.urlopen(req).read().decode("utf-8").replace('\n','') .replace('\r','').replace('\t','')
  data = json.loads(resp)
  translation = data['responseData']['translatedText']
  if not isinstance(translation, bool):
    return translation
  else:
    matches = data['matches']
    for match in matches:
     if not isinstance(match['translation'], bool):
      next_best_match = match['translation']
      break

def tlp(args, tl):
  headers = {}
  headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
  req = urlreq.Request("http://mymemory.translated.net/api/get?q="+"+".join(args.split())+"&langpair=EN|PT", headers = headers)
  resp = urlreq.urlopen(req).read().decode("utf-8").replace('\n','') .replace('\r','').replace('\t','')
  data = json.loads(resp)
  translation = data['responseData']['translatedText']
  if not isinstance(translation, bool):
    return translation
  else:
    matches = data['matches']
    for match in matches:
     if not isinstance(match['translation'], bool):
      next_best_match = match['translation']
      break

def tjp(args, tl):
  headers = {}
  headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
  req = urlreq.Request("http://mymemory.translated.net/api/get?q="+"+".join(args.split())+"&langpair=JA|PT", headers = headers)
  resp = urlreq.urlopen(req).read().decode("utf-8").replace('\n','') .replace('\r','').replace('\t','')
  data = json.loads(resp)
  translation = data['responseData']['translatedText']
  if not isinstance(translation, bool):
    return translation
  else:
    matches = data['matches']
    for match in matches:
     if not isinstance(match['translation'], bool):
      next_best_match = match['translation']
      break


def tlj(args, tl):
  headers = {}
  headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
  req = urlreq.Request("http://mymemory.translated.net/api/get?q="+"+".join(args.split())+"&langpair=PT|JA", headers = headers)
  resp = urlreq.urlopen(req).read().decode("utf-8").replace('\n','') .replace('\r','').replace('\t','')
  data = json.loads(resp)
  translation = data['responseData']['translatedText']
  if not isinstance(translation, bool):
    return translation
  else:
    matches = data['matches']
    for match in matches:
     if not isinstance(match['translation'], bool):
      next_best_match = match['translation']
      break


def dtl(args):
  url = "http://ws.detectlanguage.com/0.2/detect?q="+"+".join(quote(args).split())+"&key=demo"
  headers = {}
  headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
  req = urllib.request.Request(url, headers = headers)
  resp = urllib.request.urlopen(req).read().decode("utf-8").replace('\n','').replace('  ','').replace(' Subtitle Indonesia','').replace('-subtitle-indonesia','')
  res = re.findall('"language":"(.*?)"', resp)
  newset = list()
  num = 1
  return "".join(res).upper()

def dtg(args):
  url = "http://ws.detectlanguage.com/0.2/detect?q="+"+".join(quote(args).split())+"&key=demo"
  headers = {}
  headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
  req = urllib.request.Request(url, headers = headers)
  resp = urllib.request.urlopen(req).read().decode("utf-8").replace('\n','').replace('  ','').replace(' Subtitle English','').replace('-subtitle-english','')
  res = re.findall('"language":"(.*?)"', resp)
  newset = list()
  num = 1
  return "".join(res).upper()

def saveRank():
    f = open("owners.txt","w")
    f.write("\n".join(owners))
    f.close()
    f = open("admin.txt","w")
    f.write("\n".join(admin))
    f.close()
    f = open("archknight.txt","w")
    f.write("\n".join(archknight))
    f.close()
    f = open("whitelist.txt","w")
    f.write("\n".join(whitelist))
    f.close()
    
def googleSearch(search):
  try:
    encoded = urllib.parse.quote(search)
    rawData = urllib.request.urlopen("http://ajax.googleapis.com/ajax/services/search/web?v=1.0&q="+encoded).read().decode("utf-8")
    jsonData = json.loads(rawData)
    searchResults = jsonData["responseData"]["results"]
    full = []
    val = 1
    for data in searchResults:
      if "youtube" in data["url"]:
        data["url"] = "http://www.youtube.com/watch?v="+data["url"][35:]
      full.append("<br/>"+"(<b>%s</b> %s -> %s" % (val, data["title"], data['url']))
      val = val + 1
    return '<br/>'.join(full).replace('https://','http://')
  except Exception as e:
    return str(e)
      


      
##Setting Pretty Colors

class TestBot(ch.RoomManager):
  
  def onInit(self):
    self.setNameColor("D8BFD8")
    self.setFontColor("BA55D3")
    self.setFontFace("3")
    self.setFontSize(11)
    self.enableBg()
    self.enableRecording()

##Connecting Crap

  def onConnect(self, room):
    print("Connected")
  
  def onReconnect(self, room):
    print("Reconnected")
  
  def onDisconnect(self, room):
    print("Disconnected")

  def onPMMessage(self, pm, user, body):
    print("PM - "+user.name+": "+body)
    pm.message(user, "Sorry I'm just a bot") 
 
  #################################################################
  ### Get user access from the file, and retun lvl of access number
  #################################################################
  def getAccess(self, user):
    if user.name in owners: return 4 # Owners
    elif user.name in admin: return 3 # Admins
    elif user.name in archknight: return 2 # Arch Knight
    elif user.name in whitelist: return 1 
    elif user.name in dlist: return 0
    else: return 0
   
##Ignore this, you dont need to worry about this
#Well, you can actually take a little time to look at it and learn something
  
  def onMessage(self, room, user, message):
   try:
    msgdata = message.body.split(" ",1)
    if len(msgdata) > 1:
      cmd, args = msgdata[0], msgdata[1]
    else:
      cmd, args = msgdata[0],""
      cmd=cmd.lower() 
    global lockdown
    global newnum
    print(user.name+" - "+message.body)
    if user.name in notif:
        room.message(user.name+", you got ("+str(len(sn[user.name]))+") messages unread. Do irn to read them")
        notif.remove(user.name)
    if user == self.user: return
    if "bot" == message.body:
     if self.getAccess(user) >= 0 or room.getLevel(user) > 0 and not user.name in blacklist: 
      room.message (random.choice(["yes "+sntonick(user.name)+ "-san ? ", "hello "+sntonick(user.name)+"-san"]),True)
    if "malam" == message.body:
     if self.getAccess(user) >= 0 or room.getLevel(user) > 0 and not user.name in blacklist: 
      room.message("Selamat malam"+ " ^o^ ")
    if "pagi" == message.body:
     if self.getAccess(user) >= 0 or room.getLevel(user) > 0 and not user.name in blacklist: 
      room.message("Selamat pagi"+ " ^o^ ")
    if "siang" == message.body:
     if self.getAccess(user) >= 0 or room.getLevel(user) > 0 and not user.name in blacklist: 
      room.message("selamat siang "+sntonick(user.name)+ " ^o^ "),True
    if "sore" == message.body:
     if self.getAccess(user) >= 0 or room.getLevel(user) > 0 and not user.name in blacklist:
      room.message("Selamat sore"+ " ^o^ ")
    if "afk" in message.body:
     if self.getAccess(user) >= 0 or room.getLevel(user) > 0 and not user.name in blacklist: 
      room.message (random.choice(["See ya "+sntonick(user.name)+" :) ",]),True)
    if "brb" in message.body:
     if self.getAccess(user) >= 0 or room.getLevel(user) > 0 and not user.name in blacklist:
      room.message (random.choice(["Bye "+sntonick(user.name)+" :) ",]),True)
    if message.body == "": return  
    if message.body[0] in ["¬"]:   
      data = message.body[1:].split(" ", 1)
      if len(data) > 1:
        cmd, args = data[0], data[1]
      else:
        cmd, args = data[0], ""
        try:
          if message.ip in whois:
              if user.name not in whois[message.ip]:
                whois[message.ip].append(user.name)
              else:
                whois[message.ip] = list()
                whois[message.ip].append(user.name)
                f = open('whois.txt','w')
                for ip in whois:
                  try:
                    names = whois[ip]
                    f.write(json.dumps([ip, names])+"\n")
                  except:pass
                f.close()
        except:pass
 
   
    
    ##check access and ignore
      if self.getAccess(user) == -1: return 
      def pars(args):
        args=args.lower()
        for name in room.usernames:
          if args in name:return name    
      def roompars(args):
        args = args.lower()
        for name in self.roomnames:
          if args in name:return name
      def roomUsers():
          usrs = []
          gay = []
          prop = 0
          prop = prop + len(room._userlist) - 1
          for i in room._userlist:
            i = str(i)
            usrs.append(i)
          while prop >= 0:
            j = usrs[prop].replace("<User: ", "")
            i = j.replace(">", "")
            gay.append(i)
            prop = prop - 1
          return gay
      
      def getParticipant(arg):
          rname = self.getRoom(arg)
          usrs = []
          gay = []
          finale = []
          prop = 0
          prop = prop + len(rname._userlist) - 1
          for i in rname._userlist:
            i = str(i)
            usrs.append(i)
          while prop >= 0:
            j = usrs[prop].replace("<User: ", "")
            i = j.replace(">", "")
            gay.append(i)
            prop = prop - 1
          for j in gay:
            if j not in finale:
              finale.append(j)
          return finale
          
        
      #Find
      if cmd == "find" and len(args) > 0:
        name = args.split()[0].lower()
        if not ch.User(name).roomnames:
          room.message("aku tidak tau")
        else:
          room.message("kamu dapat menemukan  %s Di %s" % (args, ", ".join(ch.User(name).roomnames)),True)

      ##whois
      if cmd == "whois":
        name = args
        possible = list()
        for i in whois:
          if name in whois[i]:
            for j in whois[i]:
              if j not in possible:
                possible.append(j)
        room.message("Possible aliases of %s: %s" %(name, ", ".join(possible)))
      ##cmds
      if cmd == "cmds":
        room.message("<br/>"+user.name+" Rank [...] "+"<br/>"+" Prefixo[ <b>°</b> ] :<br/>wl , <b>gs</b>(Google search) , <b>yt</b>(Youtube) , <b>df</b>(define) , <b>udf</b>(undefine) , fax , bc , <b>sn</b>(sendnote) , <b>rn</b>(readnote) , join , leave , mydict, nick , staff ,  setnick , mynick , seenick , profile , rank , myrank , ranker ,",True)
        if user.name in owners and not user.name in admin and not user.name in archknight and not user.name in whitelist:
          room.message("<br/>"+user.name+" Rank 4 [Owner] "+"<br/>"+" Prefixo[ <b>°</b> ] :<br/>wl , <b>gs</b>(Google search) , <b>yt</b>(Youtube) , <b>df</b>(define) , <b>udf</b>(undefine) , fax , bc , <b>sn</b>(sendnote) , <b>rn</b>(readnote) , join , leave , mydict, nick , staff ,  setnick , mynick , seenick , profile , rank , myrank , ranker ,",True)
        if user.name in admin and not user.name in owners and not user.name in archknight and not user.name in whitelist:
          room.message("<br/>"+user.name+" Rank 3 [Admin] "+"<br/>"+" Prefixo[ <b>°</b> ] :<br/>wl , <b>gs</b>(Google search) , <b>yt</b>(Youtube) , <b>df</b>(define) , <b>udf</b>(undefine) , fax , bc , <b>sn</b>(sendnote) , <b>rn</b>(readnote) , join , leave , mydict, nick , staff , setnick , mynick , seenick , profile , rank , myrank , ranker ,",True) 
        if user.name in archknight and not user.name in owners and not user.name in admin and not user.name in whitelist:
          room.message("<br/>"+user.name+" Rank 2 [Archknight] "+"<br/>"+" Prefixo[ <b>°</b> ] :<br/>wl , <b>gs(Google search) , <b>yt</b>(Youtube) , <b>df</b>(define) , <b>udf</b>(undefine) , fax , bc , <b>sn</b>(sendnote) , <b>rn</b>(readnote) , join , leave , mydict, nick , staff , setnick , mynick , seenick , profile , rank , myrank , ranker ,",True)
        if user.name in whitelist and not user.name in owners and not user.name in admin and not user.name in archknight:
          room.message("<br/>"+user.name+" Rank 1 [Whitelist] "+"<br/>"+" Prefixo[ <b>°<b/> ] :<br/>wl , <b>gs</b>(Google search) , <b>yt</b>(Youtube) , <b>df</b>(define) , <b>udf</b>(undefine) , fax , bc , <b>sn</b>(sendnote) , <b>rn</b>(readnote) , join , leave , mydict, nick , staff , setnick , mynick , seenick , profile , rank , myrank , ranker ,",True)
        
  
      ##Setnick
      if cmd == "setnick":
        if self.getAccess(user) < 4:return
        try:
          if args:
            user, nick = args.split(" ",1)
            nicks[user]=json.dumps(nick)
            room.message("Sukses")
            f = open("nicks.txt","w")
            for user in nicks:
              nick = json.loads(nicks[user])
              f.write(json.dumps([user,nick])+"\n")
            f.close()
          else:
            room.message("Who?")
        except:
          room.message("The nick please")

              
      ##Setrank
      if cmd == "setrank": 
        if self.getAccess(user) < 4:return
        try:
          if len(args) >= 3:
            name = args
            if pars(name) == None:
                name = name
            elif pars(name) != None:
                name = pars(name)
            name, rank = args.lower().split(" ", 1)
            if rank == "4":
              owners.append(name)
              f = open("owners.txt", "w")
              f.write("\n".join(owners))
              f.close()
              room.message("Sukses")
              if name in admin:
                admin.remove(name)
                f = open("admin.txt", "w")
                f.write("\n".join(admin))
                f.close()
              if name in archknight:
                archknight.remove(name)
                f = open("archknight.txt", "w")
                f.write("\n".join(archknight))
                f.close()
              if name in whitelist:
                whitelist.remove(name)
                f = open("whitelist.txt", "w")
                f.write("\n".join(whitelist))
                f.close()
            if rank == "3":
              admin.append(name)
              f = open("admin.txt", "w")
              f.write("\n".join(admin))
              f.close()
              room.message("Sukses")
              if name in owners:
                owners.remove(name)
                f = open("owners.txt", "w")
                f.write("\n".join(owners))
                f.close()
              if name in archknight:
                archknight.remove(name)
                f = open("archknight.txt", "w")
                f.write("\n".join(archknight))
                f.close()
              if name in whitelist:
                whitelist.remove(name)
                f = open("whitelist.txt", "w")
                f.write("\n".join(whitelist))
                f.close()
            if rank == "2":
               archknight.append(name)
               f = open("archknight.txt", "w")
               f.write("\n".join(archknight))
               f.close()
               room.message("Sukses")
               if name in owners:
                 owners.remove(name)
                 f = open("owners.txt", "w")
                 f.write("\n".join(owners))
                 f.close()
               if name in admin:
                 admin.remove(name)
                 f = open("admin.txt", "w")
                 f.write("\n".join(admin))
                 f.close()
               if name in whitelist:
                 whitelist.remove(name)
                 f = open("whitelist.txt", "w")
                 f.write("\n".join(whitelist))
                 f.close()
            if rank == "1":
                whitelist.append(name)
                f = open("whitelist.txt", "w")
                f.write("\n".join(whitelist))
                f.close()
                room.message("Sukses")
                if name in owners:
                  owners.remove(name)
                  f = open("owners.txt", "w")
                  f.write("\n".join(owners))
                  f.close()
                if name in admin:
                  admin.remove(name)
                  f = open("admin.txt", "w")
                  f.write("\n".join(admin))
                  f.close()
                if name in archknight:
                  archknight.remove(name)
                  f = open("archknight.txt", "w")
                  f.write("\n".join(archknight))
                  f.close()
                  
        except:
              room.message("something wrong")

     # clear
      elif cmd == "clear":
          if room.getLevel(self.user) > 0:
            if self.getAccess(user) >= 4 or room.getLevel(user) == 2:
              room.clearall(),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
            else: room.message("Only rank 4+ or the room owner can do this")
          else:
            room.message("aku bukan mods disini :|")
      ##delete chat  
      elif (cmd == "delete" or cmd == "dl" or cmd == "del"):
          if room.getLevel(self.user) > 0:
            if self.getAccess(user) >= 1 or room.getLevel(user) > 0:
              name = args.split()[0].lower()
              room.clearUser(ch.User(name))
            else:room.message("kamu tidak bisa melakukannya!!")
          else:
            room.message("aku bukan mods disini :|")

      ##fax
      if cmd == "fax":
        if self.getAccess(user) >= 1:
          if len(args) > 1:
            try:
              target, body = args.split(" ", 1)
              if user.name in room.modnames or user.name in room.ownername or self.getAccess(user) > 2:
                if target in self.roomnames:
                  if room.name == "dai-tenshi":
                    self.getRoom(target).message("Fax from <b>%s</b> [via <font color='#ff0000'><b>%s</b></font> Fax] - <font color='#3300FF'>%s</font>" % (sntonick(user.name), "Heaven", body), True)
                    room.message("[<b>%s</b>] Fax Sent" % "INF", True)
                  else:
                    self.getRoom(target).message("Fax from <b>%s</b> [via <font color='#ff0000'><b>%s</b></font> Fax] - <font color='#3300FF'>%s</font>" % (sntonick(user.name), room.name, body), True)
                    room.message("[<b>%s</b>] Fax Sent" % "INF", True)
                else:
                  room.message("[<b>%s</b>] There's no Fax Service in <font color='#ff0000'><b>%s</b></font> :|" % ("ERROR", target), True)
              else:
                room.message("You mere mortals can never do that !!")
                self.setTimeout(int(3), room.message, "*Aims Colt. Python Revolver at <b>%s</b> and shot him dead*" % user.name, True)
            except:
              room.message("Gagal !!")     
          


      ##Ranker
      if cmd == "ranker":
        room.message("<br/><f x120000FF='0'><b>Owner:</b></f> %s<br/><f x12FF0000='0'><b>Admin:</b></f> %s<br/><f x12FF00FF='0'><b>ArchKnight:</b></f>%s" % (", ".join(owners), ", ".join(admin), ", ".join(archknight)),True)
      ##staff
      if cmd == "staff":
        room.message("<br/><f x120000FF='0'><b>Owner:</b></f> %s<br/><f x12FF0000='0'><b>Admin:</b></f> %s" % (", ".join(owners), ", ".join(admin)),True)

  
      ##GS
      if cmd == "gs": 
        room.message(gs(args),True)    

      if cmd == "pfpic":
                link = "http://fp.chatango.com/profileimg/%s/%s/%s/full.jpg" % (args[0], args[1], args)
                room.message("<br/>"+"User ID : "+args+""+"<br/>Profile Picture :<br/>"+link,True)    
    ##Eval
      if cmd == "ev" or cmd == "eval" or cmd == "e":
        if self.getAccess(user) == 4:
          ret = eval(args)
          if ret == None:
            room.message("Done.")
            return
          room.message(str(ret))

      ##Say
      if cmd == "say":
        room.message(args)

      ##Random User
      if cmd == "randomuser":
        room.message(random.choice(room.usernames))

     

          
        ##Check if Mod
	#not really important
      elif cmd == "ismod":
        user = ch.User(args)
        if room.getLevel(user) > 0:
          room.message("yesh")
        else:
          room.message("nope")

      ## Youtube
      elif cmd == "youtube" or cmd == "yt":
        if args:
          room.message(tube(args),True)
     
      ## Broadcast
      elif cmd=="bc":
          r = room.name
          l = "http://ch.besaba.com/mty.htm?"+r+"+"
          for room in self.rooms:
            room.message("[<font color='#6699CC'><b>Broadcast</b></font>] from - "+sntonick(user.name)+ " : <font color='#33FF33'><i>"+args+"<i></font>", True)              
    ###### Define            
      elif cmd == "define" or cmd == "df" and len(args) > 0:
          try:
            try:
              word, definition = args.split(" as ",1)
              word = word.lower()
            except:
              word = args
              definition = ""
            if len(word.split()) > 4:
              room.message("Fail")
              return
            elif len(definition) > 0:
              if word in dictionary:
                room.message("%s defined already" % user.name.capitalize())
              else:
                dictionary[word] = json.dumps([definition, user.name])
                f =open("definitions.txt", "w")
                for word in dictionary:
                  definition, name = json.loads(dictionary[word])
                  f.write(json.dumps([word, definition, name])+"\n")
                f.close
                room.message("Definition Saved")
            else:
              if word in dictionary:
                definition, name = json.loads(dictionary[word])
                room.message("<br/>ID : %s<br/>Keyword : %s<br/>Definition:<br/>%s" % (name, word, definition),True)
              else:
                room.message(args+" is not defined")
          except:
            room.message("something wrong")
                
      elif cmd == "rank":
        if not args:
            if user.name in owners and not user.name in whitelist:
              room.message(user.name+" Kamu Rank 4 [Owner] ",True)
            elif user.name in admin and not user.name in whitelist and not user.name in archknight and not user.name in owner:
              room.message(user.name+" Kamu Rank 3 [Admin] ",True)  
            elif user.name in archknight and not user.name in whitelist and not user.name in owners and not user.name in admin:  
              room.message(user.name+" Kamu Rank 2 [Arckhnight]",True)
            elif user.name in whitelist and not user.name in owners:
              room.message(user.name+" Kamu Rank 1 [Whitelist]",True)
            elif user.name not in whitelist and not user.name not in archknight and user.name not in admin and user.name not in owners:
              room.message(user.name+" Kamu Belum terdaftar",True)
        if args:
              sss = args
              if sss in owners:
                  room.message(sss.title()+" Rank Dia 4 [Owner] ",True)
              if sss in admin:
                  room.message(sss.title()+" Rank Dia 3 [Admin] ",True)
              if sss in archknight:
                  room.message(sss.title()+" Rank Dia 2 [Arckhnight] ",True)
              if sss in whitelist:
                  room.message(sss.title()+" rank Dia 1 [Whitelist] ",True)   
              if sss not in owners and sss not in admin and sss not in archknight and sss not in whitelist:
                  room.message(sss.title()+" Tidak ada rank :) ")
  

    ##### Whitelist
      elif cmd == "wl" and self.getAccess(user) >= 0:
        name = args
        if name not in whitelist and name not in owners and name not in admin and name not in archknight and name not in blacklist:
          room.message("Sukses")
          whitelist.append(name)
          f = open("whitelist.txt","w")
          f.write("\n".join(whitelist))
          f.close
        else:
          room.message("User tersebut sudah terdaftar")
    
     ###blacklist
      elif cmd == "bl" and self.getAccess(user) >= 3:
        name = args
        if name not in whitelist and name not in owners and name not in admin and name not in archknight:
          room.message("Done")
          blacklist.append(name)
          f = open("blacklist.txt","w")
          f.write("\n".join(blacklist))
          f.close
        else:
          room.message("User tersebut sudah di blacklist")

      ##ubl
      if cmd == "ubl" and self.getAccess(user) >= 3:
        try:
          if args in blacklist:
            blacklist.remove(args)
            f = open("blacklist.txt","w")
            f.write("\n".join(blacklist))
            f.close()
            room.message("Sukses")
        except:
          room.message("Gagal")
            
      ##uwl
      if cmd == "uwl" and self.getAccess(user) >= 3:
        try:
          if args in owners:
            owners.remove(args)
            f = open("owners.txt","w")
            f.write("\n".join(owners))
            f.close()
            room.message("Sukses")
          if args in admin:
            admin.remove(args)
            f = open("admin.txt","w")
            f.write("\n".join(admin))
            f.close()
            room.message("Sukses")
          if args in archknight:
            archknight.remove(args)
            f = open("archknight.txt","w")
            f.write("\n".join(archknight))
            f.close()
            room.message("Sukses")
          if args in whitelist:
            whitelist.remove(args)
            f = open("whitelist.txt","w")
            f.write("\n".join(whitelist))
            f.close()
            room.message("Sukses")  
        except:
          room.message("Gagal")
        
      if cmd== "sbg":
            if self.getAccess(user) >= 3:
              if len(args) > 0:
                  if args == "on":
                    room.setBgMode(1)
                    room.message("Background On")
                    return
                  if args == "off":
                    room.setBgMode(0)
                    room.message("Background Off")
      elif cmd == "mydict":
          arr = []
          for i in dictionary:
            if user.name in dictionary[i]:
              arr.append(i)
          if len(arr) > 0:
            room.message("You have defined <b>"+str(len(arr))+"</b> words in your dictionary :<i> %s"% (', '.join(sorted(arr))), True)
          else:
            room.message("kamu tidak memiliki dictionary.")
    # yt
      elif cmd == "gis":
        word = args\
                .replace(" ", "+")
        word = re.sub('[^A-Za-z0-9]+', '', word)
        if self.getAccess(user)>=0: room.message(gis(args),True)


      if cmd == "tli":
        args = quote(args)
        room.message(tli(args, dtl(args)))

      if cmd == "tip":
        args = quote(args)
        room.message(tip(args, dtl(args)))

      if cmd == "tle":
        args = quote(args)
        room.message(tle(args, dtg(args)))

      if cmd == "tlp":
        args = quote(args)
        room.message(tlp(args, dtg(args)))

      if cmd == "tpj":
        args = quote(args)
        room.message(tlj(args, dtg(args)))

      if cmd == "tjp":
        args = quote(args)
        room.message(tjp(args, dtg(args)))

      if cmd == "udf" and len(args) > 0:
          try:
            word = args
            if word in dictionary:
              definition, name = json.loads(dictionary[word])
              if name == user.name or self.getAccess(user) >= 3:
                del dictionary[word]
                f =open("definitions.txt", "w")
                for word in dictionary:
                  definition, name = json.loads(dictionary[word])
                  f.write(json.dumps([word, definition, name])+"\n")
                f.close
                room.message(args+" has been removed from Definition database")
                return
              else:
                room.message("<b>%s</b> you can not remove this define only masters or the person who defined the word may remove definitions" % user.name, True)
                return
            else:
               room.message("<b>%s</b> is not yet defined you can define it by typing <b>define %s: meaning</b>" % args, True)
          except:
            room.message("Gagal")
            return
            
      elif cmd == "sdf" or cmd == "seedict":
          if not args:
            room.message("Whose dict do you want to see ?")
            return
          args = args.lower()
          if pars(args) == None:
            args = args.lower()
          if pars(args) != None:
            args = pars(args)
          arr = []
          for i in dictionary:
            if args in dictionary[i]:
              arr.append(i)
          if len(arr) > 0:
            room.message("<b>"+args.title()+"</b> have defined <b>"+str(len(arr))+"</b> words in his dictionary :<i> %s"% (', '.join(sorted(arr))), True)
          else:
            room.message(args.title()+" defined nothing.")

      if cmd == "seenick":
            try:
              if args in nicks:
                room.message(args+" Nick Dia : "+sntonick(args)+"", True)
              else:
                room.message(args+" Belum membuat nick di aku :|")
            except:
              return      

      elif cmd == "prof" or cmd == "profile" or cmd == "Prof" or cmd == "Profile":
          try:
            args=args.lower()
            stuff=str(urlreq.urlopen("http://"+args+".chatango.com").read().decode("utf-8"))
            wl = args.lower() in whitelist
            white = ""
            resp = urlreq.urlopen("http://"+args+".chatango.com").read().decode()
            fap = bool('chat with' in resp.lower())
            fapper = ""
            crap, age = stuff.split('<span class="profile_text"><strong>Age:</strong></span></td><td><span class="profile_text">', 1)
            age, crap = age.split('<br /></span>', 1)
            crap, gender = stuff.split('<span class="profile_text"><strong>Gender:</strong></span></td><td><span class="profile_text">', 1)
            gender, crap = gender.split(' <br /></span>', 1)
            if fap == True:
              fapper += "<f x1233FF33='1'>Online</f><f xc0c0c0='1'>"
            if fap == False:
              fapper += "<f x12FF0000='1'>Offline</f><f xc0c0c0='1'>"
            if wl == True:
              white += " <f x1233FF33='1'>Yes</f><f xc0c0c0='1'> "
            if wl == False:
              white += " <f x12FF0000='1'>No</f><f xc0c0c0='1'> "
            if gender == 'M':
                gender = 'Laki - Laki'
            elif gender == 'F':
                gender = 'Perempuan'
            else:
                gender = '?'
            crap, location = stuff.split('<span class="profile_text"><strong>Location:</strong></span></td><td><span class="profile_text">', 1)
            location, crap = location.split(' <br /></span>', 1)
            crap,mini=stuff.split("<span class=\"profile_text\"><!-- google_ad_section_start -->",1)
            mini,crap=mini.split("<!-- google_ad_section_end --></span>",1)
            mini=mini.replace("<img","<!")
            picture = '<a href="http://fp.chatango.com/profileimg/' + args[0] + '/' + args[1] + '/' + args + '/full.jpg" style="z-index:59" target="_blank">http://fp.chatango.com/profileimg/' + args[0] + '/' + args[1] + '/' + args + '/full.jpg</a>'
            prodata = '<br/><br/><a href="http://chatango.com/fullpix?' + args + '" target="_blank">' + picture + '<br/><br/>''<b>Nama</b>: '+ args.capitalize() +'<br/>  <b>Umur</b>: '+ age + ' <br/> <b>Jenis Kelamin</b>: ' + gender +  ' <br/> <b>Lokasi</b>: ' +  location + ' <br/> <b>Html</b>: http://barrykun.com/?'+  args + ' <br/><b>Whitelist?</b>: ' + white + ' <br/><b>Status</b>: '+ fapper +'<br/> <a href="http://' + args + '.chatango.com" target="_blank"><u>Chat With User</u></a> ' '<br/><br/><b>'
            room.message(prodata,True)
          except:
            room.message(""+args+" not found ")
      elif cmd=="mini":
        try:
          args=args.lower()
          stuff=str(urlreq.urlopen("http://"+args+".chatango.com").read().decode("utf-8"))
          crap,mini=stuff.split("<span class=\"profile_text\"><!-- google_ad_section_start -->",1)
          mini,crap=mini.split("<!-- google_ad_section_end --></span>",1)
          mini=mini.replace("<img","<!")
          prodata = '<br/>'+mini
          room.message(prodata,True)
        except:
          room.message(""+args+" doesn't exist o.o ")

      if cmd == "bgimg":
        try:
          args=args.lower()
          picture = '<a href="http://st.chatango.com/profileimg/' + args[0] + '/' + args[1] + '/' + args + '/msgbg.jpg" style="z-index:59" target="_blank">http://fp.chatango.com/profileimg/' + args[0] + '/' + args[1] + '/' + args + '/msgbg.jpg</a>'
          prodata = '<br/>'+picture
          room.message("<br/>"+"User ID : "+args+"<br/>Background :"+prodata,True)
        except:
          room.message(""+args+" doesn't exist:'v")
        #MalCommand
      elif cmd == "malinfo":
         anime = myanimelistanime(args)
         room.message(anime,True)

      elif cmd == "mal2info":
         manga = myanimelistmanga(args)
         room.message(manga,True)

      elif cmd == "mal":
         anime = myanimelist1(args)
         room.message(anime,True)

      elif cmd == "mal2":
         manga = myanimelist2(args)
         room.message(manga,True)
          

    ### Private Messages
      elif cmd=="pm":
        data = args.split(" ", 1)
        if len(data) > 1:
          name , args = data[0], data[1]
          self.pm.message(ch.User(name), "[Private.Message] By - "+user.name+" : "+args+" ")
          room.message("Sent to "+name+"")
    ### Sentnote
      elif cmd == "inbox":
          if user.name in sn:
            mesg = len(sn[user.name])
            room.message("["+str(mesg)+"] messages in your inbox. To read it, do irn")
          else:
            sn.update({user.name:[]})
            mesg = len(sn[user.name])
            room.message("["+str(mesg)+"] messages in your inbox. To read it, do irn")


        #send notes
      elif cmd == "sn" or cmd == "sendnote":
          args.lower()
          untuk, pesan = args.split(" ", 1)
          if untuk[0] == "+":
                  untuk = untuk[1:]
          else:
                  if pars(untuk) == None:
                    room.message("Who is "+untuk+" ??")
                    return
                  untuk = pars(untuk)
          if untuk in sn:
            sn[untuk].append([user.name, pesan, time.time()])
            if untuk not in notif:
              notif.append(untuk)
            else:pass
          else:
            sn.update({untuk:[]})
            sn[untuk].append([user.name, pesan, time.time()])
            if untuk not in notif:
              notif.append(untuk)
            else:pass
          room.message('Sent to %s'% (untuk)+"'s inbox" , True)
				


        #Read Notes
      elif cmd =="rn" or cmd =="readnote":
          if user.name not in sn:
            sn.update({user.name:[]})
          user=user.name.lower()
          if len(sn[user]) > 0:
            messg = sn[user][0]
            dari, pesen, timey = messg
            timey = time.time() - int(timey)
            minute = 60
            hour = minute * 60
            day = hour * 24
            days =  int(timey / day)
            hours = int((timey % day) / hour)
            minutes = int((timey % hour) / minute)
            seconds = int(timey % minute)
            string = ""
            if days > 0:
              string += str(days) + " " + (days == 1 and "day" or "days" ) + ", "
            if len(string) > 0 or hours > 0:
              string += str(hours) + " " + (hours == 1 and "hour" or "hours" ) + ", "
            if len(string) > 0 or minutes > 0:
              string += str(minutes) + " " + (minutes == 1 and "minute" or "minutes" ) + ", "
            string += str(seconds) + " " + (seconds == 1 and "second" or "seconds" )
            room.message("[<font color='#6699CC'><b>Private Message</b></font>] from - "+sntonick(dari)+" : "+pesen+"  (<font color='#9999FF'>"+string+" ago </font>)", True)
            try:
              del sn[user][0]
              notif.remove(user)
            except:pass
          else:room.message('%s'%(user)+" you don't have any messages in your inbox" , True)
   ###### leave + room 
      elif cmd == "leave"  and self.getAccess(user) >=1:
        if not args:args=room.name
        self.leaveRoom(args)
        room.message("Baik aku out "+args+" ...")
        print("[SAVE] SAVING Rooms...")
        f = open("rooms.txt", "w")
        f.write("\n".join(self.roomnames))
        f.close()

    ###### join room + roomname

      if cmd == "join" and len(args) > 1:
          if self.getAccess (user) >= 1:
              if args not in self.roomnames:
                room.message("Baik aku join ke "+args+" ...")
                self.joinRoom(args)
              else:
                room.message("aku sudah ada disana ...")
              print("[SAVE] SAVING Rooms...")
              f = open("rooms.txt", "w")
              f.write("\n".join(self.roomnames))
              f.close()
      elif cmd == "userlist":
         if args == "":
          usrs = []
          gay = []
          finale = []
          prop = 0
          prop = prop + len(room._userlist) - 1
          for i in room._userlist:
            i = str(i)
            usrs.append(i)
          while prop >= 0:
            j = usrs[prop].replace("<User: ", "")
            i = j.replace(">", "")
            gay.append(i)
            prop = prop - 1
          for i in gay:
            if i not in finale:
              finale.append(i)
          if len(finale) > 40:
            room.message("<font color='#9999FF'><b>40</b></font> of <b>%s</b> users in this room: %s"% (len(finale), ", ".join(finale[:41])), True)
          if len(finale) <=40 :
            room.message("Current <b>%s</b> users of this room: %s"% (len(finale),", ".join(finale)), True)
         if args != "":
           if args not in self.roomnames:
             room.message("I'm not there.")
             return
           users = getParticipant(str(args))
           if len(users) > 40:
             room.message("<font color='#9999FF'><b>40</b></font> of <b>%s</b> current users in <b>%s</b>: %s"% (len(users), args.title(), ", ".join(users[:41])), True)
           if len(users) <=40:
             room.message("Current <b>%s</b> users in <b>%s</b>: %s"% (len(users), args.title(), ", ".join(users)), True) 
    ##### bot rooms
      elif cmd == "rooms" : 
        j = [] 
        for i in self.roomnames: 
          j.append(i+'[%s]' % str(self.getRoom(i).usercount)) 
          j.sort() 
        room.message("aku bermain Di "+'[%s] rooms: '%(len(self.roomnames))+", ".join(j))
      ## Mods
      elif cmd == "mods":
          args = args.lower()
          if args == "":
            room.message("<font color='#ffffff'><b>Room</b>: "+room.name+" <br/><b>Owner</b>: <u>"+ (room.ownername) +"</u> <br/><b>Mods</b>: "+", ".join(room.modnames), True)
            return
          if args in self.roomnames:
              modask = self.getRoom(args).modnames
              owner = self.getRoom(args).ownername
              room.message("<font color='#ffffff'><b>Room</b>: "+args+" <br/><b>Owner</b>: <u>"+ (owner) +"</u> <br/><b>Mods</b>: "+", ".join(modask), True)
  

        # Nick
      elif (cmd == "nick"):
        try:
          if args:
            nicks[user.name]=json.dumps(args)
            room.message (user.name+" will now be called "+args ,True)
            saveNicks()
          if args == "":
             room.message("type +nick (your-new-nickname-here)")
        except:
          room.message("Failed to create a nickname for "+user.name+".")

      elif cmd == "mynick":
        try:
          if user.name in nicks:
            room.message("Your current nick is "+sntonick(user.name)+" :3", True)
          else:
             room.message("You haven't told me your nick, do +nick new-nick-here to make your nick")
        except:
          return
          
      elif cmd == "seenick":
        try:
          if args in nicks:
            room.message(args+"'s nickname is "+sntonick(args)+" xD", True)
          else:
            room.message(args+" haven't told me his nick :|")
        except:
          return
  ## Aisatsu or Greetings
    msgd = message.body.split(" ", 1 )
    if len(msgd) > 1:
     cmd, args = msgd[0], msgd[1] # if command and args
    else:
     cmd, args  = msgd[0], "" # if command and no args
    cmd=cmd.lower()
    if "rea" in message.body and args:  
                  if len(args) > 1:
                     room.message(__import__("simsimi").SimSimi(args)) 
                  else:
                    room.message("What "+sntonick(user.name)+" ?", True)
    if "Rea" in message.body and args:  
                  if len(args) > 1:
                     room.message(__import__("simsimi").SimSimi(args)) 
                  else:
                    room.message("What "+sntonick(user.name)+" ?", True)

    if "rea" == message.body and not args:
                  room.message(random.choice(["O que foi "+sntonick(user.name)+"-san ?","Oi "+sntonick(user.name)+"-san"]), True)

    if "Rea" == message.body and not args:
                  room.message(random.choice(["O que foi "+sntonick(user.name)+"-san ?","Oi "+sntonick(user.name)+"-san"]), True)

    if "@Reabot" == message.body and not args:
                  room.message(random.choice(["O que foi "+sntonick(user.name)+"-san ?","Oi "+sntonick(user.name)+"-san"]), True)

    if "@Reabot " == message.body and not args:
                  room.message(random.choice(["O que foi "+sntonick(user.name)+"-san ?","Oi "+sntonick(user.name)+"-san"]), True)

    if "reabot" == message.body and not args:
                  room.message(random.choice(["O que foi "+sntonick(user.name)+"-san ?","Oi "+sntonick(user.name)+"-san"]), True)

    if "Reabot" == message.body and not args:
                  room.message(random.choice(["O que foi "+sntonick(user.name)+"-san ?","Oi "+sntonick(user.name)+"-san"]), True)

   except Exception as e:
      try:
        et, ev, tb = sys.exc_info()
        lineno = tb.tb_lineno
        fn = tb.tb_frame.f_code.co_filename
        room.message("[Expectation Failed] %s Line %i - %s"% (fn, lineno, str(e)))
        return
      except:
        room.message("Undescribeable error detected !!")
        return


  ##Other Crap here, Dont worry about it
  
  def onFloodWarning(self, room):
    room.reconnect()
  
  def onJoin(self, room, user):
   print(user.name + " joined the chat!")
  
  def onLeave(self, room, user):
   print(user.name + " left the chat!")
  
  def onUserCountChange(self, room):
    print("users: " + str(room.usercount))
  

        

if __name__ == "__main__":
  TestBot.easy_start(rooms, botname, password)

