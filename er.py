""" 1) Escreva uma RE para encontrar números de telefone do tipo:
(091)91234 5678
91 91234 5678
91-91234-5678
(91) 91234-5678

2) Faça uma função que recebe um string e retorna o string com os números de telefones transformados para um único formato:
(91) 91234 5678 """

import re


# primeira questao
re1 = re.search(r'\(\d+\)9\d+.\d+', ' 123123 123 (091)91234 5678 123 123 123 ')
re2 = re.search(r'\d+.9\d+.\d+', '91 91234 5678')
re3 = re.search(r'\d+.9\d+.\d+', '91-91234-5678')
re4 = re.search(r'\(\d+\).9\d+.\d+', '(91) 91234-5678')

print(re1)
print(re2)
print(re3)
print(re4)
