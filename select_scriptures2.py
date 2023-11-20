from gtts import gTTS
import tkinter as tk
from tkinter import ttk
import pygame

class FileReader:
    def __init__(self, file_paths):
        self.file_paths = file_paths
        self.current_file_index = 0


    def create_window(self):
        #creating a window
        app = tk.Tk()
        self.app = app
        
        app.title("Audio Scriptures")
        app.geometry('500x700')

        #create menu
        menu = tk.Menu(app, tearoff= 'false')
    
        #add menus
        file_menu = tk.Menu(menu, tearoff= 'false')
        file_menu.add_command(label= 'new', command= print('file created'))
        menu.add_cascade(label= 'file', menu= file_menu)
                
        #adding buttons
        play_button = ttk.Button(master=app, text='play', command= lambda: FileReader.play_audio_when(self, True))
        play_button.pack()

        pause_button = ttk.Button(master=app, text='pause', command= lambda: FileReader.pause_audio_when(self, True))
        pause_button.pack()

        


    def play_audio_when(self, condition):
        if condition:
            pygame.mixer.music.play()

    def pause_audio_when(self, condition):
        if condition:
            pygame.mixer.music.pause()

    def read_current_file(self, play_audio=True):
        try:
            with open(self.file_paths[self.current_file_index], 'r', play_audio, encoding='utf-8') as file:
                #create a variable that stores the text by using file.read() which reads the file

                self.create_window()
                #read the txt file
                text = file.read()
                #use the text var as a parameter for gTTS
                tts = gTTS(text=text, lang='en')
                #save the audio into a file
                tts.save("speech.mp3")

                # load the audio file
                pygame.mixer.init()
                pygame.mixer.music.load("speech.mp3")
                
                tk.mainloop()

        except FileNotFoundError:
            print(f"The file {self.file_paths[self.current_file_index]} does not exist.")

    def read_next_file(self):
        if self.current_file_index < len(self.file_paths) - 1:
            self.current_file_index += 1
            self.read_current_file()
        else:
            print("This is the last file. No next file to read.")

    def read_previous_file(self):
        if self.current_file_index > 0:
            self.current_file_index -= 1
            self.read_current_file()
        else:
            print("This is the first file. No previous file to read.")
            
