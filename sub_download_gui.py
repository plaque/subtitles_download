from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import requests
from bs4 import BeautifulSoup
import re
import random
import time
from download import download as d


def sub_download(event=None):

    urlSite = url.get()
    i = episodeNum.get()
    i = int(i)
    name = showName.get()

    urlSite.strip()
    name.strip()

    r = requests.get(urlSite)
    soup = BeautifulSoup(r.content)
    all_links = []

    for a in soup.find_all("a"):
        if re.search("\dx", a.text):
            all_links.append("http://www.opensubtitles.org" + a.get("href"))

    num_links = len(all_links)

    for j in range(0, num_links):
        if j + 1 > i:
            time.sleep(random.randint(2, 5))
            d(all_links[j], name + str(j + 1) + ".rar")
            print(all_links[j])


root = Tk()
root.title("Sub download")
root.geometry("430x110+300+300")

frame = Frame(root)

url = StringVar()
showName = StringVar()
episodeNum = IntVar()

urlLabel = Label(frame, text = "Url")
urlLabel.grid(row = 0, column = 0, sticky = N)
urlEntry = Entry(frame, textvariable = url)
urlEntry.grid(row = 1, column = 0, sticky = N)

showNameLabel = Label(frame, text = "Name of the show")
showNameLabel.grid(row = 0, column = 1, sticky = N)
showNameEntry = Entry(frame, textvariable = showName)
showNameEntry.grid(row = 1, column = 1, sticky = N)

episodeNumLabel = Label(frame, text = "Last subtitles downloaded")
episodeNumLabel.grid(row = 0, column = 2, sticky = N)
episodeEntry = Entry(frame, textvariable = episodeNum)
episodeEntry.grid(row = 1, column = 2, sticky = N)

bDownload = Button(frame, text="Get data")
bDownload.bind("<Button-1>", sub_download)
bDownload.grid(row = 3, column = 1, sticky = NS)

frame.pack(fill="both", expand=True, padx=20, pady=20)
root.mainloop()


