
def removeEspacos(splited):
    count = 0
    if splited.count('') != 0:
        splited.remove('')
        return count
    return 0

arquivo = open('C:\\Users\\delta\\Desktop\\xcode\\arq.txt', 'r')


linha = arquivo.readline()

usuarios = []
espacoTotal = 0

while linha != '':
    separado = linha.split()
    #print(separado)
    x  = removeEspacos(separado)
    #print('Tem espaços: {} '.format(x))
    
    
    espacoTotal += int(separado[1])
    
    
    
    linha = arquivo.readline()
    

arquivo.close()

espacoTotal = espacoTotal / (1024**2)



def gera_relatorio(usuarios, espacoTotal):
    relatorio = open('C:\\Users\\delta\\Desktop\\xcode\\relatorio.txt', 'w')
    
    usuarios = [['lucas', '343']]    
    i = 0
    linha = '%i'%(i+1)
    linha += (5-len(linha))*' '

    linha += usuarios[i][0] + (15 - len(usuarios[i][0]))*' '

    linha += '324324'

    print(linha)
    
    relatorio.writelines(linha + '\n')
    
    
gera_relatorio(usuarios, espacoTotal)
