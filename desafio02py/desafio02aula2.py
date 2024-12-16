def cadastrar_aluno():
    aluno = {}
    
    aluno['nome'] = input("Digite o nome do aluno: ")
    aluno['idade'] = int(input("Digite a idade do aluno: "))
    
    matematica = float(input("Digite a nota de Matemática: "))
    ciencias = float(input("Digite a nota de Ciências: "))
    historia = float(input("Digite a nota de História: "))
  
    aluno['notas'] = (matematica, ciencias, historia)
    
    return aluno

def calcular_media(notas):
    return sum(notas) / len(notas)


alunos = []


quantidade_alunos = int(input("Quantos alunos você deseja cadastrar? "))


for i in range(quantidade_alunos):
    print(f"\nCadastro do aluno {i+1}:")
    aluno = cadastrar_aluno()
    alunos.append(aluno)

def visualizar_alunos():
    print("\nInformações dos alunos cadastrados:")
    for i, aluno in enumerate(alunos):
        media = calcular_media(aluno['notas'])
        print(f"\nAluno {i+1}:")
        print(f"Nome: {aluno['nome']}")
        print(f"Idade: {aluno['idade']}")
        print(f"Notas: Matemática = {aluno['notas'][0]}, Ciências = {aluno['notas'][1]}, História = {aluno['notas'][2]}")
        print(f"Média: {media:.2f}")
        
def aluno_com_melhor_media():
    melhor_media = -1
    aluno_melhor = None
    for aluno in alunos:
        media = calcular_media(aluno['notas'])
        if media > melhor_media:
            melhor_media = media
            aluno_melhor = aluno
    return aluno_melhor, melhor_media

visualizar_alunos()

aluno_melhor, melhor_media = aluno_com_melhor_media()
if aluno_melhor:
    print("\nAluno com a melhor média:")
    print(f"Nome: {aluno_melhor['nome']}")
    print(f"Média: {melhor_media:.2f}")
