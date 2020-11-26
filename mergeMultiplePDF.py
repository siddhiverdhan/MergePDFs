import PySimpleGUI as sg
import PyPDF2
import sys
import os

def PDFmerge(pdfs, output):  
    # creating pdf file merger object 
    pdfMerger = PyPDF2.PdfFileMerger() 
      
    # appending pdfs one by one 
    for pdf in pdfs: 
        with open(pdf, 'rb') as f:
            pdfMerger.append(PyPDF2.PdfFileReader(f),'rb')
          
    # writing combined pdf to output pdf file 
    with open(output, 'wb') as f: 
        pdfMerger.write(f) 
event, values = sg.Window('Browse PDF files to merge').Layout([[sg.Input(key='_FILES_'), sg.FilesBrowse()], [sg.OK(), sg.Cancel()]]).Read()

print(values['_FILES_'].split(';'))

# output pdf file name 
output  = 'Merged.pdf'
        
# calling pdf merge function 52
PDFmerge(pdfs = values['_FILES_'].split(';'), output = output) 



sg.Popup('Merged Files', 'file saved at  "{}" with name Merged.pdf'.format(os.getcwd()))
