#binarios

file = open('C:\\Users\\delta\\Desktop\\xcode\\bin.txt', 'w')


file.write('lucas\n')

file.close()


file = open('C:\\Users\\delta\\Desktop\\xcode\\bin.txt', 'rb')

nome = file.read()


print(nome)

nome = file.seek(3)

print(nome)


list  = ['2', '3']

listaa = str(list)

print(listaa)


xc = eval(listaa)

print(xc)








