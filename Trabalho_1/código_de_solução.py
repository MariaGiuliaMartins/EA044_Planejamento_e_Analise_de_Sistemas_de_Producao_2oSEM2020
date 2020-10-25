# -*- coding: utf-8 -*-
#Código para solucionar Trabalho T1 EA044 - Formulação de Modelos de Otimização
## Aluno(a): Maria Giulia Martins
## Curso: 34 - Engenharia de Computação

#-------------------------------------------------------------------------------

#   Vamos criar funções que generalizem nosso problema para que, desta forma, 
#possamos resolver este tipo de problema, mas com funções diferentes.
#   Uma observação é válida: a nossa restrição de p > 0 sempre se manterá, 
#pois o nosso objetivo é o lucro e, portanto, não podemos ter um preço negativo

#-------------------------------------------------------------------------------

#Função que determina o preço:
def preco(q):
  '''
    Função preco
    Input: array q que representa os coeficientes da nossa expressão que será 
  maximizada
    Output: função de preço
  '''
  return 10 - 0.01*q[0]

#Função que determina o custo:
def custo(q):
  '''
    Função custo
    Input: array q que representa os coeficientes da nossa expressão que será 
  maximizada
    Output: função de custo
  '''
  return 500 + 5*q[0]

#Função que determina a receita:
def receita(q):
  '''
    Função receita
    Input: array q que representa os coeficientes da nossa expressão que será 
  maximizada
    Output: função de receita
  '''
  return preco(q) * q[0]

#Agora vamos implementar nossa função Lucro:
def lucro(q):
  '''
      Função lucro
      Input: array q que representa os coeficientes da nossa expressão que será 
    maximizada
      Output: -[l(r, c)] Retorna a nossa função de lucro multiplicada por -1, 
    pois queremos maximizá-la e sabemos que max(l(r, c)) = - min(l(r, c))
  '''
  return - (receita(q) - custo(q))

#-------------------------------------------------------------------------------

# Agora vamos propriamente aplicar nosso modelo de solução no nosso problema:
##Bibliotecas que usaremos
import scipy.optimize as op
import numpy as np
from scipy.optimize import Bounds

q1 = np.array([1]) #array de entrada

p1 = preco(q1) #preço

c1 = custo(q1) #custo

r1 = receita(q1) #receita

l1 = lucro(q1) #lucro

limites = Bounds([0], [np.inf]) #nossos limitantes

sol = op.minimize(lucro, q1, bounds = limites) #aplicando o solver

for i in sol.x: resultado = i #salvando nosso resultado em uma forma bonita

#printando resultados de interesse
print("Quantidade de Creme a ser produzida:", resultado.round())
print("Preço do Creme:", preco(sol.x).round())
print("Lucro correspondente a essa produção:", -lucro(sol.x).round())
