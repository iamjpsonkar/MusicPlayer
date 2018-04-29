import os
from tkinter import *
from tkinter.filedialog import askdirectory

import pygame

root = Tk()
root.minsize(300, 300)
root.title("Music Player By JaySoft")




n=0
LOS = []
IND = 0
v=StringVar()                          
sng=Label(root,textvariable=v,width=40)





def play(n):
    if n<0 or n>=len(LOS):
        return
    pygame.mixer.init()
    pygame.mixer.music.load(LOS[n])
    a=pygame.mixer.music.play()
    updatesng()
    
    

def play1(event):
    pygame.mixer.music.play()
    updatesng()


def next(event):
    global n
    if n==len(LOS)-1:
        n=0
    else:
        n+=1
    pygame.mixer.music.load(LOS[n])
    pygame.mixer.music.play()
    updatesng()






def prev(event):
    global n
    if n==0:
        n=len(LOS)-1
    else:
        n-=1
    pygame.mixer.music.load(LOS[n])
    pygame.mixer.music.play()
    updatesng()


def pause(event):
    pygame.mixer.music.pause()
    updatesng()



def stop(event):
    pygame.mixer.music.stop()
    global v
    v.set("")



def updatesng():
    global n,v,LOX
    v.set(LOS[n])
    return LOS[n]




def Dir_choose():
    dir_c = askdirectory()
    os.chdir(dir_c)
    global LOS
    global IND
    for files in os.listdir(dir_c):
        if files.endswith(".mp3"):
            LOS.append(files)
            IND += 1


# print(os.path.dirname(os.path.realpath(__file__)))
l1 = Label(root, text="Playlist")
l1.configure(background="orange",bd=2)
l1.pack()
lb = Listbox(root,width=30)
lb.configure(background="green")
lb.pack()
sng.configure(background="yellow",bd=2)
sng.pack()
prv = Button(root, text="Prev", width=15)
prv.configure(background="blue",bd=2)
prv.pack()
prv.bind("<Button-1>",prev)


pl = Button(root, text="Play", width=15)
pl.configure(background="blue",bd=2)
pl.pack()
pl.bind("<Button-1>",play1)


nxt = Button(root, text="Next", width=15)
# image=PhotoImage(file="image\\next.jpg"),height=15,width=15
nxt.configure(background="blue",bd=2)
nxt.pack()
nxt.bind("<Button-1>",next)


ps = Button(root, text="Pause", width=15)
ps.configure(background="blue",bd=2)
ps.pack()
ps.bind("<Button-1>",pause)


st = Button(root, text="Stop", width=15)
st.configure(background="blue",bd=2)
st.pack()
st.bind("<Button-1>",stop)
Dir_choose()
LOS1=LOS[::-1]
for x in LOS1:
    lb.insert(0,x)
play(n)

root.configure(background="red")

root.mainloop()
