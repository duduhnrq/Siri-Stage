# Luiz Henrique e Pedro Marrocos - CRUD de Candidatos

import json
import os

CAMINHO = "data/candidatos.json"

def carregar_candidatos(): # Carrega os candidatos do arquivo JSON
    if not os.path.exists(CAMINHO): # Verifica se o arquivo existe
        return [] # Se não existir, retorna uma lista vazia
    with open(CAMINHO, "r") as arquivo: # Abre o arquivo em modo leitura
        return json.load(arquivo) # Carrega o conteúdo do arquivo JSON e retorna como uma lista de dicionários

def salvar_candidatos(candidatos): # Salva a lista de candidatos no arquivo JSON
    with open(CAMINHO, "w") as arquivo: # Abre o arquivo em modo escrita
        json.dump(candidatos, arquivo, indent=4) # Converte a lista de candidatos em JSON e escreve no arquivo com indentação de 4 espaços

def adicionar_candidato(candidato): # Adiciona um novo candidato à lista de candidatos
    candidatos = carregar_candidatos() # Carrega os candidatos existentes
    candidatos.append(candidato) # Adiciona o novo candidato à lista
    salvar_candidatos(candidatos) # Salva a lista atualizada de candidatos no arquivo JSON

def listar_candidatos(): # Lista todos os candidatos cadastrados
    return carregar_candidatos() # Retorna a lista de candidatos carregados do arquivo JSON

def obter_candidato_por_indice(indice): # Obtém um candidato específico pelo índice
    candidatos = carregar_candidatos() # Carrega os candidatos existentes
    if 0 <= indice < len(candidatos): # Verifica se o índice está dentro do intervalo válido
        return candidatos[indice] # Retorna o candidato correspondente ao índice
    
    
    
def atualizar_candidato(indice, candidato_atualizado): # Atualiza um candidato existente pelo índice
    candidatos = carregar_candidatos() # Carrega os candidatos existentes
    if 0 <= indice < len(candidatos): # Verifica se o índice está dentro do intervalo válido
        candidatos[indice] = candidato_atualizado # Atualiza o candidato no índice especificado
        salvar_candidatos(candidatos) # Salva as alterações
        return True
    return False

def remover_candidato(indice): # Remove um candidato existente pelo índice
    candidatos = carregar_candidatos() # Carrega os candidatos existentes
    if 0 <= indice < len(candidatos): # Verifica se o índice está dentro do intervalo válido
        candidatos.pop(indice) # Remove o candidato no índice especificado
        salvar_candidatos(candidatos) # Salva as alterações
        return True
    return False

def obter_candidato_mais_recente(): # Obtém o candidato mais recente
    candidatos = carregar_candidatos() # Carrega os candidatos existentes
    if candidatos: # Verifica se há candidatos cadastrados
        return candidatos[-1] # Retorna o último candidato da lista
    return None

def editar_candidato(novos_dados): # Edita os dados do último candidato cadastrado
    candidatos = carregar_candidatos() # Carrega os candidatos existentes
    if candidatos: # Verifica se há candidatos cadastrados
        candidatos[-1] = novos_dados # Atualiza o último candidato cadastrado
        salvar_candidatos(candidatos) # Salva as alterações
        return True
    return False