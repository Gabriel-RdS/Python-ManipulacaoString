"""
Documentação link: https://docs.python.org/pt-br/3/library/re.html
"""

# Expressões regulares
import re

texto = "Meu número para contato é 2633-5723"
texto2 = 'numero 99368-4836'

padrao = "[0-9]{4,5}-?[0-9]{4}"
retorno = re.search(padrao, texto)
retorno2 = re.search(padrao, texto2)
print(retorno.group())
print(retorno2.group())