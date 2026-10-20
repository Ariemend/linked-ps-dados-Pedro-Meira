# linked-ps-dados-PedroMeira
Projeto do processo seletivo de dados linked 2026.2

Nome: *Pedro Lima Braga Meira*

## Ferramenta escolhida: Python + Streamlit/Pandas

Eu escolhi utilizar Python para fazer esse projeto pelo fato que tenho um pouco de experiência com a linguagem anteriormente, e a ideia de aprender novas ferramentas dessa linguagem tão importante me empolgou, já que não havia feito um projeto tão complexo antes.

## Como rodar o projeto
Primeiramente, é necessario ter Python instalado na sua máquina, o que pode ser feito [aqui](https://www.python.org).
Feito isso, instale as bibliotecas utilizadas no projeto, que estão agrupadas na pasta requirements.txt. Para instalar todas de uma vez
basta rodar o comando:

**pip install -r requirements.txt**

Após instalar as bibliotecas, so falta rodar o programa em si, abra a pasta contendo os arquivos do projeto no seu terminal e digite o seguinte comando:

**python -m streamlit run Painel-de-Vendas.py**

O projeto deve abrir dentro do seu navegador.

## Insights
Eu juntei um total de 3 Insights sobre os dados que analisei do projeto, eles estão presentes no projeto em sua própria pagina, mas irei resumir eles aqui:


### Insight 1
O primeiro insight que tive foi sobre a diferença entre a proporção da quantidade de produtos vendidos e seu faturamento. Utilizando gráficos de setores, percebi que, em todos os setores os produtos eram vendidos na mesma proporção de 16% a 10%, porém, alguns produtos de algumas categorias eram extremamente mais lucrativos que outros, tomando uma grande parte do faturamento gerado pela categoria. O exemplo mais extremo da base de dados foi na categoria Esportes, onde o produto "Bicicleta Speed Aro 29" foi responsável por 67,9% do faturamento, apesar de representar apenas 14,3% das vendas da categoria. Informações como essa são muito importantes para a empresa, já que ela obtem uma visão mais clara de quais produtos que valem a pena serem mantidos e impulsionados, e quais podem ser cortados.

### Insight 2
O segundo insight foi a respeito do período mais lucrativo da empresa. Após analisar o gráfico de barras contendo o faturamento total pelo tempo, notei que o valor era muito alto no final do ano, investigando um pouco mais, observei que isso era uma tendência em todas as categorias e regiões, sem exceção, pude então concluir que o período mais lucrativo e ativo da empresa é nesse perído. Uma informação dessa é extremamente valiosa para uma empresa, que precisa planejar entregas e estoque.

### Insight 3
O terceiro e último insight analisa as ordens canceladas, e o impacto delas na empresa. Após analisar os dados relevantes, percebi que existem alguns produtos que possuem taxas maiores e menores de cancelamento, mas em geral, as categorias possuem taxas similares apesar de "pequenas". Porém, essas pequenas taxas causam um impacto enorme no faturamento, com uma taxa de apenas 10,42% de cancelamento, a empresa perdeu quase 40 mil reais de faturamente, algo equivalente a 11,39% da receita liquída. Com todas essas informações, pode-se concluir que a forma de combater os cancelamentos é com uma analise individual de cada produto e resolver qualquer problema que ele possa ter.

## Principais Dificuldades
Assim como todo projeto, encontrei diversas dificuldades ao tentar criar esse projeto. Como dito anteriormente, eu nunca tinha feito um projeto de programção dessa forma, o que me possibilitou adquirir vários conhecimentos e práticas novas rapidamente, pois eu tinha que terminar esse projeto em um tempo relativamente curto.


Começando pelo GitHub, eu já tinha noção do o que era e como funcionava, mas nunca havia utilizado na prática, fiquei um tempo descobrindo como se clonava um repósitorio, além de como dar commit e fetch. Após resolver isso, fiquei em dúvida em como eu faria o projeto em si, algo que eu resolvi na tentativa e erro, testando o que deixava o projeto mais legível, acessivel e eficiente. O principal exemplo dessa evolução são os arquivos de apoio filtros.py e analise.py, que surgiram da necessidade de fazer as mesmas operações diversas vezes, além disso, fiz eles com a intenção de serem compativeis uns com os outros, para que eu pudesse analisar e filtrar quaisquer combinações que eu julgasse necessário. No geral, senti que essa foi a parte que eu mais evolui como programador, e aprendi muitas lições de como manter um código acessivel.


Outra questão foi o uso de ferramentas que eu nunca utilizei antes, em especial o pandas. Eu tive uma dificuldade para entender como funcionava os DataFrames, além de ter alguns tropeços com a criação de gráficos no plotly e com o sistema datetime. Para resolver isso, utilizei de varios metódos para aprender como esses sistemas funcionavam, li bastante documentação (a do streamlit é excelente), assisti vídeoaulas e utilizei da IA para explicar conceitos. Com todo esse processo, tive confiança na forma em que organizei a estrutura, páginas e código, e posso explicar a decisão por trâs de cada elemento.

## Possíveis evoluções desse projeto
Apesar de ter feito o meu melhor para realizar esse projeto, tenho algumas ideias que eu gostaria de implementar futuramente, talvez quando tiver um pouco mais de experência utilizando essas ferramentas.


-*Adição de dados novos*: Eu gostaria que fosse possível adicionar novas ordens a base de dados, com todas as métricas e informações recalculadas automáticamente após receber a nova informação


-*Utilização de gráficos geográficos*: Eu vi na documentação do plotly que eles possuem diversos tipos de gráficos, eu tentei usar uma seleção mais váriada nesse projeto, porém acabei desistindo por uma série de razões. O tipo de gráfico que mais chamou a minha atenção foi os geográficos, que mostram um mapa da região analisada, o que seria ótimo de ter na página de analise das regiões, adicionando mas uma faixa de interatividade.


+*Integração de metas*: Eu acho que ia ser uma feature muito legal se o usuário pudesse colocar uma meta de faturamento, e o app mostrasse o quanto que falta para ele atingir essa meta, além de poder criar metas especificas para região, categoria, e produto e analisar cada uma individualmente.

