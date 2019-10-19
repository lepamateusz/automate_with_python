#! /usr/bin/python3

# mabLibs.py - find words in file like NOUN , ADJECTIVE, ADVERB, ADVERB
# and change it into words user typed

file = open('hello.txt', 'r+')
print(type(file))
fileContent = file.read()
file.close()
print(fileContent)

print("Enter an adjective: ")
adjective = input()

print("Enter a noun: ")
noun = input()

print("Enter a verb: ")
verb = input()

print("Enter a adverb: ")
adverb = input()

fileList = fileContent.split()
print(fileList)

for i in range(len(fileList)):
    if fileList[i].strip('.|!|?|,') == 'ADJECTIVE':
        fileList[i] = adjective
    elif fileList[i].strip('.|!|?|,') == 'NOUN':
        fileList[i] = noun
    elif fileList[i].strip('.|!|?|,') == 'VERB':
        fileList[i] = verb
    elif fileList[i].strip('.|!|?|,') == 'ADVERB':
        fileList[i] = adverb

print(fileList)

result = ' '.join(fileList)
print(result)


resultFile = open('hello.txt', 'w')
resultFile.write(result)
resultFile.close()