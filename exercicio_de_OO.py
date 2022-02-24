class Ponto:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        
        
    def print_xy(self):
        print('X = %d e Y = %d'%(self.x, self.y))
        
    
class Retangulo:
    def __init__(self, largura, comprimento, ponto = Ponto()):
        self.largura = largura
        self.comprimento = comprimento
        #recebe um objeto do tipo ponto
        verticeInicial = ponto
        
        
    def achaCentro(self):
        x = self.verticeInicial.x + self.largura/2
        y = self.verticeInicial.y + self.comprimento/2
        #retorna um objeto do tipo ponto
        return Ponto(x, y)
        
    
    