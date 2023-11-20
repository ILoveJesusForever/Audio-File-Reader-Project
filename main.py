import tkinter as tk
from tkinter import ttk
from select_scriptures2 import FileReader


# Create an instance of FileReader with a list of file paths
files = FileReader(['.txt/John 4,31-38.txt', '.txt/Ezekiel 2,1-8.txt'])


def readFiles():
    files.read_current_file()

readFiles()


# app = tk.Tk()
# app.title("Scriptures App")
# app.geometry('300x500')



# #menu for settings
# menu = tk.Menu(master=app)
# app.configure(menu= menu)
# file_menu = tk.Menu(master=menu, tearoff= 'false')
# menu.add_cascade(label= 'File', menu= file_menu)
# file_menu.add_command(label= 'New', command= lambda: print("new file"))

# #menu button
# select_category = ttk.Menubutton(master=app,text= 'Select Category of Scripture')
# select_category.pack()

# #scripture categories
# categories = tk.Menu(master=select_category, tearoff= 'false')
# categories.add_command(label= 'Faith Scriptures', command= lambda: print('faith scriptures selected'))
# categories.add_command(label= 'Spiritual Food Scriptures', command= lambda: print('spiritual food scriptures selected'))
# categories.add_command(label= 'Discipline Scriptures', command= lambda: readFiles)
# select_category['menu'] = categories
# #another way to pack the submenus in the menu button
# select_category.configure(menu = categories)


# combobox = ttk.Combobox(master=app)
# combobox.pack()

# menuButton = ttk.Menubutton(master=app, menu= ['option1', 'option2', 'option3'])
# menuButton.pack()

# app.mainloop()










