class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        
        
    def envelhecer(self):
        if self.idade < 21:
            self.altura += 0.5
        self.idade += 1
        return self.idade
   
    def engordar(self, peso):
        self.peso +=peso
        return self.peso
        
    def emagrecer(self, peso):
        self.peso -=peso
        return self.peso
        
    
             
   
        
        
p = Pessoa('joao', 14, 70.0, 1.75)

print(p.engordar(23))

        
    