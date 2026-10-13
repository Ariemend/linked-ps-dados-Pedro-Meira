import pandas as pd

base_de_dados = pd.read_csv('vendas_linked_ps.csv')

# Pegar as informações relevantes

def vendas_completas(df):
    vendas_incompletas = df["order_status"] == "Cancelado"
    total = len(df.loc[~vendas_incompletas])
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
    num_cancelamentos = total_de_pedidos - vendas_completas(df)
    print(num_cancelamentos)
    taxa = round((num_cancelamentos / total_de_pedidos) * 100, ndigits=2)
    return taxa