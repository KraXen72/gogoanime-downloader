# gogoanime-downloader
generate links from gogoanime to batch download whole series

## required
- python 3
- pip
- The following modules: (Use pip install to download them)
  - requests
  - bs4
  - lxml
  
## how to use  
**1.** go to the first episode of the anime you would like to download.    
for example: https://gogoanime.so/shingeki-no-kyojin-episode-1  

**2.** copy the link  
**3.** open command line in the folder where you downloaded / cloned this  
**4.** type ``python anime.py`` note: `python` has to be in PATH if you are on windows. google it.  
**5.** you will see:  
![what you will see](https://cdn.discordapp.com/attachments/704792091955429426/799622541672579092/Screenshot_2021_01.15_1354.png)
  
then paste the link there (ctrl + shift + v)  
**6.** you will be prompted to enter first episode you want to download  
**7.** you will be prompted to enter last episode you want to download note: to download the whole season just set this to like 1000 the program will automatically stop when needed  
**8.** wait for it to generate links.
**9.** in the folder there should appear a `.txt` file with all the links.
**10.** copy the links to clipboard and use any downlaod manager to download the anime.

## downloading the links with free download manager  
i will briefly explain how to use free download manager in case you haven't used a download manager yet  
**1.** download free download manager: https://www.freedownloadmanager.org  
**2.** open it and press the three lines in top right corner  
**3.** ``Paste urls from clipboard``
**4.** complete this dialog and you're good to go.  
  
![a](https://cdn.discordapp.com/attachments/704792091955429426/799624841758113852/unknown.png)  
