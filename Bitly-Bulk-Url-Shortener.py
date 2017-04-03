#Created by c0ldsnap
#First Github upload ever!
#Github https://github.com/c0ldsnap/Bitly-Bulk-Url-Shortener
#Python 2.7


import requests
import json
import time
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

start = time.time() #Starts Timer

#File Handling
shorty = open("shorty.txt","w") #Output File which to write shortened Links
link_file = open("long_urls.txt","r") #Reads file line by line with Long Urls
links = link_file.readlines()
link_file.close()


token = "" #Put Your Auth Token Here.
county = 0
for link in links:
    link = link.strip()
    print "Shortening Link -> " + link

    endpoint = "https://api-ssl.bitly.com/v3/shorten"
    query_params = {"access_token": token,"longUrl": link}
    response = requests.get(endpoint, params=query_params, verify=False) #Call to api with api token
    data = json.loads(response.content)

    try:
        #print data
        short_link = data["data"]["url"] #Grabs Shortlink from json
        print "Shortened Link -> " + short_link
        shorty.write(short_link + "\n")
        shorty.flush()
        county+=1
    except Exception,e:
        print e
        print "[-] Error [-] => " + link

    print "Total -> ", county

shorty.close()
print "Done Shortened a Total of %d links in %d seconds" % (county, start - time.time())
