from tkinter import *
import pyscreenrec
import os

root = Tk()
root.geometry("400x600")
root.title("screen recorder")
root.config(bg="#fff")
root.resizable(False, False)

def get_next_filename(filename):
    base_name = filename + ".mp4"
    if not os.path.exists(base_name):
        return base_name
    i = 1
    while os.path.exists(f"{filename}({i}).mp4"):
        i += 1
    return f"{filename}({i}).mp4"


def start_rec():
    file = Filename.get()
    file = get_next_filename(file)
    rec.start_recording(str(file), 5)
    root.attributes("-alpha", 0.1)  # Makes the entire app almost transparent when recording starts

def on_enter(event):
    root.attributes("-alpha", 1.0)  # Sets the opacity back to normal when mouse hovers over the window

def on_leave(event):
    root.attributes("-alpha", 0.1)  # Makes the entire app almost transparent again when the mouse leaves

# Bind mouse hover events to the root window
root.bind("<Enter>", on_enter)
root.bind("<Leave>", on_leave)

def pause_rec():
    rec.pause_recording()

def resume_rec():
    rec.resume_recording()

def stop_rec():
    rec.stop_recording()

rec = pyscreenrec.ScreenRecorder()

# icon
image_icon = PhotoImage(file="icon.png")
root.iconphoto(False, image_icon)

# background images
image1 = PhotoImage(file="yellow.png")
Label(root, image=image1, bg="#fff").place(x=-2, y=35)

image2 = PhotoImage(file="blue.png")
Label(root, image=image2, bg="#fff").place(x=223, y=200)

# heading
lbl = Label(root, text="Screen Recorder", bg="#fff", font="arial 13 bold")
lbl.pack(pady=20)

image3 = PhotoImage(file="recording.png")
Label(root, image=image3, bd=0).pack(pady=30)

# entry
Filename = StringVar()
entry = Entry(root, textvariable=Filename, width=14, font="arial 15")
entry.place(x=100, y=350)
Filename.set("recording")

# buttons
start = Button(root, text="Start", font="arial 20", bd=0, bg="#FFFFFF", command=start_rec)
start.place(x=137, y=247)

image4 = PhotoImage(file="pause.png")
pause = Button(root, image=image4, bd=0, bg="#fff", command=pause_rec)
pause.place(x=50, y=450)

image5 = PhotoImage(file="resume.png")
resume = Button(root, image=image5, bd=0, bg="#fff", command=resume_rec)
resume.place(x=150, y=450)

image6 = PhotoImage(file="stop.png")
stop = Button(root, image=image6, bd=0, bg="#fff", command=stop_rec)
stop.place(x=250, y=450)

root.mainloop()
