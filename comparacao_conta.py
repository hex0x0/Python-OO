"""
class Banco:
    def __init__(self):
        self.contas = []
        
        

class Conta:
    def __init__(self, i, s):
        self.ID = i
        self.saldo = s
        
    def deposito(self, v):
        self.saldo += v
    
    def saque(self, v):
        if self.saldo >= v:
            self.saldo -= v
            
            
            
banco = Banco()

itau = Conta(13, 234.0)
bradesco = Conta(43, 3243.0)
banco.contas = [itau, bradesco]


#Não estão definidas as comparações em banco

        
        
        
"""

class Conta:
    def __init__(self, i, s):
        self.ID = i
        self.saldo = s
        
    def deposito(self, v):
        self.saldo += v
    
    def saque(self, v):
        if self.saldo >= v:
            self.saldo -= v




class Contas(list):
    def sort(self):
        copia = self.copy()
        
        tam = len(self) 
        
        self.clear()
        
        while(len(self) < tam):
            min_id = copia[0]
            
            for conta in copia:
                if conta.ID > min_id.ID:
                    min_id = conta
                    
            self.append(min_id)
            copia.remove(min_id)
            
            
            
class Banco:
    def __init__(self):
        self.contas = Contas()
        
        


banco = Banco()

itau = Conta(34, 342.0)
bradesco = Conta(12, 89.0)

banco.contas.append(itau)
banco.contas.append(bradesco)
banco.contas.sort()

print(banco.contas[0].ID)




        
        
          
        
            
    