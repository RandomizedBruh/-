import tkinter as tk
from tkinter import font

root = tk.Tk()
root.title = "Программс"
root.geometry("400x300")

# root.iconbitmap(default="./limonch.ico")
# metanit.com

count = 0

def handlePop():
    global count
    count = count +1
    print("HAHA U can't LEAVE")
    label["text"] = f"click {count}"
    if count > 40:
        label["background"] = "red"


iconFromPhoto = tk.PhotoImage(file="./5RUBLESFNFWHAAT.png")
root.iconphoto(False,iconFromPhoto)




root.minsize(200,200)
root.maxsize(800,800)

root.resizable(True, False) 

cfont= font.Font(family="Comic Sans MS",size=14,weight="normal")

# a=lambda a: a*8
# print(a)

label = tk.Label(root,text=f"prevet {count}", font = cfont, foreground="green", background="yellow")
label.pack()

topFrame = tk.Frame(root, width=200 ,height=100, background="blue",padx=20, pady=30)
topFrame.pack(expand=True, fill="both")


button = tk.Button(topFrame, text="Close dis shhhh....", background="red", command=handlePop)
button.pack()

check = tk.Checkbutton(topFrame, text="CHECKPOINT")
check.pack()

button = tk.Button(root, text="BUTTon", background="gray", command=handlePop, font =cfont)
button.pack(expand=True, fill="none", anchor="s",padx=20,pady=40)


root.mainloop()