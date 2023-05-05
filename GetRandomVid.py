import os
import random
import tkinter as tk

#Get list of videos from current directory (recursive)
vidlist = []
for root, dirs, files in os.walk(os.getcwd()):
    for file in files:
        if file.endswith('.mp4') or file.endswith('.m4v'):
            vidlist.append(os.path.join(root, file))

#Choose random file from list and play
def myCommand():
    if len(vidlist) == 0:
        print("No videos to play")
    else:
        random_file=random.choice(vidlist)
        os.startfile(random_file)

#Create new window with button
window = tk.Tk()
window.geometry("700x300")
window.title("Get Random Video")
button = tk.Button(text="Play", width=10, height=2, command=myCommand)
button.grid(row=0, column=0, sticky="nsew")

window.mainloop()