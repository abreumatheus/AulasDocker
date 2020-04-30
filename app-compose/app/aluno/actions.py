from app.main import db
from .models import Aluno


class AlunoActions:
    def criar(self, nome, sobrenome, idade):
        novo_aluno = Aluno(nome=nome, sobrenome=sobrenome, idade=idade)
        db.session.add(novo_aluno)
        db.session.commit()
        return novo_aluno

    def listar(self):
        alunos = Aluno.query.all()
        return alunos
