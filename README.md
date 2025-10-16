## Phone Number Detector (Two Versions)
This project demonstrates two ways to identify and extract phone numbers in text using Python.

1. **`isPhoneNumber.py`** – A manual implementation that checks each character to validate the phone number format.
2. **`isPhoneNumber2.py`** – A regex-based implementation using Python’s built-in `re` module for faster and more concise pattern matching.

### Overview:
Both scripts are designed to detect phone numbers written in the standard **U.S. format**: For example: `415-555-1011` or `212-999-8888`.

##  1. `isPhoneNumber.py` – Manual Validation Approach
### Description:
This version checks each character of a string manually to determine if it matches the structure of a valid phone number.  
It ensures that:
- The total length is **12 characters**.
- Only digits and two dashes appear.
- The dashes are in the correct positions (after the 3rd and 7th characters).

### Logic Flow:
1. Loop through each character index in a text message.
2. Extract a **12-character segment** at each step.
3. Pass that segment into the `isPhoneNumber()` function.
4. If it matches the phone number pattern, print it.

## 2. isPhoneNumber2.py – Regular Expression Version
### Description:
This version uses the `re` (Regular Expression) module to search for phone numbers much more efficiently.
The regex pattern `\d{3}-\d{3}-\d{4}` looks for:
- Three digits (\d{3})
- A dash
- Three more digits
- Another dash
- Four digits

### Logic Flow:
1. Compile the regex pattern using re.compile().
2. Use .findall() to return all matches in the text.
3. Print each phone number found.
---
### Comparison:
| Feature           | `isPhoneNumber.py`                 | `isPhoneNumber2.py`                    |
| ----------------- | ---------------------------------- | -------------------------------------- |
| **Method**        | Manual character checking          | Regular expressions (`re` module)      |
| **Speed**         | Slower for long texts              | Much faster and more concise           |
| **Code Length**   | Long and detailed                  | Short and powerful                     |
| **Readability**   | Beginner-friendly                  | Intermediate-level                     |
| **Best Use Case** | Teaching logic and string handling | Real-world text parsing and automation |

### Key Takeaways
- Manual checking teaches the logic behind pattern validation.
- Regex simplifies the same task using compact, reusable patterns.
- Both approaches are valuable for learning and can be adapted for more complex data formats (emails, dates, URLs, etc.).
