import pandas as pd
import streamlit as st
import plotly.express as px
import filtros as fl
import analise as an

#Pegar os dados
base_de_dados = pd.read_csv("vendas_linked_ps.csv",parse_dates=["order_date"]) #pegar os dados do arquivo csv, transformando o "order_date" em datetime

#Analise por Categoria
st.title("Analise das Categorias",text_alignment="center")
st.caption("Uma analise voltada as categorias individuais e seus produtos",text_alignment="center")
st.divider()

base_filtrado_faturamento = fl.ordens_por_status(base_de_dados,["Entregue", "Em transito"])
analise_das_categorias = an.analise_de_elementos(base_de_dados,"product_category")

grafico_barra_categoria_valor = px.bar(base_filtrado_faturamento,x="product_category",y="total_value",labels={"product_category" : "Categoria", "total_value" : "Valor total"})
grafico_setor_categoria_valor = px.pie(base_filtrado_faturamento,names="product_category",values="total_value",labels={"product_category" : "Categoria", "total_value" : "Valor total"})
grafico_barra_categoria_qtd = px.bar(base_de_dados,x="product_category",y="quantity",labels={"product_category" : "Categoria", "quantity" : "Quantidade"})
grafico_setor_categoria_qtd = px.pie(base_de_dados,names="product_category",values="quantity",labels={"product_category" : "Categoria", "quantity" : "Quantidade"})
grafico_barra_categoria_taxa = px.bar(analise_das_categorias,x="elemento",y="taxa_de_cancelamento",labels={"elemento" : "Categoria", "taxa_de_cancelamento" : "Taxa de Cancelamento"})

col1, col2 = st.columns(2,border=True)
with col1:
    st.subheader("Faturamento",text_alignment="center")
    st.plotly_chart(grafico_barra_categoria_valor)
    st.plotly_chart(grafico_setor_categoria_valor)
with col2:
    st.subheader("Quantidade vendida",text_alignment="center")
    st.plotly_chart(grafico_barra_categoria_qtd)
    st.plotly_chart(grafico_setor_categoria_qtd)
st.subheader("Taxa de cancelamento")
st.plotly_chart(grafico_barra_categoria_taxa)

st.divider()
#Selecao de categoria
st.title("Analise individual das categorias",text_alignment="center")
st.divider()
categoria = st.selectbox(label=None,options=base_de_dados["product_category"].unique(),on_change="rerun",placeholder="Escolha uma opção")
base_filtrada_categoria = fl.ordens_por_categorias(base_de_dados,[categoria])
base_categoria_tempo = fl.coluna_por_mes(base_filtrada_categoria)

#Analise individual de cada categoria
st.subheader("Valor Total de cada produto",text_alignment="center")
grafico_produto_valor = px.bar(base_filtrada_categoria,x="product_name",y="total_value",labels={"product_name" : "Produto", "total_value" : "Valor Total"})
st.plotly_chart(grafico_produto_valor)

analise_elementos_produtos = an.analise_de_elementos(base_filtrada_categoria,"product_name")

#graficos de proporcao
pizza_elementos_qtd = px.pie(analise_elementos_produtos,names="elemento",values="quantidade_vendida",color="elemento")
pizza_elementos_valor = px.pie(analise_elementos_produtos,names="elemento",values="total_value",color="elemento")

st.subheader("Proporção p/ quantidade",text_alignment="center")
st.plotly_chart(pizza_elementos_qtd)
st.subheader("Proporção p/ valor",text_alignment="center")
st.plotly_chart(pizza_elementos_valor)

#grafico de taxa de cancelamento
st.subheader("Taxa de cancelamento")
grafico_barra_produto_taxa = px.bar(analise_elementos_produtos,x="elemento",y="taxa_de_cancelamento",labels={"elemento" : "Produto", "taxa_de_cancelamento" : "Taxa de cancelamento"})
st.plotly_chart(grafico_barra_produto_taxa)

#grafico de tempo
grafico_categoria_tempo_valor = px.bar(base_categoria_tempo,x="order_date",y="total_value",labels={"order_date" : "Data", "total_value" : "Valor total"})
grafico_categoria_tempo_pedidos = px.bar(base_categoria_tempo,x="order_date",y="n_orders",labels={"order_date" : "Data", "n_orders" : "Número de ordens"})
col1,col2 = st.columns(2,border=True)
with col1:
    st.subheader("Valor total X Tempo")
    st.plotly_chart(grafico_categoria_tempo_valor)
with col2:
    st.subheader("Quantidade de produtos X Tempo")
    st.plotly_chart(grafico_categoria_tempo_pedidos)

st.dataframe(analise_elementos_produtos)
