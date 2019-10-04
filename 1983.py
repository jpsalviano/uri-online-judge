alunos = list()
notas = list()

for _ in range(int(input())):
    aluno, nota = [float(i) for i in input().split()]
    alunos.append(aluno)
    notas.append(nota)

maior_nota = max(notas)
melhor_aluno = alunos[notas.index(maior_nota)]
print(int(melhor_aluno)) if maior_nota >= 8 else print('Minimum note not reached')
