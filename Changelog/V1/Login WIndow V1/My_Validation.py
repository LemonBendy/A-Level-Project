import re

def is_valid_length(text: str, length: int, s: str = "eq") -> bool: # 0 for equal, 1 for more than, 2 for less than
    """Checks if a string is a certain length"""
    match s:
        case "eq":  # default
            return int(len(text)) == int(length)
        case "gt":  # more than
            return int(len(text)) > int(length)
        case "lt":  # less than
            return int(len(text)) < int(length)

def is_valid_range(text: str, max: int, min: int, s: str = "gt") -> bool: # 0 for equal, 1 for more than, 2 for less than
    """Checks if a number is within a range"""
    match s:
        case "eq":  # default
            return int(min) <= int(len(text)) <= int(max)
        case "gt":  # more than
            return int(max) < int(len(text))
        case "lt":  # less than
            return int(len(text)) < int(min)

def is_valid_email(email: str) -> bool:
    """Checks if an email is valid"""
    # TODO: If you want more to write about, use an email validator library to check MX records (Ask Ash)
    return bool(re.search(r"^[\w.+\-]+@[\w]+\.[a-z]{2,3}$", email))

def is_valid_integer(text: str) -> bool:
    """Checks if a string is a valid integer"""
    return all(char.isdigit() for char in text)

def is_valid_float(text) -> bool:
    """Checks if a string is a valid float"""
    if text.count('.') > 1:
        return False
    return all(char.isdigit() or char == '.' for char in text)

def is_valid_string(text) -> bool:
    """Checks if a string is valid"""
    valid_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    return all(char in valid_characters for char in text)

def is_valid_date(text) -> bool:
    """Checks if a string is a valid date"""
    return bool(re.search(r"/^(?:31([/\-.])(?:0?[13578]|1[02])\1|(?:(?:29|30)(\/|-|\.)(?:0?[13-9]|1[0-2])\2))(?:(?"
                          r":1[6-9]|[2-9]\d)?\d{2})$|^(?:29(\/|-|\.)0?2\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|"
                          r"[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:0?[1-9]|1\d|2[0-8])(\/|-|\.)(?:(?:"
                          r"0?[1-9])|(?:1[0-2]))\4(?:(?:1[6-9]|[2-9]\d)?\d{2})$/gm", text))
