#!/usr/bin/env python
# -*- coding: utf-8 -*-
from style import style
from dicas import dicas



def tela_resposta(ali_consumidos, vit_consumidas, vit_nao_consumidas, consumidos_sem_vitaminas, expe_a, expe_b, expe_c, expe_d, expe_e, expe_k):
	

	# Tratamento de alimentos cosumidos que nao possuem vitamina
	if len(consumidos_sem_vitaminas) < 1:
		consumidos_sem_vitaminas = 'Você não consumiu nenhum alimento pobre em vitaminas!'
	else:
		consumidos_sem_vitaminas = ', '.join(consumidos_sem_vitaminas)

	#aux_a = expe_a[0]
	# Sugestoes de lista de alimentos
	
	if len(expe_a) < 1:
		expe_a = 'Você ingeriu a quanidade adequada!'
	else:
		expe_a = ', '.join(expe_a[0])
	if len(expe_b) < 1:
		expe_b = 'A quanidade consumida está de acordo!'
	else:
		expe_b = ', '.join(expe_b[0])
	if len(expe_c) < 1:
		expe_c = 'O nível de vitamina está apropriado!'
	else:
		expe_c = ', '.join(expe_c[0])
	if len(expe_d) < 1:
		expe_d = 'Você ingeriu a quanidade adequada!'
	else:
		expe_d = ', '.join(expe_d[0])
	if len(expe_e) < 1:
		expe_e = 'A quanidade consumida está de acordo!'
	else:
		expe_e = ', '.join(expe_e[0])
	if len(expe_k) < 1:
		expe_k = 'O nível de vitamina está apropriado!'
	else:
		expe_k = ', '.join(expe_k[0])

	# Transformando listas em strings e tratando a saida
	# Alimentos consumidos
	ali_consumidos = ', '.join(ali_consumidos)
	# Vitaminas Consumidas
	if len(vit_consumidas) < 1:
		vit_consumidas = 'Quantidade insuficiente de vitaminas!'
	else:
		vit_consumidas = ', '.join(sorted(vit_consumidas))
	# Vitaminas não consumidas
	if len(vit_nao_consumidas) < 1:
		vit_nao_consumidas = 'Você consumiu todas as vitaminas necessárias para sua alimentação diária!'	
	else:
		vit_nao_consumidas = ', '.join(sorted(vit_nao_consumidas))



	# Mostar Tela
	print('''Content-type: text/html\n\n 
		<!DOCTYPE html>
		<html lang="pt-br">
		<head>
			<meta charset=iso-utf-8"/>
			{}
		</head>
		<body>	
		<div class="Fundo">

		<div class="Titulo">
			<h2>Resultado da Consulta</h2>
		</div>

		<div class="Conteudo">

			<div class="Vitaminas">

				<div class="VitaminasItem">
					<h5>Vitaminas Consumidas: </h5>
					<h6>
					{}
					</h6>
				</div>
				<div class="VitaminasItem">
					<h5>Vitaminas não Consumidas: </h5>
					<h6>
					{}
					</h6>
				</div>
				<div class="VitaminasItem">
					<h5 class="consumidos">Alimentos consumidos que não oferecem nenhuma quantidade considerável de vitamina: </h5>
					<h6>
					{}
					</h6>
				</div>
				
					<h5>Algumas sugestões de alimentos para reforçar sua alimentação: </h5>
				
				<div class="VitaminasItem">
					<h5>Alimentos que contêm vitamina A: </h5>
					<h6>
					{}
					</h6>
				</div>
				<div class="VitaminasItem">
					<h5>Alimentos que contêm vitamina B: </h5>
					<h6>
					{}
					</h6>
				</div>
				<div class="VitaminasItem">
					<h5>Alimentos que contêm vitamina C: </h5>
					<h6>
					{}
					</h6>
				</div>
				<div class="VitaminasItem">
					<h5>Alimentos que contêm vitamina D: </h5>
					<h6>
					{}
					</h6>
				</div>
				<div class="VitaminasItem">
					<h5>Alimentos que contêm vitamina E: </h5>
					<h6>
					{}
					</h6>
				</div>
				<div class="VitaminasItem">
					<h5>Alimentos que contêm vitamina K: </h5>
					<h6>
					{}
					</h6>
				</div>
				<br>
				<div class="divBotao">
				<input class="botao" type="button" value="Home" onClick="history.go(-1)">
				</div>
			</div>
			{}
			</body></html>'''.format(style, vit_consumidas, vit_nao_consumidas, consumidos_sem_vitaminas, expe_a, expe_b, expe_c, expe_d, expe_e, expe_k, dicas))
