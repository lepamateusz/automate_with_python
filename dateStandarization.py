#! /usr/bin/python3

# dateStandarization.py - Find dates in text and standarize all dates in to one format

import pyperclip, re


dateRegex = re.compile(r'''(
    (\d{4}|\d{2}|\d{1})                # area code
    (\s|-|\.|\/)                        # separator
    (\d{2})                           # first 3 digits
    (\s|-|\.|\/)                         # separator
    (\d{4}|\d{2})                         # last 4 digits
        )''', re.VERBOSE)


text = str(pyperclip.paste())
matches = []

for group in dateRegex.findall(text):
    print(group)
    for i in range(len(group)):
        if len(group[i]) == 4:
            msc = group[3]
            rok = group[i]
            if group.index(group[i]) == 5:
                dzien = group[i-4]
            else:
                dzien = group[i+4]

    date = '-'.join([rok,msc,dzien])
    matches.append(date)


if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print("Copied to clipboard")
    print('\n'.join(matches))
else:
    print("No dates found!")


## Clean up dates in different date formats (such as 3/14/2015, 03-14-2015, and 2015/3/14) by replacing them with dates in a single, standard format.