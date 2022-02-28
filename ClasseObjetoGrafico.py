class ObjetoGrafico(object):
    def __init__(self, cor_preenchimento, preenchido, cor_de_contorno):
        self.cor_preenchimento = cor_preenchimento
        self.preenchido = preenchido
        self.cor_de_contorno = cor_de_contorno
        
    

class Retangulo(ObjetoGrafico):
    def __init__(self, largura, altura, cor_preenchimento, preenchido, cor_de_contorno):
        self.largura = largura
        self.altura = altura
        super(Retangulo, self).__init__(cor_preenchimento, preenchido, cor_de_contorno)
        
    def calculaArea(self):
        return self.largura * self.altura
    
    def perimetro(self):
        return (self.largura + self.altura) * 2
    
    
    
fig_ret = Retangulo(20,4,'marrom',True,'azul')


print(fig_ret.cor_preenchimento)



