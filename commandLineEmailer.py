#! /usr/bin/python3

# commandLineEmailer.py - takes an email address and text on the command line and ,using Selenium, logs into your email account and sends an email to the provided address.
# usage:
# commandLineEmailer.py <emial> "<temat>" "<text>"

import sys, time

#read email and text from command line

if len(sys.argv) != 4:
    print(sys.argv)
    print("Wrong arguments!")
    print('!Use schema: commandLineEmailer.py <emial> "<temat>" "<text>"!')
else:
    email = sys.argv[1]
    topic = sys.argv[2]
    text = sys.argv[3]

#selenium configuration
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Firefox(executable_path=r'/home/mati/Desktop/geckodriver')
browser.get('https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')

#log into gmail account and send text

#type login
emailElem = browser.find_element_by_id('identifierId')
emailElem.send_keys('email')
emailElem.send_keys(Keys.ENTER)

time.sleep(2)
#type password
passElem = browser.find_element_by_css_selector("input[type='password']")
passElem.send_keys('password')
passElem.send_keys(Keys.ENTER)

time.sleep(12)
browser.find_element_by_xpath("/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div[1]/div/div").click()

time.sleep(12)
toWhom = browser.find_element_by_xpath('//*[@id=":pl"]')
toWhom.send_keys(email)

title = browser.find_element_by_xpath('//*[@id=":p3"]')
title.send_keys(topic)

content = browser.find_element_by_xpath('//*[@id=":q8"]')
content.send_keys(text)
time.sleep(5)

browser.find_element_by_xpath('//*[@id=":ot"]').click()

print("Done!")