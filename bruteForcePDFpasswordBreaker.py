#! /usr/bin/python3

#bruteForcePDFpasswordBreaker.py - brute-force password attack to PDF file

import PyPDF2

#Read files with English words
pathDIC = '/home/mati/Desktop/dictionary.txt'
pathPDF = '/home/mati/Desktop/encrypted.pdf'

with open(pathDIC, 'r') as txtfile:
    words = [line.rstrip('\n').lower() for line in txtfile.readlines()]

#Read encrypted files

pdfReader = PyPDF2.PdfFileReader(open(pathPDF, 'rb'))
if pdfReader.isEncrypted:
    # Loop over words with trying to quess password
    for word in words:
        if pdfReader.decrypt(word) == 1:
            print(word)
            break
else:
    print("File is decrypted!")


