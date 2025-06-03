from flask import Flask, request, render_template, jsonify, redirect
from crud_candidatos import adicionar_candidato, carregar_candidatos, remover_candidato, editar_candidato
from crud_empresas import adicionar_empresa, carregar_empresas, remover_empresa, editar_empresa
from crud_vagas import adicionar_vaga, carregar_vagas, remover_vaga, editar_vaga

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

# Candidatos

@app.route('/candidatos') 
def candidatos():
    return render_template("candidatos.html")

@app.route('/cadastro-candidato', methods=['POST']) 
def cadastro_candidato(): 
    dados = request.json 

    candidato = { 
        "nome": dados.get("nome"),
        "email": dados.get("email"),
        "telefone": dados.get("telefone"),
        "curso": dados.get("curso"),
        "senha": dados.get("senha")
    }

    adicionar_candidato(candidato) 
    return jsonify({"mensagem": "Usuário cadastrado com sucesso!"}), 200

@app.route('/perfil-candidato') 
def perfil_candidato():
    candidatos = carregar_candidatos() 
    candidato = candidatos[-1] if candidatos else None 
    return render_template("perfil_candidato.html", candidato=candidato)

@app.route('/excluir-candidato', methods=['POST']) 
def excluir_candidato():
    candidatos = carregar_candidatos() 
    indice_ultimo = len(candidatos) - 1 
    sucesso = remover_candidato(indice_ultimo) 
    
    if sucesso:
        return jsonify({"mensagem": "Candidato excluído com sucesso!"}), 200
    else:
        return jsonify({"mensagem": "Erro ao excluir o candidato."}), 400

@app.route('/editar-candidato', methods=['GET', 'POST']) 
def editar_candidato_view():
    candidatos = carregar_candidatos() 
    if not candidatos: 
        return redirect('/')
    
    candidato = candidatos[-1] 
    if request.method == 'POST': 
        dados = request.form 
        novos_dados = { 
            "nome": dados.get("nome"),
            "email": dados.get("email"),
            "telefone": dados.get("telefone"),
            "curso": dados.get("curso")
        }

        editar_candidato(novos_dados) 
        return redirect('/perfil-candidato') 
    return render_template('editar_candidato.html', candidato=candidato)

# Empresas

@app.route('/empresas') 
def empresas(): 
    return render_template("empresas.html")

@app.route('/cadastro-empresa', methods=['POST']) 
def cadastro_empresa():
    dados = request.json 

    empresa = { 
        "nome": dados.get("nome"),
        "cnpj": dados.get("cnpj"),
        "endereco": dados.get("endereco", ""),
        "email": dados.get("email"),
        "telefone": dados.get("telefone"),
        "senha": dados.get("senha")
    }

    adicionar_empresa(empresa) 
    return jsonify({"mensagem": "Empresa cadastrada com sucesso!"}), 200

@app.route('/perfil-empresa') 
def perfil_empresa():
    empresas = carregar_empresas() 
    empresa = empresas[-1] if empresas else None 
    return render_template("perfil_empresa.html", empresa=empresa)

@app.route('/excluir-empresa', methods=['POST']) 
def excluir_empresa(): 
    empresas = carregar_empresas() 
    indice_ultima = len(empresas) - 1 
    sucesso = remover_empresa(indice_ultima) 
    if sucesso:
        return jsonify({"mensagem": "Empresa excluída com sucesso!"}), 200
    else:
        return jsonify({"mensagem": "Erro ao excluir a empresa."}), 400
    
@app.route('/editar-empresa', methods=['GET', 'POST']) 
def editar_empresa_view():
    empresas = carregar_empresas() 
    if not empresas:  
        return redirect('/')

    empresa = empresas[-1]  

    if request.method == 'POST': 
        dados = request.form 

        novos_dados = { 
            "nome": dados.get("nome"),
            "cnpj": dados.get("cnpj"),
            "endereco": dados.get("endereco"),
            "email": dados.get("email"),
            "telefone": dados.get("telefone")
        }

        editar_empresa(novos_dados)
        return redirect('/perfil-empresa')

    return render_template('editar_empresa.html', empresa=empresa)

# Vagas

@app.route('/criar-vagas') 
def vagas():
    return render_template("criar_vagas.html")

@app.route('/criar-vaga', methods=['POST']) 
def criar_vaga():
    dados = request.json 

    empresas = carregar_empresas() 
    nome_empresa = empresas[-1]["nome"] if empresas else None 

    vaga = { # Cria um dicionário com os dados da vaga
        "titulo": dados.get("titulo"),
        "descricao": dados.get("descricao"),
        "local": dados.get("local"),
        "salario": dados.get("salario"),
        "empresa": nome_empresa
    }

    adicionar_vaga(vaga) 
    return jsonify({"mensagem": "Vaga criada com sucesso!"}), 200

@app.route('/vagas') 
def listar_vagas():
    vagas = carregar_vagas() 
    return render_template("vagas_candidato.html", vagas=vagas)

@app.route('/minhas-vagas') 
def minhas_vagas():
    empresas = carregar_empresas() 
    if not empresas: 
        return "Nenhuma empresa cadastrada.", 404

    nome_empresa = empresas[-1]["nome"]  

    todas_vagas = carregar_vagas() # Carrega todas as vagas
    minhas_vagas = [vaga for vaga in todas_vagas if vaga.get("empresa") == nome_empresa] 

    return render_template('vagas_empresa.html', vagas=minhas_vagas, nome_empresa=nome_empresa)

@app.route('/excluir-vaga', methods=['POST']) 
def excluir_vaga():
    dados = request.get_json() 
    vaga_id = dados.get('id') # 

    if remover_vaga(vaga_id): # 
        return jsonify({'mensagem': 'Vaga excluída com sucesso!'}), 200
    else:
        return jsonify({'erro': 'Vaga não encontrada.'}), 404
    
@app.route('/editar-vaga/<vaga_id>', methods=['GET', 'POST'])
def editar_vaga_view(vaga_id):
    vagas = carregar_vagas() 
    vaga = next((vaga for vaga in vagas if vaga.get("id") == vaga_id), None) 

    if not vaga: 
        return "Vaga não encontrada.", 404

    if request.method == 'POST': 
        dados = request.form 

        novos_dados = { 
            "titulo": dados.get("titulo"),
            "descricao": dados.get("descricao"),
            "local": dados.get("local"),
            "salario": dados.get("salario")
        }

        editar_vaga(vaga_id, novos_dados) 
        return redirect('/minhas-vagas') 

    return render_template('editar_vaga.html', vaga=vaga)

if __name__ == '__main__':
    app.run(debug=True)