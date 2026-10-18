import pandas as pd
import numpy as np
import filtros as fl

#A funcao desse arquivo é criar as funcoes que vao analisar os DataFrames e retornar dados que realmente importam
#A maioria dessas funcoes provavelmente vai retornar um int

def numero_das_ordens(df):
    return len(df["order_id"])

def receita_das_ordens(df):
    return df["total_value"].sum()

def ticket_medio(df):
    qtd = numero_das_ordens(df)
    valor = receita_das_ordens(df)
    return valor / qtd

def taxa_cancelamento(df):
    cancelados = fl.ordens_por_status(df,["Cancelado"])
    numero = numero_das_ordens(df)
    return (len(cancelados) / numero)

def analise_de_elementos(df,coluna):
    elementos_e_valores = {
        "elemento" : [],
        "total_value" : [],
        "ticket_medio" : [],
        "taxa_de_cancelamento" : [],
        "quantidade_vendida" : [],
    }
    for i in df[coluna].unique().tolist():
        filtro = df.loc[df[coluna] == i]
        elementos_e_valores["elemento"].append(i)
        elementos_e_valores["total_value"].append(receita_das_ordens(filtro))
        elementos_e_valores["ticket_medio"].append(round(ticket_medio(filtro),2))
        elementos_e_valores["taxa_de_cancelamento"].append(round(taxa_cancelamento(filtro),2))
        elementos_e_valores["quantidade_vendida"].append(filtro["quantity"].sum())

    elementos_e_valores = pd.DataFrame(elementos_e_valores)
    return elementos_e_valores