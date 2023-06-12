'''Merge The PDF '''
from PyPDF2 import PdfWriter
import os
'''PdfWriter is a class which contain the merger object for accessing'''
merger=PdfWriter()
''' files is a folder which contain no. of pdf's '''
files=[file for file in os.listdir() if file.endswith(".pdf")]
''' pdf is iterative variable which access the every pdf file'''
for pdf in files:
    merger.append(pdf)
merger.write("merged-pdf.pdf")
merger.close()