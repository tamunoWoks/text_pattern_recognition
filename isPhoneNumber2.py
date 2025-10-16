import re  # Import the Regular Expressions module

# Compile a regex pattern that matches phone numbers in the format XXX-XXX-XXXX
phone_num_pattern = re.compile(r'\d{3}-\d{3}-\d{4}')

# Example message containing multiple phone numbers
message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'

# Use findall() to find all matches of the pattern in the message
matches = phone_num_pattern.findall(message)

# If matches are found, print them one by one
for number in matches:
    print('Phone number found: ' + number)

# Print this message when the search is complete
print('Done')


