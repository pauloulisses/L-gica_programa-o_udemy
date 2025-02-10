# Sistema Escolar

"""
Média < 50 → Reprovado
50 ≤ Média < 60 → Recuperação
Média ≥ 60 → Aprovado

"""

print("Programa que Calcula a Média Escolar\n")

notat = float(input('Digite a nota teórica: '))
notap = float(input('Digite a nota prática: '))
notatr = float(input('Digite a nota do trabalho: '))

media = (notat + notap + notatr) / 3

print(f'A nota do aluno(a) é {media:.2f}')

if media < 50:
    print('Aluno(a) reprovado')

elif 50 <= media < 60:
    print('Aluno(a) em recuperação')

else:
    print('Aluno(a) aprovado por média')
