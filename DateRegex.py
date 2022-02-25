
import re

#Como reconhecer datas válidas com regex?

"""

testeRegex = re.compile('\w+')


so = testeRegex.search('lucas')


print('Match encontrada em índice %s a %s'%(so.start(), so.end()))    
    
"""
dateRegex = re.compile(r'[0-9]{2}(\/|-)?[0-9]{2}(\/|-)?[0-9]{4}')


dt = dateRegex.search('22/04/2021')


