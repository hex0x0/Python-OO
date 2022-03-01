"""
    
class Cachorro:
    nome = 'Caramelo'
    
    
    
    
Dog = Cachorro()

print(Dog.nome)
print(Cachorro.nome) 




class Conta(object):
    #atributos de classe
    total = 10000
    reserva = 0.1
    
    def __init__(self, ID, saldo):
    
        self.ID = ID
        self.saldo = saldo
    
    def depositar(self, valor):
        self.saldo += valor
        Conta.total += self.saldo
        
    
    def sacar(self, valor):
        if self.saldo >= valor: 
            self.saldo -= valor
    
    def mostra_saldo(self):
        print(self.saldo)
        print(Conta.total)
    
conta_a = Conta(12, 1000)
conta_a.depositar(500)
conta_a.mostra_saldo()








   
    
"""


class Livro(object):
    #Atributos privados são declarados com underscores
    __nome = 100
    def __init__(self):
        pass
    
    def print_value(self):
        print(__nome)    
        

p = Livro()

p.print_value()

