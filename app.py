from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

usuarios = []

class Usuario:
    def __init__(self, cpf, nome, data_nascimento):
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

@app.route('/usuarios', methods=['POST'])
def criar_usuario():
    usuario_data = request.get_json()
    cpf = usuario_data.get('cpf')
    nome = usuario_data.get('nome')
    data_nascimento = datetime.strptime(usuario_data.get('data_nascimento'), '%Y-%m-%d').date()
    usuario = Usuario(cpf, nome, data_nascimento)
    usuarios.append(usuario)
    return jsonify({'Mensagem': 'Usuario criado com sucesso'})

@app.route('/usuarios/<cpf>', methods=['GET'])
def get_usuario(cpf):
    for usuario in usuarios:
        if usuario.cpf == int(cpf):
            return jsonify({
                'cpf': usuario.cpf,
                'nome': usuario.nome,
                'data_nascimento': usuario.data_nascimento.strftime('%Y-%m-%d')
            })
    return jsonify({'Mensagem': 'Usuário não encontrado'})

if __name__ == '__main__':
    app.run(debug=True)