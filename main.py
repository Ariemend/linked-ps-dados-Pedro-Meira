import pandas as pd
import streamlit as st
import modulo as m

base_de_dados = pd.read_csv('vendas_linked_ps.csv')

st.dataframe(base_de_dados)
# Pegar as informações relevantes

total_de_pedidos = len(base_de_dados)

st.write(m.vendas_completas(base_de_dados))
st.write(total_de_pedidos)
st.write(m.receita_total(base_de_dados))
st.write(m.ticket_medio(base_de_dados))
st.write(m.taxa_de_cancelamento(base_de_dados))
st.line_chart(base_de_dados,x="order_date",y="total_value",x_label="Data",y_label="Valor")