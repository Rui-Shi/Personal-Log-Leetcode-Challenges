# Given a text file file.txt that contains a list of phone numbers (one per line), write a one-liner bash script to print all valid phone numbers.

# You may assume that a valid phone number must appear in one of the following two formats: (xxx) xxx-xxxx or xxx-xxx-xxxx. (x means a digit)

# You may also assume each line in the text file must not contain leading or trailing white spaces.

# Example:

# Assume that file.txt has the following content:

# 987-123-4567
# 123 456 7890
# (123) 456-7890
# Your script should output the following valid phone numbers:

# 987-123-4567
# (123) 456-7890

import re

def find_valid_phone_numbers(filename):
    """Finds valid phone numbers in a text file.

    Args:
        filename: The name of the text file.

    Returns:
        A list of valid phone numbers found in the file.
    """

    try:
        with open(filename, 'r') as f:
            for line in f:
                line = line.strip()  # Remove leading/trailing whitespace
                if re.match(r"^(\(\d{3}\) \d{3}-\d{4}|\d{3}-\d{3}-\d{4})$", line):
                    valid_phone_numbers.append(line)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return  # Return empty list if file not found
    return valid_phone_numbers

# Example usage:
filename = "file.txt"  # Replace with your file name
valid_numbers = find_valid_phone_numbers(filename)

for number in valid_numbers:
    print(number)