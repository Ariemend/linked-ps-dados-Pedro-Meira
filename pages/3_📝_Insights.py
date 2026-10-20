import pandas as pd
import streamlit as st
import plotly.express as px
import filtros as fl
import analise as an

base_de_dados = pd.read_csv("vendas_linked_ps.csv",parse_dates=["order_date"])

st.title("Insights sobre os dados")
st.write("Aqui estão 3 informações que eu extrai dos dados que eu achei relevante destacar")
st.divider()

#Insight 1
st.subheader("Insight 1: A disparidade entre quantidade vendida e faturamento")
st.write("Após analisar as categorias, notei a desproporcionalidade entre a quantidade vendida e o faturamento gerado" \
"por categoria. Por exemplo, as categorias Esportes e Eletrônicos representam menos de 40% dos produtos vendidos, mas são responsaveis" \
"por mais de 50% do faturamento. O contrário também é verdade, a categoria livros representa 14,5% dos produtos vendidos, mas apenas " \
"6% do faturamento.")
st.write("A disparidade aumenta ainda mais quando analisamos as categorias individualmente, usando a categoria Eletrônicos como exemplo," \
"temos o produto Smartphone Samsung Galaxy A54, que representa 10% das vendas de eletrônicos e 50% do faturamento da categoria, e 12,5% do" \
"faturamento total da empresa. Outros produtos dominantes como esse são a Vassoura Elétrica Robô e a Bicicleta Speed Aro 29. Abaixo estão" \
"as estatisticas do Smartphone para melhor visualização.")

base_filtrada_categoria = fl.ordens_por_categorias(base_de_dados,["Eletrônicos"])
analise_elementos_produtos = an.analise_de_elementos(base_filtrada_categoria,"product_name")
pizza_elementos_qtd = px.pie(analise_elementos_produtos,names="elemento",values="quantidade_vendida",color="elemento")
pizza_elementos_valor = px.pie(analise_elementos_produtos,names="elemento",values="total_value",color="elemento")

st.subheader("Proporção p/ quantidade",text_alignment="center")
st.plotly_chart(pizza_elementos_qtd)
st.subheader("Proporção p/ valor",text_alignment="center")
st.plotly_chart(pizza_elementos_valor)

#Insight 2
st.subheader("Insight 2: A festividade das ordens")
st.write("Analisando os dados relacionado a datas, notei uma tendência interessante, a quantidade de ordens aumenta dependendo da época" \
"do ano, atingindo seu valor máximo no final do ano, provavelmente devido a festas desse período. Essa tendência se repete em todas" \
"as categorias e regiões, portanto, cheguei a conclusão que a época do ano mais lucrativa da empresa é o final do ano")

pedidos_completos = fl.ordens_por_status(base_de_dados,["Entregue", "Em transito"])
base_por_mes = fl.coluna_por_mes(pedidos_completos)
grafico_barra_faturamento_tempo = px.bar(base_por_mes,x="order_date",y="total_value",labels={"order_date" : "Data", "total_value" : "Valor total"})
st.subheader("Faturamento X Tempo")
st.plotly_chart(grafico_barra_faturamento_tempo)

#Insight 3
st.subheader("Insight 3: O custo do cancelamento")
st.write("O cancelamento é um prejuizo enorme para a empresa, como foi destacado no painel de vendas, foi perdido quase 40 mil reais" \
"de faturamento, cerca de 11% da receita. A taxa de cancelamento varia muito de acordo com o produto, categoria e região, não existindo uma" \
"'regra' que possa descrever esse comportamento, porém, pode-se analisar cada parte individualmente para determinar quais categorias e " \
"produtos estão causando o maior prejuizo, e tomar uma ação com base nessas informações.")

analise_das_categorias = an.analise_de_elementos(base_de_dados,"product_category")
analise_das_regioes = an.analise_de_elementos(base_de_dados,"customer_region")

grafico_barra_categoria_taxa = px.bar(analise_das_categorias,x="elemento",y="taxa_de_cancelamento",labels={"elemento" : "Categoria", "taxa_de_cancelamento" : "Taxa de Cancelamento"})
grafico_barra_regiao_taxa = px.bar(analise_das_regioes,x="elemento",y="taxa_de_cancelamento",labels={"elemento" : "Região", "taxa_de_cancelamento" : "Taxa de Cancelamento"})

col1, col2 = st.columns(2,border=True)
with col1:
    st.subheader("Taxa de cancelamento por categoria")
    st.plotly_chart(grafico_barra_categoria_taxa)
with col2:
    st.subheader("Taxa de cancelamento por região")
    st.plotly_chart(grafico_barra_regiao_taxa)