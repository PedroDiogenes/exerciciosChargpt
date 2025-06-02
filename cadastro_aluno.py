'''Cadastro de Alunos
   Crie um dicionário onde a chave é o nome do aluno e o valor é a idade.
   Adicione 3 alunos.
   Permita que o usuário pesquise um aluno e exiba sua idade.'''

lista_aluno ={}

def cadastro_de_alunos():
    for i in range(3):
        nome_do_aluno = input("Digite o nome do aluno: ")
        idade = int(input("Digite a idade do aluno: "))
        lista_aluno[nome_do_aluno] = idade

cadastro_de_alunos()

print(lista_aluno)


