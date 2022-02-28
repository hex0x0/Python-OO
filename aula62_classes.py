 

class Mamifero:
    def __init__(self, cor_de_pelo, genero, andar):
        self.cor_de_pelo = cor_de_pelo
        self.genero = genero
        self.num_de_patas = andar
        
    def falar(self):
        print('Ola sou um mamifero e eu sei falar')
        
    def andar(self):
        print('Estou andando sobre %i patas '%self.num_de_patas)
        
    def amamentar(self):
        if self.genero.lower()[0] == 'm':
            print('Machos não amamentam')
            return
        print('Amamentado meu filhote')
        


Rex = Mamifero('Marrom', 'masculino', 4)


Rex.falar()


#Introduzindo herança

class Pessoa(Mamifero):
    def __init__(self, cor_de_pelo, genero, andar):
        super(Pessoa, self).__init__(cor_de_pelo, genero, andar)



Julia = Pessoa('Branca', 'feminino', 2)

Julia.falar()


