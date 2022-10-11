import tkinter as tk
from tkinter import *
import webbrowser

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")
    #Default HTML Page Button
        self.btn = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.btn.grid(row=2, column=2, padx=(10,10) , pady=(10,10))
    #Submit Custom Text Button
        self.submit_btn = Button(self.master, text="Submit Custom Text", width=30, height=2, command=self.customSubmit)
        self.submit_btn.grid(row=2, column=3, padx=(10,10) , pady=(10,10))
    #Creates entry for Custom Text
        self.label = Label(root, text="Enter custom text or click the Default HTML page button").place(x=5, y=0)
        self.custText = Entry(width=75)
        self.custText.grid(row=1, column=1, columnspan=4, padx=(20,10), pady = (30,0))

    #Function for Default HTML Page Button
    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

    #Function for Custom Text Button
    def customSubmit(self):
        htmlTextCustom = self.custText.get()
        htmlFile = open("custom.html", "w")
        htmlContent = "<html>\n<body style='background-color:darkgray;'>\n<h1 style='color: aquamarine; text-align:center; font-family: Times New Roman; border: 5px inset white;'>" \
        + htmlTextCustom + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("custom.html")
        
        
    
    

    

















if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()