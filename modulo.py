import pandas as pd

base_de_dados = pd.read_csv('vendas_linked_ps.csv')

# Pegar as informações relevantes

def vendas_completas(df):
    vendas_completas = df["order_status"] == "Entregue"
    total = len(df.loc[vendas_completas])
    return total

total_de_pedidos = len(base_de_dados)

def receita_total(df):
    total = df["total_value"].sum()
    return total

def ticket_medio(df):
    vendas_validas = vendas_completas(df)
    total_vendas = receita_total(df)
    tm = round(total_vendas / vendas_validas, 2)
    return tm

def taxa_de_cancelamento(df):
    num_cancelamentos = total_de_pedidos - (vendas_completas(df) + pedidos_entregues(df))
    print(num_cancelamentos)
    taxa = round((num_cancelamentos / total_de_pedidos) * 100, ndigits=2)
    return taxa

def pedidos_entregues(df):
    vendas_nao_entregues = df["order_status"] == "Em transito"
    total = len(df.loc[vendas_nao_entregues])
    return total

def valortotal_por_mes(df):
    total_mensal = df.groupby(df["order_date"].dt.to_period("M"))["total_value"].sum().reset_index()
    total_mensal.columns = ["mes", "total_value"]
    total_mensal["mes"] = total_mensal["mes"].dt.to_timestamp()
    return total_mensal

def media_valor_produto(df):
    faturamento = df["total_value"].sum()
    media = round(faturamento / total_de_pedidos,  ndigits=2)
    return media