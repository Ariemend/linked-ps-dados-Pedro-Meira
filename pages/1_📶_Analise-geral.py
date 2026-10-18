import pandas as pd
import streamlit as st
import plotly.express as px
import filtros as fl
import analise as an

#Pegar os dados
base_de_dados = pd.read_csv("vendas_linked_ps.csv",parse_dates=["order_date"]) #pegar os dados do arquivo csv, transformando o "order_date" em datetime

#Analise por Categoria
st.title("Analise das Categorias",text_alignment="center")


st.bar_chart(base_de_dados,x="product_category",y="total_value")

#Analise por categoria
categoria = st.selectbox("Qual Categoria você deseja analisar?",options=base_de_dados["product_category"].unique(),on_change="rerun",placeholder="Escolha uma opção")
base_filtrada_categoria = fl.ordens_por_categorias(base_de_dados,[categoria])

#Analise individual de cada categoria
st.bar_chart(base_filtrada_categoria,x="product_name",y="total_value",x_label="Produto",y_label="Valor total")
analise_dos_elementos = an.analise_de_elementos(base_filtrada_categoria,"product_name")

st.dataframe(analise_dos_elementos)
pizza_elementos_qtd = px.pie(analise_dos_elementos,names="elemento",values="quantidade_vendida",color="elemento")
pizza_elementos_valor = px.pie(analise_dos_elementos,names="elemento",values="total_value",color="elemento")
col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(pizza_elementos_qtd)
with col2:
    st.plotly_chart(pizza_elementos_valor)
