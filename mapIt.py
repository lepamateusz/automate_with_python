#! /usr/bin/python3

# mapeIt.py - Launch a map in browser ussing the addrees from the command line or clipboard

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    #Get address from command line
    address = ' '.join(sys.argv[1:])
    print(address)
else:
    address = pyperclip.paste()
    print(address)

webbrowser.open('https://www.google.com/maps/place/' + address)

