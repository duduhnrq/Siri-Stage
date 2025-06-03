# Luiz Henrique e Pedro Marrocos - CRUD de Candidatos

import json
import os

CAMINHO = "data/candidatos.json"

def carregar_candidatos(): 
    if not os.path.exists(CAMINHO): 
        return [] 
    with open(CAMINHO, "r") as arquivo: 
        return json.load(arquivo) 

def salvar_candidatos(candidatos): 
    with open(CAMINHO, "w") as arquivo: 
        json.dump(candidatos, arquivo, indent=4) 

def adicionar_candidato(candidato): 
    candidatos = carregar_candidatos() 
    candidatos.append(candidato) 
    salvar_candidatos(candidatos) 

def listar_candidatos(): 
    return carregar_candidatos() 

def obter_candidato_por_indice(indice): 
    candidatos = carregar_candidatos() 
    if 0 <= indice < len(candidatos):
        return candidatos[indice] 
    
    
    
def atualizar_candidato(indice, candidato_atualizado): 
    candidatos = carregar_candidatos() 
    if 0 <= indice < len(candidatos): 
        candidatos[indice] = candidato_atualizado 
        salvar_candidatos(candidatos) 
        return True
    return False

def remover_candidato(indice): 
    candidatos = carregar_candidatos() 
    if 0 <= indice < len(candidatos): 
        candidatos.pop(indice) 
        salvar_candidatos(candidatos) 
        return True
    return False

def obter_candidato_mais_recente():
    candidatos = carregar_candidatos() 
    if candidatos: 
        return candidatos[-1] 
    return None

def editar_candidato(novos_dados): 
    candidatos = carregar_candidatos() 
    if candidatos: 
        candidatos[-1] = novos_dados 
        salvar_candidatos(candidatos) 
        return True
    return False