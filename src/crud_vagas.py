# Paulo Marrocos e Cauã dos Santos - CRUD de Vagas

import json
import os
import uuid

CAMINHO = "data/vagas.json"

def carregar_vagas():
    if not os.path.exists(CAMINHO): 
        return [] 
    with open(CAMINHO, "r") as arquivo: 
        return json.load(arquivo)

def salvar_vagas(vagas): 
    with open(CAMINHO, "w") as arquivo: 
        json.dump(vagas, arquivo, indent=4) 

def adicionar_vaga(vaga): 
    vagas = carregar_vagas() 
    vaga["id"] = str(uuid.uuid4())
    vagas.append(vaga) 
    salvar_vagas(vagas) 

def listar_vagas():
    return carregar_vagas() 

def remover_vaga(vaga_id): 
    vagas = carregar_vagas() 
    vagas_filtradas = [vaga for vaga in vagas if str(vaga.get("id")) != str(vaga_id)] 

    if len(vagas) == len(vagas_filtradas): 
        return False
    
    salvar_vagas(vagas_filtradas) 
    return True

def editar_vaga(vaga_id, novos_dados): 
    vagas = carregar_vagas() 
    vaga_encontrada = False 

    for vaga in vagas: 
        if vaga["id"] == vaga_id:
            vaga_encontrada = True 
            vaga.update(novos_dados) 
            break
    
    if vaga_encontrada: 
        salvar_vagas(vagas)
        return True
    else:
        return False