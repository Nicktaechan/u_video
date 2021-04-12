from tkinter import *


root = Tk()
root.title("U_video Player")

Label(root, text = 'U_video Player', font = 'arial 20 bold').pack()

link = StringVar()
Label(root, text = 'Paste link here', font = 'arial 15 bold').place(x= 160, y= 60)
link_enter = Entry(root, width = 70, textvariable = link).place(x= 32, y= 90)

def Downloader():
    url = Youtube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 180, y= 210)

Button(root, text = 'DOWNLOAD', font= 'arial 15 bold' ,bg = 'red', padx =2, command = Downloader).place(x= 180, y= 150)

root.mainloop()