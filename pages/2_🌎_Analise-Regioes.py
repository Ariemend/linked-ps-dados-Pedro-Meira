import pandas as pd
import streamlit as st
import plotly.express as px
import filtros as fl
import analise as an

#pegar os dados
base_de_dados = pd.read_csv("vendas_linked_ps.csv",parse_dates=["order_date"])

#Analise Geral das Regiões
st.title("Analise das regiões brasileiras",text_alignment="center")
st.divider()

grafico_barra_regiao_valor = px.bar(base_de_dados,x="customer_region",y="total_value",labels={"customer_region":"Região", "total_value":"Valor total"})
grafico_setor_regiao_qtd = px.pie(base_de_dados,names="customer_region",values="quantity",)

st.subheader("Faturamento")
st.plotly_chart(grafico_barra_regiao_valor)
st.subheader("Porcentagem das ordens")
st.plotly_chart(grafico_setor_regiao_qtd)



#Obter os dados da região especifica
st.title("Analise individual das regiões")
regiao = st.selectbox(label=None,options=base_de_dados["customer_region"].unique(),on_change="rerun",placeholder="Escolha uma opção")
base_filtrada_regiao = fl.ordens_por_regioes(base_de_dados,[regiao])

#Analise geral da região
qtd_regiao = an.numero_das_ordens(base_filtrada_regiao)
receita_total_regiao = an.receita_das_ordens(fl.ordens_por_status(base_filtrada_regiao,["Entregue","Em transito"]))
ticket_medio_regiao = round(an.ticket_medio(base_filtrada_regiao),2)
taxa_cancelamento_regiao = round(an.taxa_cancelamento(base_filtrada_regiao),2)
grafico_setor_regiao_metodo = px.pie(base_filtrada_regiao,names="payment_method",values="quantity")


col1, col2 = st.columns(2,border=True)
with col1:
    st.metric(label=f"Ordens {regiao}",value=qtd_regiao)
    st.metric(label=f"Receita total {regiao}",value=receita_total_regiao,format="accounting")
with col2:
    st.metric(label=f"Ticket Médio {regiao}",value=ticket_medio_regiao,format="accounting")
    st.metric(label=f"Taxa de cancelamento {regiao}",value=taxa_cancelamento_regiao,format="percent")
st.subheader("% Métodos de pagamento")
st.plotly_chart(grafico_setor_regiao_metodo)

#Analise categoria região
regiao_analisada = an.analise_de_elementos(base_filtrada_regiao,"product_category")
grafico_barra_categoria_regiao_valor = px.bar(regiao_analisada,x="elemento",y="total_value",labels={"elemento" : "Categoria", "total_value" : "Valor total"})
grafico_barra_categoria_regiao_taxa_cancelamento = px.bar(regiao_analisada,x="elemento",y="taxa_de_cancelamento",labels={"elemento" : "Categoria", "taxa_de_cancelamento" : "Taxa de Cancelamento"})
grafico_barra_categoria_regiao_ticket_medio = px.bar(regiao_analisada,x="elemento",y="ticket_medio",labels={"elemento" : "Categoria", "ticket_medio" : "Ticket Medio"})
grafico_barra_categoria_regiao_quantidade = px.bar(regiao_analisada,x="elemento",y="quantidade_vendida",labels={"elemento" : "Categoria", "quantidade_vendida" : "Quantidade Vendida"})

st.subheader("Analise das categorias",text_alignment="center")
col1, col2 = st.columns(2, border=True)
with col1:
    st.subheader("Valor total")
    st.plotly_chart(grafico_barra_categoria_regiao_valor)
    st.divider()
    st.subheader("Quantidade")
    st.plotly_chart(grafico_barra_categoria_regiao_quantidade)
with col2:
    st.subheader("Ticket Médio")
    st.plotly_chart(grafico_barra_categoria_regiao_ticket_medio)
    st.divider()
    st.subheader("Taxa de Cancelamento")
    st.plotly_chart(grafico_barra_categoria_regiao_taxa_cancelamento)
st.dataframe(regiao_analisada)

#Analise cronologica da região
base_regiao_tempo = fl.coluna_por_mes(base_filtrada_regiao)

grafico_pedidos_regiao_tempo = px.bar(base_regiao_tempo,x="order_date",y="n_orders")
grafico_valor_regiao_tempo = px.bar(base_regiao_tempo,x="order_date",y="total_value")

st.subheader("Analise Cronologica",text_alignment="center")
col1, col2 = st.columns(2,border=True)
with col1:
    st.subheader("Ordens X Tempo")
    st.plotly_chart(grafico_pedidos_regiao_tempo)
with col2:
    st.subheader("Valor total X Tempo")
    st.plotly_chart(grafico_valor_regiao_tempo)
