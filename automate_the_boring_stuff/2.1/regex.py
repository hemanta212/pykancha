import re

data = '''r
Dave Martin
615-555-7164
173 Main St., Springfield RI 55924
davemartin@bogusemail.com

Charles Harris
800-555-5669
969 High St., Atlantis VA 34075
charlesharris@bogusemail.com  lsdkjfd
'''

pattern = re.compile(r'\w+@\w+\.com')
matches = pattern.finditer(data)

for match in matches:
    print(match)
