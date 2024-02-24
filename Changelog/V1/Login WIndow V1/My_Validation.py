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

def is_valid_username(text) -> bool:
    """Checks if a string is a valid username"""
    #Username musn't contain any special characters and is longer than 5 characters
    return bool(re.search(r"^[a-zA-Z0-9_]{5,}$", text))

def is_valid_password(text) -> bool:
    """Checks if a string is a valid password"""
    #password must be at least 5 characters long and contain at least one uppercase letter, one lowercase letter and one number
    return bool(re.search(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{5,}$", text))

if __name__ == "__main__":
    print(is_valid_password("Password123"))  # True
    print(is_valid_password("password123"))  # False
    print(is_valid_password("Password"))  # False
    print(is_valid_password("password")) # False
    print(is_valid_password("Pass")) # False
    print(is_valid_password("Pass1")) # True
