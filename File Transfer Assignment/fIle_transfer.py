
from sqlite3 import Timestamp
import tkinter as tk
from tkinter import *
import tkinter.filedialog
import os
from os import *
import shutil
from datetime import *


class ParentWindow (Frame):
    def __init__(self, master):
        Frame.__init__(self)
        #Sets title of GUI Window
        self.master.title("File Transfer")
        #Creates button to select files from source directory
        self.sourceDir_btn = Button(text="Select Source",width=20, command=self.sourceDir)
        #Positions source button in GUI using tkinter grid()
        self.sourceDir_btn.grid(row=0, column=0, padx=(20, 10), pady=(30, 0))

        #Creates entry for source directory selection
        self.source_dir = Entry(width=75)
        #Positions entry in GUI using tkinter grid() padx and pady are the same as
        #the button to ensure they will line up 
        self.source_dir.grid(row=0, column=1, columnspan=2, padx=(20,10), pady = (30,0))

        #Creates button to select destination of files from destination directory
        self.destDir_btn = Button(text="Select Destination", width=20, command=self.destDir)
        #Positions destination button in GUI using tkinter grid()
        #on the next row under the source button
        self.destDir_btn.grid(row=1, column=0, padx=(20, 10), pady=(15,10))

        #Creates entry for destination directory selection
        self.destination_dir = Entry(width=75)
        #Postions entry in GUI using tkinter grid() padx and pady are the same as
        #the button to ensure they will line up
        self.destination_dir.grid(row=1, column=1, columnspan=2, padx=(20, 10), pady=(15,10))

        #Creates files to transfer files
        self.transfer_btn = Button (text="Transfer Files", width=20, command=self.transferFiles)
        #Positions transfer files button
        self.transfer_btn.grid(row=2, column=1, padx=(200, 0), pady=(0,15))

        #Creates an Exit Button
        self.exit_btn = Button (text="Exit", width= 20, command=self.exit_program)
        self.exit_btn.grid(row=2, column=2, padx=(10, 40), pady=(0, 15))

    def sourceDir(self):
        selectSourceDir = tkinter.filedialog.askdirectory()
        #The .delete (0, END) will clear the content that is inserted in the Entry widget,
        #this allows the path to be inserted into  the Entry widget properly.
        self.source_dir.delete(0,END)
        #The .insert method will insert the user selection to the source_dir Entry
        self.source_dir.insert(0, selectSourceDir)

    #Creates function to select destination directory.
    def destDir(self):
        selectDestDir= tkinter.filedialog.askdirectory()
        self.destination_dir.delete(0, END)
        self.destination_dir.insert(0, selectDestDir)
    
    #Creates function to transfer files from one directory to another
    def transferFiles(self):
        source=self.source_dir.get()
        destination = self.destination_dir.get()
        source_files = os.listdir(source)
        
        #Checks if files are new or modified in last 24 hours
        date_curr = datetime.now()#Var for current time
        date_24hr = date_curr - timedelta(hours=24)#Var for time 24 hours ago
        path = self.source_dir.get()# Path to source folder
        for i in source_files:
            fullpath = os.path.join(path,i)#joins path to folder and files
            date_DM = os.path.getmtime(fullpath)# Gets date modified for each file
            date_eng = datetime.fromtimestamp(date_DM)#converts date_DM from secs to readable format ("eng")
            if date_eng > date_24hr: #transfers files if files modif. date is > past 24s
                shutil.move(source + '/' + i, destination)
                print(i + ' was sucessfully transferred.' )

    def exit_program(self):
        #root is the main GUI window, the Tkinter destory method
        #tells python to terminate root.mainloop and all widgets inside the GUI window
        root.destroy()




#Creates function to select source directory.

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
