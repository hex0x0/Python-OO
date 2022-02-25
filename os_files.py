import os


#Current working directory
print(os.getcwd())
#Change directory
print(os.chdir('c:\\Users\\delta\\Desktop'))

print(os.getcwd())

#Cria um diretorio chamado lucas


try:
    os.makedirs('lucas')
except:
    print('Já existe')




#Converte um path relativo em absoluto
os.path.abspath('c:\\users\\delta\\Desktop')

#Path relativo
#os.path.relpath('alguma coisa')



