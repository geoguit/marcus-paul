#                                          --- geoguit ---
# marcus-paul.py
# Created on the 3rd of July, 2020
#
# Spams the Marcus Paul contact section on the 2SM website
#                                          --- geoguit ---

import json
import random
import string
import requests

def randomNum(stringLength):
    letters = string.digits
    return ''.join(random.choice(letters) for i in range(stringLength))

msg = 'https://youtu.be/5-tcuHdfQek'
url = 'http://2smsupernetwork.com/wp-json/contact-form-7/v1/contact-forms/1609/feedback'
firstNames = json.loads(open('first-names.json').read())
lastNames = json.loads(open('last-names.json').read())
emails = ['gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com']

while True:
    fName = random.choice(firstNames)
    lName = random.choice(lastNames)
    client = random.choice(emails)
    ext = randomNum(3)
    selectNm = random.randint(0, 3)
    if(selectNm == 0):
        uName = fName.lower() + ext + '@' + client
            
    elif(selectNm == 1):
        uName = fName.lower() + '.' + lName.lower() + '@' + client
        
    elif(selectNm == 2):
        uName = fName.lower() + ext + '.' + lName.lower() + '@' + client

    elif(selectNm == 3):
        uName = fName.lower() + '.' + lName.lower() + ext + '@' + client

    fullName = fName + ' ' + lName

    res = requests.Session().post(url, allow_redirects=False, data={
        '_wpcf7': 1609,
        '_wpcf7_version': '5.1.7',
        '_wpcf7_locale': 'en_US',
        '_wpcf7_unit_tag': 'wpcf7-f1609-p1614-o1',
        '_wpcf7_container_post': 1614,
        'Sendmessageto': 'Marcus Paul',
        'your-name': fullName,
        'your-email': uName,
        'your-subject': 'The Comedian',
        'your-message': msg
    })
    print('Name: %s, email: %s, got status code %s.' % (fullName, uName, res.status_code))