def is_secure(password:str)->bool:
    '''
    Verify if a password is secured:
    - must be at least 8 characters long
    - has at least one lowercase character
    - has at least one uppercase character
    - has at least one digit
    - has at least one symbol

    parameter:
    password (str): the password to check

    returns:
    bool: True if password passes all requirement, otherwise returns False

    Raises:
    TypeError: if password is not str
    '''

    if len(password) < 8:
        return False
    
    has_lowercase = False
    has_uppercase = False
    has_digit = False
    has_symbol = False

    for char in password:

        if has_lowercase and has_uppercase and has_digit and has_symbol:
            return True
        
        if char.isdigit(): # if char is digit
            has_digit = True
            continue


        char = ord(char) # fetch ASCII value

        if  97 <= char <= 122: #if is lowercase alphabet
            has_lowercase = True
            continue

        elif 65 <= char <= 90: # if is uppercase
            has_uppercase = True
            continue

            # if char matches any group of ASCII symbols
        elif (32 <= char <= 47) or (58 <= char <= 64) or (91 <= char <= 96) or (123 <= char <= 126):
            has_symbol = True
            continue


    if has_lowercase and has_uppercase and has_digit and has_symbol:
        return True
    else:
        return False
    


is_secure("rEVELATION2001!!!")