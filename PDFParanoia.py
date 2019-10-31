#! /usr/bin/python3

#PDFPAranoia.py - a script that go through every PDF in a folder (and its subfolders) and encrypt the PDFs using a password provided on the command line.
#Save each encrypted PDF with an _encrypted.pdf suffix added to the original filename.

import os, PyPDF2,sys

#set paths od dirs; path1 - source, path2 - direction

path1 = '/path/to/folder/with/pdfs'
path2 = '/path/to/des/of/encrypted/files'

# taking password from command line
if len(sys.argv) != 2:
    print("Too many arguments!")
else:
    password = sys.argv[1]

#checking if the path already exists
if os.path.isdir(path2) == True:
    pass
else:
    os.mkdir(path2)


#walking through folder and subfolders
for folderName, subfolders, filenames in os.walk(path1):
    for filename in filenames:

        #finding .pdfs
        if filename.endswith('.pdf'):
            #opening .pdfs
            pdfFile = open(folderName+"/"+filename, 'rb')
            pdfReader = PyPDF2.PdfFileReader(pdfFile)
            pdfWriter = PyPDF2.PdfFileWriter()
            for pageNum in range(pdfReader.numPages):
                pdfWriter.addPage(pdfReader.getPage(pageNum))
            #encrypt .pdfs
            pdfWriter.encrypt(password)
            #saving pdfs
            print(path2+'/'+filename[:-4]+'_encrypted.pdf')
            resultPdf = open(path2+'/'+filename[:-4]+'_encrypted.pdf', 'wb')
            pdfWriter.write(resultPdf)
            resultPdf.close()
print("--------")
print("DONE")

