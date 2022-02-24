class Pessoa:
    def __init__(self, nome, peso, cao):
        self.nome = nome
        self.peso = peso
        self.cao = cao
        
    def treinar(self):
        self.cao.daApatinha()
        self.cao.latir()
        
        
        
class Cachorro:
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor
        
    def daApatinha(self):
        print('%s extendeu a patinha'%self.nome)
    def latir(self):
        print('Auaguagdgfdgfdsa')   
        
        
rex = Cachorro('Rex','Yellow')

donoPet = Pessoa('Lucas', 234.0, rex)

donoPet.treinar()
