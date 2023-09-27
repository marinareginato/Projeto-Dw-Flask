from flask import Flask, render_template
from flask import request

meu_site = Flask(__name__)

@meu_site.route("/")
def homepage():
    return render_template("homepage.html")

@meu_site.route("/contato")
def contato():
    return render_template("contato.html")

@meu_site.route("/usuario")
def dados_usuario():
    nome_usuario= "Marina"
    dados_usuario= {"profissao": "Desenvolvedora", "especialidade":"front-end"}
    return render_template("usuario.html", nome=nome_usuario, dados=dados_usuario)

@meu_site.route("/usuarios/<nome_usuario>;<nome_profissao>")
def usuarios(nome_usuario, nome_profissao):
    dados_usuario= {"profissão": nome_profissao, "especialidade":"front-end"}
    return render_template("usuario.html", nome=nome_usuario, dados=dados_usuario)

@meu_site.route("/autenticar", methods=['GET', 'POST'])
def autenticar():
    usuario = request.args.get('nome_usuario')
    senha = request.args.get('senha')
    return f"usuario: {usuario} e senha {senha}"


if __name__ == "__main__":
    meu_site.run(host='0.0.0.0', port=8080, debug=False)