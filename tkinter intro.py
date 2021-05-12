from tkinter import *
root = Tk()
root.title = ("I am a window")
root.geometry("100x100")
app = Frame(root)
app.grid()
button1 = Button(app, text = "I am button 1")
button1.grid()
root.mainloop()
