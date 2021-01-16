import requests
from bs4 import BeautifulSoup
import os


#CONFIG
quality = "1080P" # 360P or 480P or 720P or 1080P
URL_PATTERN = 'https://gogoanime.so/{}-episode-{}' #General URL pattern for every anime on gogoanime

def init(): #init function

	string = "welcome to gogoanime.so batch downloader / link generator. \n"
	string += "by default it fetches at 1080P\n"
	string += "link example: \n"
	string += "https://gogoanime.so/kanojo-okarishimasu-episode-1 \n"

	return string 

def getlink(): #get the anime link
	return input("Enter Link to the first episode of your Anime Series : ")  #User Enters URL

def getstart(): #get the anime start
	start = int(input("Enter Episode Number to start with : "))
	if start <= 0:
		start = 1
	return start

def getend(): #get the anime end
	end = int(input("Enter Episode Number to end with : "))
	return end
def formatname(animelink):
	animename = animelink.split("/")  #splits link by /
	animearr = animename[3].split("-")
	animearr.pop()
	animearr.pop()
	animename = "-".join(animearr)
	return animename

def dl():
	print(init())
	animelink = getlink()
	start = getstart()
	end = getend()
	main()

def main(alink, startt, endd):
	start = int(startt)
	end = int(endd)
	animename = formatname(alink)

	try:
		filename = "{}.txt".format(animename)
		f = open(filename)
		f.close()
		os.remove(filename)
	except:
		#do nothing i don't care
		dummy = "dummy"

	longstring = ""
	end=end+1 # Increased by 1 for range function
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

		preferredlink = preferredlink.replace("&amp;", "&")

		#write it into a file
		
		f = open('{}.txt'.format(animename), "a") #opens file with name of "test.txt"
		f.write(preferredlink+"\n")
		
		longstring += preferredlink + "\n" 

		#print the link for good measure
		print(preferredlink)
	return longstring


#print(init())

#print(main())

#forget deleting the file for now



def success(alink):
	animename = formatname(alink)
	print("----------------------------------------------------------")
	print("success. you can copy the links here or from {}.txt in this folder".format(animename))
	print("----------------------------------------------------------")



