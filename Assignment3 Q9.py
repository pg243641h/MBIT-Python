import re

text = "Please contact us at support@example.com or sales@example.org. Also, you can reach out to info@example.net for more info."
emails = re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', text)
print("Extracted emails:", emails)

def is_valid_date(date_str):
    pattern = r'^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$'
    return bool(re.match(pattern, date_str))

date_to_test = "2023-04-15"
print("Is valid date (2023-04-15):", is_valid_date(date_to_test))
invalid_date = "2023-13-40"
print("Is valid date (2023-13-40):", is_valid_date(invalid_date))

sample_text = "Hello world! Hello everyone! Hello, how are you?"
replaced_text = re.sub(r'\bHello\b', "Hi", sample_text)
print("Replaced text:", replaced_text)

split_string = re.split(r'\W+', "Hello, world! Welcome to Python programming 101.")
print("Split string:", split_string)
