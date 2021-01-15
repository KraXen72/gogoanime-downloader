import requests
from bs4 import BeautifulSoup
import os


#CONFIG
quality = "1080P" # 360P or 480P or 720P or 1080P


#ASK from users
print("----------------------------------------------------------")
print("welcome to gogoanime.so batch downloader / link generator.")
print("by default it downloads at 1080P")
print("link example: ")
print("https://gogoanime.so/kanojo-okarishimasu-episode-1")
print("----------------------------------------------------------")
animelink = input("Enter Link of your Anime Series : ")  #User Enters URL
start = int(input("Enter Episode Number to start with : "))
if start <= 0:
	start = 1
end = int(input("Enter Episode Number to end with : "))
print("Generating Links from", start, "to", end)
end=end+1 # Increased by 1 for range function

animename = animelink.split("/")  #splits link by /
animearr = animename[3].split("-")
animearr.pop()
animearr.pop()
animename = "-".join(animearr)

URL_PATTERN = 'https://gogoanime.so/{}-episode-{}' #General URL pattern for every anime on gogoanime

try:
	filename = "{}.txt".format(animename)
	f = open(filename)
	f.close()
	os.remove(filename)
except:
	#do nothing i don't care
	dummy = "dummy"



for episode in range(start,end):

	#generate url
	url = URL_PATTERN.format(animename,episode)
	srcCode = requests.get(url)
	soup = BeautifulSoup(srcCode.content,"lxml")

	#get link from download buttons lets goo
	dl_wrapper = soup.find_all('li', class_='dowloads')
		
	try:
		dl_wrapper = BeautifulSoup(str(dl_wrapper[0]),"lxml")
	except:
		print("there are no more episodes than {}".format(episode-1))
		break
	aaa = dl_wrapper.find_all('a')
	link = str(aaa[0]).replace('<a href="', '')
	ind = link.index('"')
	link = link[0:ind] #results in link to new site

	#get the new download page
	srcCode = requests.get(link)
	soup = BeautifulSoup(srcCode.content,"lxml")

	preferredlink = "" #find the link matching the quality
	for dl in soup.find_all('div', class_='dowload'):
		if str(dl).find(quality) != -1: #start with preffered quality and then downgrade
			preferredlink = str(dl)

		if preferredlink == "": #if you couldn't find the desired quality, downgrade by one
			if str(dl).find("720P") != -1:
				preferredlink = str(dl)
		"""#for now i am not doing lower than 720P
		if preferredlink == "": #if you couldn't find the desired quality, downgrade by one
			if str(dl).find("480P") != -1:
				preferredlink = str(dl)

		if preferredlink == "": #if you couldn't find the desired quality, downgrade by one
			if str(dl).find("360P") != -1:
				preferredlink = str(dl)
		"""
	#format the preffered link
	preferredlink = preferredlink.replace('<div class="dowload"><a download="" href="', '')
	ind = preferredlink.find('"')
	preferredlink = preferredlink[0:ind]

	#write it into a file
	f = open('{}.txt'.format(animename), "a") #opens file with name of "test.txt"
	f.write(preferredlink+"\n")

	#print the link for good measure
	print(preferredlink)
f.close()

print("----------------------------------------------------------")
print("success. you can copy the links here or from {}.txt in this folder".format(animename))
print("----------------------------------------------------------")



