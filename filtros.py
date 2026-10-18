import pandas as pd
import numpy as np

#A funcao desse arquivo eh escrever funcoes que vao filtrar a base de dados para obter dados relevantes.
#Sempre retornar um DataFrame apenas com as linhas relevantes.

def ordens_por_status(df,status):
    if len(status) == 0:
        return False
    elif len(status) == 1:
        return df.loc[df["order_status"] == status[0]]
    else:
        return df.loc[df["order_status"].isin(status)]
    
def ordens_por_categorias(df,categoria):
    if len(categoria) == 0:
        return False
    elif len(categoria) == 1:
        return df.loc[df["product_category"] == categoria[0]]
    else:
        return df.loc[df["product_category"].isin(categoria)]

def ordens_por_regioes(df,regiao):
    if len(regiao) == 0:
        return False
    elif len(regiao) == 1:
        return df.loc[df["customer_region"] == regiao[0]]
    else:
        return df.loc[df["customer_region"].isin(regiao)]

def orderns_por_metodos_de_pagamento(df,metodo):
    if len(metodo) == 0:
        return False
    elif len(metodo) == 1:
        return df.loc[df["payment_method"] == metodo[0]]
    else:
        return df.loc[df["payment_method"].isin(metodo)]

def pedidos_por_produtos(df,produtos):
    if len(produtos):
        return False
    elif len(produtos):
        return df.loc[df["product_name"] == produtos[0]]
    else:
        return df.loc[df["product_name"].isin(produtos)]
