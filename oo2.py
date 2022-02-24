class Quadrado:
    def __init__(self):
        self.l = 0
        
        
    def setLado(self, l):
        self.l = l
        
    def calculaArea(self, l):
        return l**2
        
        
obj_square = Quadrado()

print(obj_square.calculaArea(2))
        