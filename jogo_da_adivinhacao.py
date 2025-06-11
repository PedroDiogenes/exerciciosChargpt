from random import randint


print('---------JOGO DA ADIVINHACAO----------')

numero_aleatorio = randint(1, 100)

for i in range(10, 1, -1):
    print(f'Voce tem {i} tentativas')
    numero_jogador = int(input("Digite um numero de 1 a 100: "))
    if numero_jogador not in range(1, 100):
        print("Digite um numero de 1 a 100")
        
    if numero_jogador < numero_aleatorio:
        print('maior')
    elif numero_jogador > numero_aleatorio:
        print('menor')
    else:
        print('Voce venceu!')
        break
   
print(f'numero sorteado: {numero_aleatorio}')