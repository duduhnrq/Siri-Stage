# Pedro Vinicius e Sérgio Gonçalves - CRUD de Empresas

import json 
import os 

CAMINHO = "data/empresas.json" 

def carregar_empresas(): 
    if not os.path.exists(CAMINHO): 
        return [] 
    with open(CAMINHO, "r") as arquivo: 
        return json.load(arquivo) 

def salvar_empresas(empresas): 
    with open(CAMINHO, "w") as arquivo: 
        json.dump(empresas, arquivo, indent=4) 

def adicionar_empresa(empresa): 
    empresas = carregar_empresas() 
    empresas.append(empresa) 
    salvar_empresas(empresas) 

def listar_empresas(): 
    return carregar_empresas() 

def obter_empresa_por_indice(indice):
    empresas = carregar_empresas() 
    if 0 <= indice < len(empresas): 
        return empresas[indice] 
    return None

def atualizar_empresa(indice, empresa_atualizada): 
    empresas = carregar_empresas() 
    if 0 <= indice < len(empresas): 
        empresas[indice] = empresa_atualizada 
        salvar_empresas(empresas) 
        return True
    return False

def remover_empresa(indice): 
    empresas = carregar_empresas() 
    if 0 <= indice < len(empresas): 
        empresas.pop(indice) 
        salvar_empresas(empresas) 
        return True
    return False

def obter_empresa_mais_recente(): 
    empresas = carregar_empresas() 
    if empresas: 
        return empresas[-1] 
    return None

def editar_empresa(novos_dados):
    empresas = carregar_empresas() 
    if empresas: 
        empresas[-1] = novos_dados 
        salvar_empresas(empresas) 
        return True
    return False