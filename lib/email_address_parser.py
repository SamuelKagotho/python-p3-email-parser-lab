import re

class EmailAddressParser:
    def __init__(self, email_string):
        self.email_string = email_string

    def parse(self):
        email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
        
        emails = re.findall(email_pattern, self.email_string)

        return emails[::-1]
