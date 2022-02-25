import re
#Um tipo de validador de senhas
#Não sei bem  o que quero fazer aqui
#Apenas testando mesmo


"""

pwd = re.compile(r'[a-zA-Z]\d\w+$')


password = pwd.findall('fa3222aa')

print(password)



"""

#identifica um arquivo

file = re.compile(r'([a-z]+)(\.|-)?([a-z]{3,4})')


teste = file.findall('pedro.txt ana.docx')


print(teste[0])

string = ''

for i in teste[0]:
    string += i
    
print(string)


