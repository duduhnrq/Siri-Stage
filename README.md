# 🦀 SiriStage - Plataforma de gestão de vagas de estágio, empresas e candidatos.

## 🚀 Sobre o Projeto

Este projeto foi desenvolvido como parte da disciplina **"Fundamentos da Programação"** do curso de **Análise e Desenvolvimento de Sistemas** da **CESAR School**.

O objetivo do projeto foi a prática e o aprofundamento nos conceitos de **CRUDs**, utilizando **dicionários**, manipulação de arquivos **JSON**, além da integração com **Flask** para construção de interfaces web. Durante o desenvolvimento, foram colocados em prática habilidades de organização de dados e manipulação de informações em aplicações web.

## 🔧 Tecnologias Utilizadas

- Python
- Flask
- HTML
- CSS
- JavaScript

## 🧠 Equipe

O desenvolvimento foi dividido em squads, cada um responsável por uma parte do projeto:

- 👨‍💻 **Eduardo Henrique** — *Tech Lead / Front-End*
- 🧠 **Luiz Henrique** e **Pedro Marrocos** — *CRUD de Candidatos*
- 🏢 **Pedro Vinicius** e **Sérgio Gonçalves** — *CRUD de Empresas*
- 📄 **Paulo Marrocos** e **Cauã Santos** — *CRUD de Vagas*

## 📂 Estrutura do Projeto

```bash
Siri-Stage/
├── src/
│   ├── app.py                # Arquivo principal com as rotas Flask
│   ├── crud_candidatos.py    # Operações CRUD para candidatos
│   ├── crud_empresas.py      # Operações CRUD para empresas
│   ├── crud_vagas.py         # Operações CRUD para vagas
│   ├── static/               # Arquivos estáticos (CSS, imagens, JS)
│   └── templates/            # Arquivos HTML (páginas)
│
├── data/                     # Arquivos JSON que armazenam os dados
│   ├── candidatos.json
│   ├── empresas.json
│   └── vagas.json
│
├── requirements.txt          # Dependências do projeto
├── README.md                 # Documentação do projeto
└── .gitignore                # Arquivos e pastas ignorados pelo Git
```

## 🌐 Live Preview

[🔗 SiriStage | Vagas de Estágio](https://siri-stage.onrender.com)

## 💻 Como Rodar o Projeto

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/SiriStage.git
```

2. Acesse a pasta do projeto:

```bash
cd SiriStage/src
```

3. Crie e ative um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv
venv\Scripts\activate  # Windows
# ou
source venv/bin/activate  # macOS/Linux
```

4. Instale as dependências:

```bash
pip install -r requirements.txt
```

5. Execute a aplicação:

```bash
python app.py
```

6. Acesse no navegador:

```bash
http://127.0.0.1:5000/
```
