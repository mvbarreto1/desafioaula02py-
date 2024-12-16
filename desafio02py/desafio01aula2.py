def cadastrar_aluno():
    aluno = {}
    

    aluno['nome'] = input("Digite o nome do aluno: ")
    aluno['idade'] = int(input("Digite a idade do aluno: "))
    
    matematica = float(input("Digite a nota de Matemática: "))
    ciencias = float(input("Digite a nota de Ciências: "))
    historia = float(input("Digite a nota de História: "))
    
    aluno['notas'] = (matematica, ciencias, historia)
    
    return aluno

alunos = []

quantidade_alunos = int(input("Quantos alunos você deseja cadastrar? "))

for i in range(quantidade_alunos):
    print(f"\nCadastro do aluno {i+1}:")
    aluno = cadastrar_aluno()
    alunos.append(aluno)

print("\nInformações dos alunos cadastrados:")
for i, aluno in enumerate(alunos):
    print(f"\nAluno {i+1}:")
    print(f"Nome: {aluno['nome']}")
    print(f"Idade: {aluno['idade']}")
    print(f"Notas: Matemática = {aluno['notas'][0]}, Ciências = {aluno['notas'][1]}, História = {aluno['notas'][2]}")
