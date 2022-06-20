# Email Collector

import re

email = """
Email1: qwedf@gmail.com
Email2: adfdf@gmail.com
Email3: sdfdf@gmail.com
"""

a = re.compile(r'.+@+.')
b = a.finditer(email)
for i in b:
    print(i)