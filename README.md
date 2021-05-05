# gogoanime-downloader

# a lot better, faster version written in javascript (that downloads from animetwist) [here](https://github.com/KraXen72/animetwist-dl-electron)
![preview](https://camo.githubusercontent.com/6c14e407fb7b2652a18ed7808f855ce041c58ed9d07d3dc14d18333af06f0027/68747470733a2f2f63646e2e646973636f72646170702e636f6d2f6174746163686d656e74732f3730343739323039313935353432393432362f3830363937333233383633383534323933392f5265635f323032315f30322e30345f323034322e676966)

## python version (standalone program) - discontinued & slow:
generate links from gogoanime to batch download whole series
![showcase](https://cdn.discordapp.com/attachments/704792091955429426/799685944756273213/ezgif-3-34b0a9c89d2e.gif)
  
# installation:
## windows (gui)
- download the ``gui.exe`` and ``gogoanimee.py``
- run ``gui.exe``

  
## windows / linux / mac (cli / gui)
- **required**  
  - python 3
  - pip
  - The following modules: (Use pip install to download them)
    - requests
    - bs4
    - lxml
    - pysimpleguiqt (if you want gui)
- clone this repo
- run ``cli.py`` or ``gui.py``
  
note: ``cli.py`` or ``gui.py`` will not work without ``gogoanimee.py`` in the same folder.  
  
# how to use
**1.** go to the first episode of the anime you would like to download and copy the link.        
for example: https://gogoanime.so/shingeki-no-kyojin-episode-1   
**2.**  
- GUI: paste it into the first field
- CLI: paste it into console  
    
**3.** 
- GUI: enter the download range into their respective fields.     
e.g. 1 in first field and 12 in the next field  
- CLI: enter the first episode you want downloaded, and then the last one.  
  
**4.** wait for it to generate links. if you are using gui, you can check the second window for progress. cli prints the links out.   
**5.** in the folder there should appear a `.txt` file with all the links.  
**6.** copy the links to clipboard and use any downlaod manager to download the anime.    

## downloading the links with free download manager  
i will briefly explain how to use free download manager in case you haven't used a download manager yet  
**1.** download free download manager: https://www.freedownloadmanager.org  
**2.** open it and press the three lines in top right corner  
**3.** click ``Paste urls from clipboard``  
**4.** complete this dialog and you're good to go.    
  
![a](https://cdn.discordapp.com/attachments/704792091955429426/799624841758113852/unknown.png)  
