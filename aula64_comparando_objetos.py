#id -> retorna um id referente a posição do objeto na memória
#Para fazer comparações customizadas entre objetos podemos utilizar os seguintes métodos

"""
__le__   x <=y
__eq__   x == y
__ge__   x >= y
__lt__   x < y
__gt__   x > y
__ne__   x != y


"""


class Pai():
    pass


print(id(Pai()))

class Conta():
    def __init__(self, ID):
        self.ID = ID
        
        
    def __le__(self, outro):
        if self.ID <= outro.ID:
            return True
        return False
    
    
itau = Conta(3)
itau2 = Conta(3)

print(itau <= itau2)



