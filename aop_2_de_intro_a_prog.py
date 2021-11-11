# -*- coding: utf-8 -*-
"""aop 2 de intro a prog

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jtZvo4AC2cquaWxc7wfuRjktxQSklaJa
"""



import numpy as np

index = 0

alunos = int(input("Qual é o número de alunos? "))
aop1 = np.zeros(alunos)
aop2 = np.zeros(alunos)
aop3 = np.zeros(alunos)
prova = np.zeros(alunos)
recupera = np.zeros(alunos)
mm = np.zeros(alunos)
nota_final = 0
print("Vamos começar a inserir as notas dos alunos. Primeiro, insira as notas da AOP1")

while index < alunos:
  aop1[index] = float(input(f'Nota [0.0, 1.0] do Aluno {index + 1}: '))
  if aop1[index] < 0.0 or aop1[index] > 1.0:
    print("Errou, tente novamente.")
  else:
    index += 1
if index == alunos:
  index = 0

print("Agora vamos pra AOP2.")

while index < alunos:
  aop2[index] = float(input(f'Nota [0.0, 2.0] do Aluno {index + 1}: '))
  if aop2[index] < 0.0 or aop2[index] > 2.0:
    print("Errou, tente novamente.")
  else:
    index += 1
if index == alunos:
  index = 0

print("Agora, a AOP3.")
while index < alunos:
  aop3[index] = float(input(f'Nota [0.0, 1.0] do Aluno {index + 1}: '))
  if aop3[index] < 0.0 or aop3[index] > 1.0:
    print("Errou, tente novamente.")
  else:
    index += 1
if index == alunos:
  index = 0

print("Finalmente, a nota da prova.")

while index < alunos:
  prova[index] = float(input(f'Nota [0.0, 6.0] do Aluno {index + 1}: '))
  if prova[index] < 0.0 or prova[index] > 6.0:
    print("Errou, tente novamente.")
  else:
    index += 1
if index == alunos:
  index = 0

prova = prova.reshape((alunos,1))
aop1 = aop1.reshape((alunos,1))
aop2 = aop2.reshape((alunos,1))
aop3 = aop3.reshape((alunos,1))
recupera = recupera.reshape((alunos,1))
notas = np.concatenate((aop1, aop2, aop3, prova, recupera), axis=1)
notas

aprovados = 0

while index < alunos:
  mm[index] = aop1[index]+aop2[index]+aop3[index]+prova[index]
  print(f'A média do módulo do aluno {index + 1} é: ', mm[index])
  
  if mm[index]>= 7:
    print(f"Aprovado com {mm[index]} pontos. Parabéns!")
    aprovados += 1
    index += 1
  elif mm[index]<7:
    print("O aluno precisa da prova de recuperação.")
    recupera[index] = float(input(f'Nota [0.0, 10.0] do Aluno {index + 1}: '))
    if recupera[index] < 0.0 or recupera[index] > 10.0:
      print("Errou, tente novamente.")
    nota_final = float((mm[index]+recupera[index])/2)

    if nota_final >= 5:
      print(f"Aprovado com {nota_final} pontos. Parabéns!")
      aprovados += 1
      index += 1
    else:
      print(f"Não deu, o aluno {index+1} foi reprovado com {nota_final} pontos.")
      index+=1
  
porcentagem_de_aprovados = (aprovados/alunos)*100
print(f"A porcentagem de alunos aprovados foi de {porcentagem_de_aprovados} %.")