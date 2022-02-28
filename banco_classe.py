class Banco(object):
    __total_banco = 100
    taxa_reserva = 0.1
    reserva_exigida = __total_banco * taxa_reserva
    
    def pega_emprestimo(valor):
        Banco.__total_banco -= valor
        
        if Banco.__total_banco >= Banco.reserva_exigida:
            pode = True
        else:
            pode = False
            
           
           
        Banco.__total_banco += valor 
    
        return pode
    
    
obj = Banco()

print('%.i'%obj.reserva_exigida)

print(Banco.pega_emprestimo(3))