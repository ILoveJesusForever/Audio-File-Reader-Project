import tkinter as tk
from tkinter import ttk
from tkinterdnd2 import tkinterDnD, DND_FILES

def drop_event(event):
    #assumes the event parameter has a data property
    #the data property of a file contains the filepath
    filepath = event.data
    print(f'File path: {filepath}')




def create_app():
    #create window
    app = tk.Tk()
    app.title('File Reader')
    app.geometry('300x500')
    #create canvas for file drops
    drop_window = tk.Canvas(width=100, height= 100, bg= 'white')
    

    #run window
    app.mainloop()


create_app()