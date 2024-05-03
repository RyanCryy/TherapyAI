from flask import Flask, render_template, request, flash
##Youtube imports
from pytube import YouTube
import os
import pafy
import regex
import tkinter as tk
from tkinter import filedialog
from tkinter import *
##instagram imports

from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time

import instaloader 

###tiktok imports
from pathlib import Path
#from TikTokApi import TikTokApi

app = Flask(__name__)
app.secret_key = "123456789"

@app.route('/')
def homepage():
    return render_template("homepage.html")

@app.route('/login')
def login():  
    return render_template("login.html" )

@app.route('/playlists')
def playlists():  
    return render_template("playlists.html" )

@app.route('/how')
def how():
    return render_template("how.html")

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/socials')
def socials():
    return render_template('socials.html')

@app.route('/page2')
def page2():
    return render_template("page2.html")
###########################################################################################################################
@app.route('/searchbarutubevid')
def searchbarutubevid():
    return render_template('searchbarutubevid.html') #done

@app.route('/searchbarutubeau')
def searchbarutubeau():
    return render_template('searchbarutubeau.html')#done

@app.route('/searchbarinsta')
def searchbarinsta():
    return render_template('searchbarinsta.html')#done

@app.route('/searchbartiktok')
def searchbartiktok():
    return render_template('searchbartiktok.html')

@app.route('/searchbarwatcher')
def searchbarwatcher():
    return render_template('searchbarwatcher.html')
###########################################################################################################################

@app.route('/youtubeau',methods=["GET","POST"])
def youau():
    root = tk.Tk()
    root.withdraw()

    
    links=str(request.form.get('links')) ##this is the link given by the user
    print(regex)

    yt=YouTube(links)
    ys = yt.streams.get_highest_resolution()
    path="downloads"
    #path = filedialog.askdirectory()
    ys.download(output_path = path, filename = yt.title + " .mp3 ")
    display = yt.title 

    return render_template("youau.html",display=display)

@app.route('/youtubevid',methods=["GET","POST"])
def youvid():
    root = tk.Tk()
    root.withdraw()
    
    
    links=str(request.form.get('links')) ##error
    print(regex)
         
    yt=YouTube(links)
    ys = yt.streams.get_highest_resolution()
    path="downloads"
    #path = filedialog.askdirectory()
    ys.download(output_path = path, filename = yt.title + " .mp4 ")
    display = yt.title 

    return render_template('youvid.html',display=display)

@app.route('/instagram',methods=["GET","POST"])
def instagram():
    root = tk.Tk()
    root.withdraw()
    ###code for form actions here
   
    links=str(request.form.get('links')) ##this is the link given by the user
    print(regex)

    username = links
    #instaloader.Instaloader().download_profile(username,profile_pic_only=False)
    display = links + "'s profile" 
    return render_template('instagram.html', display=display)

@app.route('/watcher',methods=["GET","POST"])
def watcher():  
    ######here will be the input link
    link = request.form.get('link')
    return render_template("watcher.html" ,link= link)

@app.route('/wip')
def wip():
    return render_template('workinprogress.html')
'''
@app.route('/tiktok')
def tiktok():
    return render_template('tiktok.html')

'''


app.run(debug=True,port=5000)


'''  
Note:if you still get an error to due to me forgetting what to install do drop me a message


$ pip install Flask
#######################pip install TikTokApi
python -m playwright install
pip install beautifulsoup
pip install selenium
pip install tk
$ pip install pytube

'''