# Define a function that checks whether a string follows the phone number pattern XXX-XXX-XXXX
def isPhoneNumber(text):
    # A valid phone number should be exactly 12 characters long (including dashes)
    if len(text) != 12:
        return False

    # Check that the first three characters are all digits
    for i in range(0, 3):
        if not text[i].isdecimal():  # isdecimal() returns True only if the character is a digit
            return False

    # The fourth character must be a dash
    if text[3] != '-':
        return False

    # Check that the next three characters (positions 4–6) are digits
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False

    # The eighth character must be a dash
    if text[7] != '-':
        return False

    # The last four characters (positions 8–11) must be digits
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False

    # If all checks pass, return True (it’s a valid phone number)
    return True


# Example message containing phone numbers within a sentence
message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'

# Loop through each character index in the message
for i in range(len(message)):
    # Extract a 12-character substring from the current position
    segment = message[i:i+12]

    # Check if this substring matches the phone number pattern
    if isPhoneNumber(segment):
        print('Phone number found: ' + segment)

# Print this message when the search is complete
print('Done')

