import re


phoneNumber = re.compile(r'(\d{3}|\(\d{3}\))?(\s|-|\.)?(\d{3}(\s|-|\.)(\d{4}))')

mo = phoneNumber.search('(333) 333-4444')

telefone = mo.group()


#for i in telefone:
#   print(i)

#*lucas
emailRegex = re.compile(r'''[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+(\.[a-zA-Z]{2,4})''', re.VERBOSE)


emailSearch = emailRegex.search('deltaalpha.correia@gmail.com')

email = emailSearch.group()


print(email)


