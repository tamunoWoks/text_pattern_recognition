## Phone Number Detector (Two Versions)
This project demonstrates two ways to identify and extract phone numbers in text using Python.

1. **`isPhoneNumber.py`** – A manual implementation that checks each character to validate the phone number format.
2. **`isPhoneNumber2.py`** – A regex-based implementation using Python’s built-in `re` module for faster and more concise pattern matching.

### Overview:
Both scripts are designed to detect phone numbers written in the standard **U.S. format**: For example: `415-555-1011` or `212-999-8888`.

##  1. `isPhoneNumber.py` – Manual Validation Approach
### 🔍 Description
This version checks each character of a string manually to determine if it matches the structure of a valid phone number.  
It ensures that:
- The total length is **12 characters**.
- Only digits and two dashes appear.
- The dashes are in the correct positions (after the 3rd and 7th characters).


