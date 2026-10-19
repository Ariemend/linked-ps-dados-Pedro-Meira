import pandas as pd
import streamlit as st
import plotly.express as px
import filtros as fl
import analise as an

#Inicializando a base de dados e os elementos base do streamlit
base_de_dados = pd.read_csv('vendas_linked_ps.csv', parse_dates=["order_date"]) #pega a base de dados, transformando os elementos de "order_date" em datetime
st.sidebar.success("Select a page above:") #inicializa a barra lateral


#Titulo e apresentacao
st.title("Painel de Vendas PS 2024",text_alignment="left")
st.caption("Todas as informações relevantes sobre a empresa PS no ano de 2024. Clique na barra a esquerda para navegar o dashboard",text_alignment="left")
st.divider()

#Primeiras informacoes
col1, col2= st.columns((2),wrap=True,border=True)
count1 = st.container(border=True)

#Pegando os dados relevantes

#coluna 1
pedidos_completos = fl.ordens_por_status(base_de_dados,["Entregue","Em transito"])
receita_total = an.receita_das_ordens(pedidos_completos)

pedidos_em_transito = fl.ordens_por_status(base_de_dados,["Em transito"])
receita_pendente = an.receita_das_ordens(pedidos_em_transito)
porcentagem_pendente = (receita_pendente / receita_total) * 100

#coluna 2
pedidos_cancelados = fl.ordens_por_status(base_de_dados,["Cancelado"])
taxa_cancelamento = an.taxa_cancelamento(base_de_dados)
receita_perdida = an.receita_das_ordens(pedidos_cancelados)
porcentagem_perdida = (receita_perdida / receita_total) * 100

#container 1
total_pedidos = an.numero_das_ordens(base_de_dados)
total_pedidos_entregues = an.numero_das_ordens(pedidos_completos)
total_pedidos_em_transito = an.numero_das_ordens(pedidos_em_transito)
total_pedidos_cancelados = an.numero_das_ordens(pedidos_cancelados)

#Aplicando no streamlit
with col1:
    st.metric("Receita Liquida",receita_total,format="accounting",delta_description="S/ Cancelados")
    st.metric("Receita Pendente",receita_pendente,format="accounting",delta=porcentagem_pendente,delta_description="% Receita Total",delta_arrow="off",delta_color="grey")

with col2:
    st.metric("Receita Perdida",receita_perdida,format="accounting",delta=porcentagem_perdida,delta_description="% Perdida",delta_arrow="off",delta_color="inverse")
    st.metric("Taxa de Cancelamento",taxa_cancelamento,format="percent")

with count1:
    col3a, col3b, col3c = st.columns(3)
    col3a.metric("Total de Pedidos",total_pedidos)
    col3b.metric("N/ Pedidos Em Transito",total_pedidos_em_transito,delta=(round((total_pedidos_em_transito/total_pedidos)*100,2)),delta_color="green",delta_arrow="off")
    col3c.metric("N/ Pedidos Cancelados",total_pedidos_cancelados,delta=(round((total_pedidos_cancelados/total_pedidos)*100,2)),delta_color="red",delta_arrow="off")

#Graficos
col1, col2 = st.columns(2,border=True)
base_por_mes = fl.coluna_por_mes(pedidos_completos)
grafico_valor_por_mes = px.bar(base_por_mes,x="order_date",y="total_value")
grafico_proporcao_metodo = px.pie(base_de_dados,names="payment_method",values="quantity")

with col1:
    st.subheader("Faturamento x Tempo",text_alignment="center")
    st.plotly_chart(grafico_valor_por_mes)
with col2:
    st.subheader("Proporção Metódo de Pagamento",text_alignment="center")
    st.plotly_chart(grafico_proporcao_metodo)


