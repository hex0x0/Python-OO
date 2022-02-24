def find(string, sub):
    
    for i in range(len(string)+1-len(sub)):
        
        if string[i:i+len(sub)] == sub:
            return True
        
    return False

def index(string, sub):
    
    for i in range(len(string)+1-len(sub)):
        
        if string[i:i+len(sub)] == sub:
            return i
        
    return None



def count(string, sub):
    aux = 0
    for i in range(len(string)+1-len(sub)):
        
        if string[i:i+len(sub)] == sub:
            aux += 1
        
    return aux    
        
print(count('lucass', 's'))


#implemente replace por conta propria

def replace(phrase, sep, substitute):
    word = ''
    #lucas , uc , ja
    for i in range(len(phrase)+1-len(sep)):
        if phrase[i:i+len(sep)] != sep:
            word += phrase[i]
        else:
            i += len(sep)
            word += substitute
            continue
        
        i+= 1
    
    word += phrase[i:]
    return word

print(
replace('lucas', 'uca', 'ja'))       
