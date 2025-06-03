'''Cadastro de Alunos
   Crie um dicionário onde a chave é o nome do aluno e o valor é a idade.
   Adicione 3 alunos.
   Permita que o usuário pesquise um aluno e exiba sua idade.'''

lista_aluno = {'Pedro': 14, 'Luan': 6, 'Ana': 14}

nome = 'Pedro'
def cadastro_de_alunos():
    for i in range(3):
        nome_do_aluno = input("Digite o nome do aluno: ").capitalize()
        idade_do_aluno = int(input("Digite a idade do aluno: "))
        lista_aluno[nome_do_aluno] = idade_do_aluno

def pesquisar_idade():
    nome = input('digite o nome o aluno: ').capitalize()
  
    print(f'Idade do aluno: { lista_aluno[nome]}')

cadastro_de_alunos()
print(' ')
pesquisar_idade()


