import os
import re
import random
import sys
import json
import time
import datetime
import base64

if sys.version_info[0] < 3:
  class urllib:
    parse = __import__("urllib")
    request = __import__("urllib2")
  input = raw_input
  import codecs
  import Queue as queue
  class http:
    client = __import__("httplib")
else:
  import http.client
  import queue
  import urllib.request
  import urllib.parse

def toTime(data):
  try:
    year, month, day = data.split("-")
  except:
    year, month, day = "0000", "00", "00"
  year, month, day = int(year), int(month), int(day)
  try:
    return datetime.date(year, month, day).strftime("%A %d. %B %Y")
  except:
    try:
      return datetime.date(year, month , 1).strftime("%B %Y")
    except:
      try:
        return datetime.date(year, 1, 1).strftime("%Y")
      except:
        return "?"
        
def getInfoAnime(anime):
    header = {
    'Content-Type':'application/x-www-form-urlencoded',
    'Host':'myanimelist.net',
    'Origin':'http://myanimelist.net',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.22 Safari/537.36'
    }
    conn = http.client.HTTPConnection("myanimelist.net")
    conn.request("POST", "/anime/%s" % anime , None, header)
    url = conn.getresponse().read().decode().replace('\r','').replace('\n','').replace('\t','')
    try:
      duration = re.search('<div><span class="dark_text">Duration:</span>(.*?)</div>', url).group(1)
    except:
      duration = ""
    try:
      rating = re.search('<div class="spaceit"><span class="dark_text">Rating:</span>(.*?)</div>', url).group(1)
    except:
      rating = ""
    try:
      genre = re.search('<div class="spaceit"><span class="dark_text">Genres:</span>(.*?)</div>', url).group(1)
      genres = "".join(re.findall('>(.*?)<',genre))
    except:
      genres = ""
    try:
      producer = re.search('<div><span class="dark_text">Producers:</span>(.*?)</div>', url).group(1)
      producers = "".join(re.findall('>(.*?)<', producer))
    except:
      producer = ""
    try:
      japanese = re.search('<div class="spaceit_pad"><span class="dark_text">Japanese:</span>(.*?)</div>', url).group(1)
    except:
      japanese = ""
    return (japanese[1:], genres ,producers, duration[2:], rating[2:])

def getInfoManga(manga):
    header = {
    'Content-Type':'application/x-www-form-urlencoded',
    'Host':'myanimelist.net',
    'Origin':'http://myanimelist.net',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.22 Safari/537.36'
    }
    conn = http.client.HTTPConnection("myanimelist.net")
    conn.request("POST", "/manga/%s" % manga , None, header)
    url = conn.getresponse().read().decode().replace('\r','').replace('\n','').replace('\t','')
    try:
      genre = re.search('<div class="spaceit"><span class="dark_text">Genres:</span>(.*?)</div>', url).group(1)
      genres = "".join(re.findall('>(.*?)<',genre))
    except:
      genres = ""
    try:
      author = re.search('<div><span class="dark_text">Authors:</span>(.*?)</div>', url).group(1)
      authors = "".join(re.findall('>(.*?)<', author))
    except:
      authors = ""
    try:
      japanese = re.search('<div class="spaceit_pad"><span class="dark_text">Japanese:</span>(.*?)</div>', url).group(1)
    except:
      japanese = ""
    try:
      serialization = re.search('<div class="spaceit"><span class="dark_text">Serialization:</span>(.*?)</div>', url).group(1)
      serializations = "".join(re.findall('>(.*?)<', serialization))
    except:
      serializations = ""
    return (japanese[1:], genres ,authors, serializations)
  
def anime(encoded, v, val):
    encoded = urllib.parse.quote(encoded)
    auth = base64.encodestring(b'justhoax:magenta').decode().replace('\n', '')
    header = {
    'Content-Type':'application/x-www-form-urlencoded',
    'Host':'myanimelist.net',
    'Origin':'http://myanimelist.net',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.22 Safari/537.36',
    'Authorization':'Basic %s' % auth}
    url = urllib.request.Request('http://myanimelist.net/api/anime/search.xml?q=%s'% (encoded), None , header)
    udict = urllib.request.urlopen(url).read().decode()
    udict = udict.replace('\r','').replace('\n','').replace('&lt;br /&gt;','<br />').replace("&amp;quot;",'"')
    id = re.findall("<id>(.*?)</id>", udict, re.S)
    title= re.findall("<title>(.*?)</title>", udict, re.S)
    english = re.findall("<english>(.*?)</english>", udict, re.S)
    synonyms = re.findall("<synonyms>(.*?)</synonyms>", udict, re.S)
    episodes = re.findall("<episodes>(.*?)</episodes>", udict, re.S)
    score = re.findall("<score>(.*?)</score>", udict, re.S)
    type = re.findall("<type>(.*?)</type>", udict, re.S)
    status = re.findall("<status>(.*?)</status>", udict, re.S)
    start_date = re.findall("<start_date>(.*?)</start_date>", udict, re.S)
    end_date = re.findall("<end_date>(.*?)</end_date>", udict, re.S)
    synopsis = re.findall("<synopsis>(.*?)</synopsis>", udict, re.S)
    image = re.findall("<image>(.*?)</image>", udict, re.S)        

    if v == 0:
        entry  = [pair for pair in zip(image,id,title,english,synonyms,episodes,score,type,status,start_date,end_date,synopsis)]
        if val == 0:
            en = entry[0]
            image,id,title,english,synonyms,episodes,score,type,status,start_date,end_date,synopsis = en
            japanese, genres ,producers , duration, rating= getInfoAnime(id)
            en = image,id,title,english,japanese,genres,producers,episodes,score,duration,rating,type,status,toTime(start_date),toTime(end_date),synopsis
            return "%s <b>Id:</b> %s, <b>Title:</b> %s, <b>English:</b> %s, <b>Japanese:</b> %s, <b>Genres:</b> %s, <b>Producers:</b> %s, <b>Episodes:</b> %s, <b>Score:</b> %s, <b>Duration:</b> %s, <b>Rating:</b> %s, <b>Type:</b> %s, <b>Status:</b> %s, <b>Aired:</b> %s to %s, <b>Synopsis:</b> %s" % en
        else:
            en = entry[val]
            image,id,title,english,synonyms,episodes,score,type,status,start_date,end_date,synopsis = en
            japanese, genres ,producers , duration, rating= getInfoAnime(id)
            en = image,id,title,english,japanese,genres,producers,episodes,score,duration,rating,type,status,toTime(start_date),toTime(end_date),synopsis
            return "%s <b>Id:</b> %s, <b>Title:</b> %s, <b>English:</b> %s, <b>Japanese:</b> %s, <b>Genres:</b> %s, <b>Producers:</b> %s, <b>Episodes:</b> %s, <b>Score:</b> %s, <b>Duration:</b> %s, <b>Rating:</b> %s, <b>Type:</b> %s, <b>Status:</b> %s, <b>Aired:</b> %s to %s, <b>Synopsis:</b> %s" % en
    else:
        entry = [pair for pair in zip(title,id,episodes,score,type,status,start_date,end_date)]
        j = []
        num = 1
        rank =  0
        for en in entry:
            if num == val:
                rank = val
            en = "(<b>%s</b>)" % num +"<b>%s</b>(#<b>%s</b>), Eps: %s, Score: <b>%s</b>, Type: <b>%s</b>, Status: <b>%s</b>, Aired: %s to %s" % en
            num = num + 1
            j.append(en)
            
        rank1 = rank - 2
        rank2 = rank + 3
        if rank1 < 0:
          rank2 = rank2 - rank1
          rank1 = 0
        if rank2 > num:
          rank1 = rank1 - (rank2-num)
          if rank1 < 0:
            rank1 = 0

        return "<b>%s</b> results (%s:%s) | Type 'malinfo &lt;your anime&gt; for more info<br/>"% (len(j),rank1+1,rank2)+"<br/>".join(j[rank1:rank2])
    
def manga(encoded, v, val):
    encoded = urllib.parse.quote(encoded)
    auth = base64.encodestring(b'justhoax:magenta').decode().replace('\n', '')
    header = {
    'Content-Type':'application/x-www-form-urlencoded',
    'Host':'myanimelist.net',
    'Origin':'http://myanimelist.net',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.22 Safari/537.36',
    'Authorization':'Basic %s' % auth}
    url = urllib.request.Request('http://myanimelist.net/api/manga/search.xml?q=%s'% (encoded), None , header)
    udict = urllib.request.urlopen(url).read().decode()
    udict = udict.replace('\r','').replace('\n','').replace('&lt;br /&gt;','<br />').replace("&amp;quot;",'"')
    id = re.findall("<id>(.*?)</id>", udict, re.S)
    title= re.findall("<title>(.*?)</title>", udict, re.S)
    english = re.findall("<english>(.*?)</english>", udict, re.S)
    synonyms = re.findall("<synonyms>(.*?)</synonyms>", udict, re.S)
    chapters = re.findall("<chapters>(.*?)</chapters>", udict, re.S)
    volumes = re.findall("<volumes>(.*?)</volumes>", udict, re.S)
    score = re.findall("<score>(.*?)</score>", udict, re.S)
    type = re.findall("<type>(.*?)</type>", udict, re.S)
    status = re.findall("<status>(.*?)</status>", udict, re.S)
    start_date = re.findall("<start_date>(.*?)</start_date>", udict, re.S)
    end_date = re.findall("<end_date>(.*?)</end_date>", udict, re.S)
    synopsis = re.findall("<synopsis>(.*?)</synopsis>", udict, re.S)
    image = re.findall("<image>(.*?)</image>", udict, re.S)        

    if v == 0:
        entry  = [pair for pair in zip(image,id,title,english,synonyms,chapters,volumes,score,type,status,start_date,end_date,synopsis)]
        if val == 0:
            en = entry[0]
            image,id,title,english,synonyms,chapters,volumes,score,type,status,start_date,end_date,synopsis = en
            japanese, genres ,authors, serializations = getInfoManga(id)
            en = image,id,title,english,japanese,genres,authors,serializations,chapters,volumes,score,type,status,toTime(start_date),toTime(end_date),synopsis
            return "%s <b>Id:</b> %s, <b>Title:</b> %s, <b>English:</b> %s, <b>Japanese:</b> %s, <b>Genres:</b> %s, <b>Author:</b> %s, <b>Serialization:</b> %s, <b>Chapters:</b> %s, <b>Volumes:</b> %s, <b>Score:</b> %s, <b>Type:</b> %s, <b>Status:</b> %s, <b>Publishing:</b> %s to %s, <b>Synopsis:</b> %s" % en
        else:
            en = entry[val]
            image,id,title,english,synonyms,chapters,volumes,score,type,status,start_date,end_date,synopsis = en
            japanese, genres ,authors, serializations = getInfoManga(id)
            en = image,id,title,english,japanese,genres,authors,serializations,chapters,volumes,score,type,status,toTime(start_date),toTime(end_date),synopsis
            return "%s <b>Id:</b> %s, <b>Title:</b> %s, <b>English:</b> %s, <b>Japanese:</b> %s, <b>Genres:</b> %s, <b>Author:</b> %s, <b>Serialization:</b> %s, <b>Chapters:</b> %s, <b>Volumes:</b> %s, <b>Score:</b> %s, <b>Type:</b> %s, <b>Status:</b> %s, <b>Publishing:</b> %s to %s, <b>Synopsis:</b> %s" % en
    else:
        entry = [pair for pair in zip(title,id,chapters,score,type,status,start_date,end_date)]
        j = []
        num = 1
        rank =  0
        for en in entry:
            if num == val:
                rank = val
            en = "(<b>%s</b>)" % num +"<b>%s</b>(#<b>%s</b>), Cpt: %s, Score: <b>%s</b>, Type: <b>%s</b>, Status: <b>%s</b>, Aired: %s to %s" % en
            num = num + 1
            j.append(en)
            
        rank1 = rank - 2
        rank2 = rank + 3
        if rank1 < 0:
          rank2 = rank2 - rank1
          rank1 = 0
        if rank2 > num:
          rank1 = rank1 - (rank2-num)
          if rank1 < 0:
            rank1 = 0

        return "<b>%s</b> results (%s:%s) | Type 'mal2info &lt;your manga&gt; for more info<br/>"% (len(j),rank1+1,rank2)+"<br/>".join(j[rank1:rank2])
