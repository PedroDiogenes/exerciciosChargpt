#Conte quantas vezes cada palavra aparece usando um dicionário.

palavras = ['maçã','banana','maçã','laranja','banana','banana']

contagem_de_palavras = {}

for palavra in set(palavras):
    contagem_de_palavras[palavra] = palavras.count(palavra)

print(contagem_de_palavras)