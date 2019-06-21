#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import randint
from vitaminas import *
from dicas import *
from resposta import *
import cgi

# Lista de alimentos
lista_alimentos = open('lista_alimentos.txt','r').read().split()

#Lista alimentos consumidos
alimentos_consumidos = []
# Instância do formulário
form = cgi.FieldStorage()

# Pegar alimentos selecionados e adicionar na lista de alimentos consumidos.
for ali in lista_alimentos:
	a = form.getvalue(ali)
	# Verificar se o alimento ja está na lista
	if ali in alimentos_consumidos:
		pass
	else:
		# Não pegar o None
		if a in lista_alimentos:
			alimentos_consumidos.append(a)

#alimentos consumidos que nao tem vitaminas
consumidos_sem_vitaminas = []
# lista de alimentos que será sugerido para comer
expe_a=[]
expe_b=[]
expe_c=[]
expe_d=[]
expe_e=[]
expe_k=[]
# lista de vitaminas consumidas
vit_consumida=[]
# lista de vitaminas não cosumidas
vit_nao_consumida=[]
# Lista de alimentos cosumidas separadas por categoria de vitamina
vit_a=[]
vit_b=[]
vit_c=[]
vit_d=[]
vit_e=[]
vit_k=[]
# lista de listas de alimentos consumidos por vitamina
lista_sugestoes=[]
# Verifica vitaminas consumidas e não consumidas.
def verfificar_vitaminas(alimentos_consumidos):
	all_vitaminas=['A', 'B', 'C', 'D', 'E', 'K']
	for alimento in alimentos_consumidos:
		# Criando listas de vitaminas consumidas por categoria
		# Vitamina A
		if alimento in vitaminas[0]:
			vit_a.append(alimento)
		# Vitamina B
		if alimento in vitaminas[1]:
			vit_b.append(alimento)
		# Vitamina C
		if alimento in vitaminas[2]:
			vit_c.append(alimento)
		# Vitamina D
		if alimento in vitaminas[3]:
			vit_d.append(alimento)
		# Vitamina E
		if alimento in vitaminas[4]:
			vit_e.append(alimento)
		# Vitamina K
		if alimento in vitaminas[5]:
			vit_k.append(alimento)		

		for vitamina in vitaminas:
			# VITAMINA A
			if alimento in vitaminas[0]:
				if 'A' in vit_consumida:
					pass
				else:
					if len(vit_a) >= 6:
						vit_consumida.append('A')
			# VITAMINA B
			if alimento in vitaminas[1]:
				if 'B' in vit_consumida:
					pass
				else:
					if len(vit_b) >= 15:
						vit_consumida.append('B')
			# VITAMINA C
			if alimento in vitaminas[2]:
				if 'C' in vit_consumida:
					pass
				else:
					if len(vit_c) >= 9:
						vit_consumida.append('C')
			# VITAMINA D
			if alimento in vitaminas[3]:
				if 'D' in vit_consumida:
					pass
				else:
					if len(vit_d) >= 5:
						vit_consumida.append('D')	
			# VITAMINA E
			if alimento in vitaminas[4]:
				if 'E' in vit_consumida:
					pass
				else:
					if len(vit_e) >= 10:
						vit_consumida.append('E')	
			# VITAMINA K
			if alimento in vitaminas[5]:
				if 'K' in vit_consumida:
					pass
				else:
					if len(vit_k) >= 12:
						vit_consumida.append('K')


			# Montar lista de alimentos consumidos que nao tem vitamina
			if alimento in sem_vitaminas:
				if alimento in consumidos_sem_vitaminas:
					pass
				else:
					consumidos_sem_vitaminas.append(alimento)

	# Montar lista de vitaminas não consumidas
	for vit in all_vitaminas:
		if vit in vit_consumida:
			pass
		else:
			vit_nao_consumida.append(vit)

	# Montar lista de sugestoes de alimentos
	if len(vit_nao_consumida) > 0:
		for vit in vit_nao_consumida:
			if vit == 'A':
				if len(expe_a) < 1:
					expe_a.append(dicas_a)
			if vit == 'B':
				if len(expe_b) < 1:
					expe_b.append(dicas_b)
			if vit == 'C':
				if len(expe_c) < 1:
					expe_c.append(dicas_c)
			if vit == 'D':
				if len(expe_d) < 1:
					expe_d.append(dicas_d)
			if vit == 'E':
				if len(expe_e) < 1:
					expe_e.append(dicas_e)
			if vit == 'K':
				if len(expe_k) < 1:
					expe_k.append(dicas_k)
	#Montar  Lista de listas de susgestoes
	lista_sugestoes.append(expe_a)
	lista_sugestoes.append(expe_b)
	lista_sugestoes.append(expe_c)
	lista_sugestoes.append(expe_d)
	lista_sugestoes.append(expe_e)
	lista_sugestoes.append(expe_k)

verfificar_vitaminas(alimentos_consumidos)


tela_resposta(alimentos_consumidos, vit_consumida, vit_nao_consumida, consumidos_sem_vitaminas, expe_a, expe_b, expe_c, expe_d, expe_e, expe_k)