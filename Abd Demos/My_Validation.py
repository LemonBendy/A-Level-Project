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

def is_valid_email(email):
    return bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email))