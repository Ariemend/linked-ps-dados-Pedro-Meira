import pandas as pd
import streamlit as st
import modulo as m

#Inicializando a base de dados e os elementos base do streamlit
base_de_dados = pd.read_csv('vendas_linked_ps.csv', parse_dates=["order_date"])
st.sidebar.success("Select a page above:")




# Pegar as informações relevantes
total_de_pedidos = len(base_de_dados)
faturamento = base_de_dados["total_value"].sum()
n_vendas_validas = m.vendas_completas(base_de_dados)
n_vendas_canceladas = n_vendas_validas - total_de_pedidos
taxa_cancelamento = m.taxa_de_cancelamento(base_de_dados)
n_pedidos_entregues = m.pedidos_entregues(base_de_dados)
valor_por_mes = m.valortotal_por_mes(base_de_dados)
media_valor_produto = m.media_valor_produto(base_de_dados)

#Construção da pagina em si
st.title("Bem vindo!!",text_alignment="left")
st.caption(f"Uma produção linked.", text_alignment="left")

st.subheader("Estatisticas Gerais da empresa:",text_alignment="center")
col1, col2 = st.columns([3,2],border=True)

with col1:
    col1a, col1b = st.columns(2,wrap=True)
    col1a.metric("Número Total de Pedidos",value=total_de_pedidos,)
    col1a.metric("Pedidos Completos:",value=n_vendas_validas)
    col1b.metric("Pedidos em trânsito",value=n_pedidos_entregues)
    col1b.metric("Taxa de Cancelamento:", value=str(taxa_cancelamento) + "%")

with col2:
    st.metric("Faturamento",value=faturamento,format="accounting")
    st.metric("Media de valor p/ ordem", value=media_valor_produto)

st.line_chart(valor_por_mes,x="mes",y="total_value",x_label="Mês do Ano", y_label="Valor Total")

