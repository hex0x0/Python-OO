import pyperclip, re

#Testar depois o método de substituição

text = str(pyperclip.paste())

urlRegex = re.compile(r'http(s)?://w{3}\.[a-zA-Z0-9]+\.[a-zA-Z]{2,4}')


url = urlRegex.search(text)

