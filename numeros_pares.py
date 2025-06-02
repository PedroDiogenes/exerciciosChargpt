#Crie uma nova lista apenas com os números pares.

numeros = [1,2,3,4,5,6,7,8,9,10]
numeros_pares = []

for i in numeros:
    if i % 2 == 0:
        numeros_pares.append(i)

print(numeros)
print(numeros_pares)