import re

def is_valid_length(text, length, s=0): # 0 for equal, 1 for more than, 2 for less than
    match s:
        case 0:  # default
            return int(len(text)) == int(length)
        case 1: # more than
            return int(len(text)) > int(length)
        case 2:# less than
            return int(len(text)) < int(length)


def is_valid_range(text, max, min, s=0): # 0 for equal, 1 for more than, 2 for less than
    match int(s):
        case 0: # default
            return int(min) <= int(len(text)) <= int(max)
        case 1: # more than
            return int(max) < int(len(text))
        case 2: # less than
            return int(len(text)) < int(min)

def is_valid_email(email): # Validate email
    return bool(re.search(r"^[\w.+\-]+@[\w]+\.[a-z]{2,3}$", email))

def is_valid_integer(text): # Validate integer
    return bool(re.search(r"^[0-9]+$", text))#

def is_valid_float(text): # Validate float
    return bool(re.search(r"^[0-9]+\.[0-9]+$", text)) # https://www.regextester.com/96683

def is_valid_string(text): # Validate string
    return bool(re.search(r"^[a-zA-Z0-9]+$", text)) # https://www.regextester.com/106421

def is_valid_date(text): # Validate date
    return bool(re.search(r"/^(?:31([/\-.])(?:0?[13578]|1[02])\1|(?:(?:29|30)(\/|-|\.)(?:0?[13-9]|1[0-2])\2))(?:(?"
                          r":1[6-9]|[2-9]\d)?\d{2})$|^(?:29(\/|-|\.)0?2\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|"
                          r"[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:0?[1-9]|1\d|2[0-8])(\/|-|\.)(?:(?:"
                          r"0?[1-9])|(?:1[0-2]))\4(?:(?:1[6-9]|[2-9]\d)?\d{2})$/gm", text)) # https://www.regextester.com/19
