from tkinter import *
from tkinter import filedialog
import pdfoperation
import os
file =[]

def merge_pdf():
    if len(file)>1:
        print(file)
        pdfoperation.merge_pdf(file)
        label_file_explorer.config(text ='File merged at "{}" with name "MergedPdf.pdf" '.format(os.getcwd()))
    else:
        label_file_explorer.config(text ="ERROR: Browse at 2 files", fg ="Red")
def open_file_dialog():
    file_path = filedialog.askopenfilename(title="Open File", filetypes=[("PDF FILES","*.pdf")])
    if file_path:
        global file
        file.append(file_path)
        label_file_explorer.config(text ="File Browsed is :"+ file_path)

root = Tk()
root.title("Merge PDF Files")
root.geometry("850x450")

root.config(background="white")

label_file_explorer = Label(root, text ="Explore files", width=100, height=4, bg="white", fg ="Blue")

open_button = Button(root, text="Open First file", width=20, height=1, fg ="sky blue",bg="white",command=open_file_dialog)

open_button2 = Button(root, text="Open Sencond file", width=20, height=1,bg="white",fg ="sky blue",command= open_file_dialog)

open_button3 = Button(root, text="Merge Files", width=20, height=1,bg="white",fg ="green",command=merge_pdf)

label_file_explorer.grid(column=0, row=1)
open_button.grid(column=0, row=3)
open_button2.grid(column=0, row=4)
open_button3.grid(column=0, row=5)

root.mainloop()