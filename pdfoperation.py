from PyPDF2 import PdfReader
from PyPDF2 import PdfMerger
import config

mergedFile =config.mergedFile

file = [config.file1, config.file1]

def merge_pdf(file):
    pdfMerger = PdfMerger()
    for pdf in file:
        with open(pdf, 'rb') as f:
            pdfMerger.append(PdfReader(f), 'rb')
    with open(mergedFile,'wb') as f:
        pdfMerger.write(f)
        print('File merged.')

def read_pdf(file):
    reader = PdfReader(file)
    page =reader.pages[0]
    return page.extract_text()