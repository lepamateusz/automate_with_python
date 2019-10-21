#! /usr/bin/python3

#selectiveCopy.py - walks through a folder tree and searches for files with a certain file extension (such as .pdf or .jpg). Copy these files from whatever location they are in to a new folder.
import os, shutil

def selectiveCopy(folder):
    dirName = os.path.dirname(folder)
    FileName = '/files' #names of new the directory
    pathDestination = dirName + FileName

    # Create the directory.
    print('Creating Directory " %s " ...' % (FileName))
    if not os.path.exists(pathDestination):
        os.mkdir(pathDestination)
        print("Directory ", (pathDestination), " Created ")
    else:
        print("Directory ", (pathDestination), " already exists")

    #Go through dictionary tree
    paths = []
    for foldername, subfolders, filenames in os.walk(folder):
        #Looking for .jpg or .pdf files
        for filename in filenames:
            if filename.endswith('.pdf') or filename.endswith('.jpg'):
                #print('The current folder name: ' + foldername)
                absPath = os.path.join(foldername, filename)
                paths.append(absPath)

    #Copy files
    for path in paths:
        shutil.copy(path, pathDestination)

    print("Done")

selectiveCopy('/path/to/directory/')