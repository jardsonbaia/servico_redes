#!/usr/bin/python3
# -*- coding: utf-8 -*-
import random
from vitaminas import *

# sorter três alimentos de cada lista de Vitamina
dicas_a = random.sample(vitamina_a2, 3)
dicas_b = random.sample(vitamina_b2, 3)
dicas_c = random.sample(vitamina_c2, 3)
dicas_d = random.sample(vitamina_d2, 3)
dicas_e = random.sample(vitamina_e2, 3)
dicas_k = random.sample(vitamina_k2, 3)

# Page
dicas = '''
	<div class="Dicas">

				<div class="DicasItem">
					
					<h4>Dica 1: Comer pão no café da manhã.</h4>
					<p>É recomendado o consumo diário de até 6 porções de alimentos ricos em carboidrato. O pãozinho garante
						energia para encarar o dia.</p>
					</div>

				<div class="DicasItem">
					
					<h4>Dica 2: Comer frutas, verduras, legumes.</h4>
					<p>São recomendadas três porções de frutas e três de verduras por dia. Os vegetais facilitam a digestão
						e combatem o colesterol ruim.</p>
					</div>

				<div class="DicasItem">
					
					<h4>Dica 3: Comer feijão com arroz.</h4>
					<p>A combinação é rica em proteínas e faz muito bem à saúde. O Ministério recomenda uma proporção de uma
						parte de feijão para duas de arroz.</p>
					</div>

				<div class="DicasItem">
					
					<h4>Dica 4: Temperar a salada com limão.</h4>
					<p>A vitamina C vinda de frutas aumenta o benefício do ferro e de outros minerais de origem vegetal.</p>
					
				</div>
				<div class="DicasItem">
					
					<h4>Dica 5: Coma carne vermelha e peixe.</h4>
					<p>Um pedaço de carne, mesmo pequeno também aumenta a absorção de ferro. O peixe contém gordura
						insaturada que não faz mal a saúde. </p>
					</div>

				<div class="DicasItem">
					
					<h4>Dica 6: Tome leite.</h4>
					<p>Leite tem proteínas, vitaminas e é a nossa principal fonte de cálcio. É u alimento essencial em todas
						as fases da vida. </p>
					</div>

				<div class="DicasItem">
					
					<h4>Dica 7: Coma coração de galinha.</h4>
					<p>É uma importante fonte de ferro, que combate a anemia, principalmente em crianças, jovens, idosos e
						mulheres em idade fértil.</p>
					</div>

				<div class="DicasItem">
					
					<h4>Dica 8: Dançar.</h4>
					<p>O Ministério da Saúde recomenda pelo menos 30 minutos de atividade física todos os dias. Dançar é uma
						maneira fácil e divertida de cumprir a meta.</p>
					</div>

				<div class="DicasItem">
					
					<h4>Dica 9: Caminhar.</h4>
					<p>Melhor quee correr por ai é caminhar. O Ministério da Saúde recomenda pequenos intervalos ao longo do
						dia para uma caminhada rápida.</p>
					</div>

				<div class="DicasItem">
					
					<h4>Dica 10: Beber água de boa qualidade.</h4>
					<p>Água, água de coco e sucos naturais fazem muito bem à saúde, principalmente no verão. A recomendação
						é beber de seis a oito copos por dia.</p>
						<a class="fonte "href="http://g1.globo.com/bemestar/noticia/2012/04/arroz-e-feijao-sao-uma-combinacao-completa-de-proteinas-vegetais.html">FONTE
						</a> 
					</div>

					<div class="DicasItem">

						<h4>Dica 11: Então, se você é um amante de cerveja, tem um motivo para se alegrar. Veja como
							você pode incorporar a cerveja em sua vida além de uma simples bebida.</h4>
							
							<p>Cerveja hidrata igual água, deixa o coração mais saudável, acalma uma dor de estômago, aumenta os níveis de vitamina, redução do risco de câncer.</p>
								<a class="fonte" href="https://manualdohomemmoderno.com.br/cerveja/15-beneficios-da-cerveja-para-sua-saude">FONTE
								</a> 
							</div>
						
							<div class="DicasItem">
								<h4>Dica 12: </h4>
								<p>A ingestão da Cafeína pode aumentar a capacidade de trabalho do coração, sendo
									um poderoso antídoto a depressão, melhora o “estado de alerta”, audição, visão e concentração.
									Em excesso traz alguns malefícios como ansiedade, dor de cabeça, insônia e irritabilidade. Visto
									isso é necessário atenção e controle com a ingestão dessa bebida, a estudos em que comprovam que
									a caféina pode induzir a perda de cálcio pela urina. Quando esse hábito é somado a outros
									fatores de risco como fumo e sedentarismo, pode levar a osteoporose. É considerado uma dose
									segura de café até quatro xícaras por dia, assim você pode aproveitar os benefícios da cafeína.
								</p>
								
								<a class="fonte "href="http://restauranteoberro.com.br/sem-categoria/cafe-com-leite/">FONTE </a> </div> </div>
							</div>
							</div> 

'''