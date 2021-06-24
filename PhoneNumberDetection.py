def is_phone_number(text):  # 415-555-
    if len(text) != 12:
        return False  # not phone number sized
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False  # not area code
    if text[3] != '-':
        return False  # missing dash
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False  # no first three digits
    if text[7] != '-':
        return False  # missing second dash
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False  # missing last four digits
    return True


# print(isPhoneNumber('415-555-1234'))

message = 'Call me 415-555-3624 tomorrow, or at 415-555-6546 for my office line.'
foundNumber = False
for x in range(len(message)):
    chunk = message[x:x+12]
    if is_phone_number(chunk):
        print('Phone number: ' + chunk)
        foundNumber = True
if not foundNumber:
    print('Could not find any phone number.')
