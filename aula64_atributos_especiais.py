class Banco:
    """
        Descricao banco
    
    """
    def __init__(self, ID, saldo):
        self.ID = ID
        self.saldo = saldo
        
    def __str__(self):
        return 'ID: %i\nSaldo: R$ %.2f'%(self.ID, self.saldo)
    
    #def __add__(self, valor):
    #   self.saldo += valor
    
    def __add__(self, other):
        self.saldo += other.saldo
        
        
    def __call__(self, x):
        print(x)
        
    
bradesco = Banco(23, 234.0)
itau = Banco(32, 234.5)
print(bradesco + itau)
print(bradesco.__doc__)


class Pai:
    pass


class Filha(Pai):
    pass


print(issubclass(Pai, Filha))
print(issubclass(Filha, Pai))    

#Informa o pai da classe

print(Filha.__bases__) 


#Objeto 'chamável'

callable(Pai)

i = Pai()