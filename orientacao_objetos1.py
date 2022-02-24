class Cachorro:
    def __init__(self): #inicializa o objeto com metodo construtor
        self.nome = 'lucas'
        self.idade = 123
        
        
    def imprime(self, i, n, *args):
        print(self.nome)
        print(self.idade)
        print(i+n)
        
        
        
objeto = Cachorro()

objeto.imprime(2, 4, 5, 6)
        