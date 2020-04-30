from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://admin:123456789@db-server/padawans'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)


from app.aluno.actions import AlunoActions
_ALUNO = AlunoActions()


@app.route('/')
def index():
    todos_os_alunos = _ALUNO.listar()
    return render_template('index.html', alunos=todos_os_alunos)


@app.route('/criar-aluno', methods=['POST'])
def criar_aluno():
    nome = request.form['nome']
    sobrenome = request.form['sobrenome']
    idade = int(request.form['idade'])

    _ALUNO.criar(nome=nome, sobrenome=sobrenome, idade=idade)

    return redirect('/')


if __name__ == '__main__':
    app.run()
