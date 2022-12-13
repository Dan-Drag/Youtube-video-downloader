import tkinter
from tkinter import ttk
from tkinter import filedialog
from pytube import *
from pytube.cli import on_progress

ytlist = None
path = None
itag = None


def findVideo():
    listForBox = list()
    link = linkEntry.get()
    global ytlist
    ytlist = YouTube(link, on_progress_callback=on_progress)
    for i in ytlist.streams:
        if (i.type == "video"):
            listForBox.append(
                f"Itag:{i.itag}; res:{i.resolution}; mime_type:{i.mime_type};")
        if (i.type == "audio"):
            listForBox.append(
                f"Itag:{i.itag}; res:{i.abr}; mime_type:{i.mime_type};")
    itagCB["values"] = listForBox
    infoLabel["text"] = f"{ytlist.title}"


def chooseInCBox(event):
    selection = itagCB.get()
    print(selection)
    global itag
    itag = selection[selection.find(":") + 1: selection.find(";")]


def chooseDerectory():
    global path
    path = filedialog.askdirectory()
    print(path)


def streamDownload():
    stream = ytlist.streams.get_by_itag(itag)
    if (path == ""):
        stream.download()
        print("Done")
    else:
        stream.download(path)
        print("Done")


root = tkinter.Tk()
root.title("Youtube")
root.geometry("400x350")

frame1 = ttk.Frame(root)
frame2 = ttk.Frame(root)
txtAboveEntry = ttk.Label(root, text="\nInset link")
linkEntry = ttk.Entry(frame1)
findButton = ttk.Button(frame1, text="Find Video", command=findVideo)
infoLabel = ttk.Label(root, background="#ffffff", wraplength=320)
txtAboveComboBox = ttk.Label(root, text="Choose video itag")
itagCB = ttk.Combobox(root)
directoryButton = ttk.Button(
    frame2, text="Choose directory", command=chooseDerectory)
downloadButton = ttk.Button(frame2, text="Download", command=streamDownload)

txtAboveEntry.pack(padx=20, anchor="nw")
frame1.pack(side="top", fill="x")
linkEntry.pack(side="left", padx=20, ipadx=60)
findButton.pack(side="right", padx=5)
infoLabel.pack(anchor="nw", ipadx=160, padx=20, pady=20)
txtAboveComboBox.pack(padx=20, anchor="nw")
itagCB.pack(anchor="nw", padx=20, ipadx=70)
itagCB.bind("<<ComboboxSelected>>", chooseInCBox)
frame2.pack(side="bottom", fill="x", padx=10, pady=5)
directoryButton.pack(side="left")
downloadButton.pack(side="right")

root.mainloop()
