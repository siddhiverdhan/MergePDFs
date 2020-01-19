import PySimpleGUI as sg
import sys
import PyPDF2

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

layout = [[sg.Text('Browse 2 PDF files to merge')],    
                [sg.Text('PDF File 1', size=(8, 1)), sg.Input(), sg.FileBrowse()],      
                [sg.Text('PDF File 2', size=(8, 1)), sg.Input(), sg.FileBrowse()],      
                [sg.Submit(), sg.Cancel()]]      

window = sg.Window('PDF Merge', layout)  

event, values = window.Read()

fname1= values[0]
fname2= values[1]

if not fname1 or not fname2:
        sg.Popup("Cancel", "No filename supplied")
        raise SystemExit("Cancelling: no filename supplied")
else:
        pdfs = [fname1, fname2]
        
        # output pdf file name 
        output  = 'Merged.pdf'
        
        # calling pdf merge function 52
        PDFmerge(pdfs = pdfs, output = output) 

        window.Close()

        sg.Popup('Merged Files',      
                        
                'file saved at  "{}" with name Merged.pdf'.format(os.getcwd()))

