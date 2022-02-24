class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
    def setBase(self, b):
        self.base = b
        
    def setAltura(self, a):
        self.altura = a
        
    def calculaArea(self):
        return self.base * self.altura
    
    def calculaPerimetro(self):
        return 2*self.base + 2*self.altura
        
        
objetoRet = Retangulo(2, 3)

objetoRet.setBase(3)
objetoRet.setAltura(3)

print(objetoRet.calculaArea())
print(objetoRet.calculaPerimetro())