from pydantic import BaseModel, Field, EmailStr

class Tarefa(BaseModel):
    id: str | None
    descricao: str
    responsavel: str| None
    nivel: int
    situacao: str | None
    prioridade: int
    usuario_id: str | int | None

    class Config:
        orm_mode = True

    @classmethod
    def fromDict(cls, tarefa):
        usuario_id = tarefa.get('usuario_id')
        if usuario_id is not None:
            usuario_id = str(usuario_id)
        return Tarefa(
            id=str(tarefa['_id']),
            descricao=tarefa['descricao'],
            responsavel=tarefa.get('responsavel'),
            nivel=tarefa['nivel'],
            situacao=tarefa.get('situacao'),
            prioridade=tarefa['prioridade'],
            usuario_id=usuario_id
        )

    
    def toDict(self):
        return {
            "descricao": self.descricao,
            "responsavel": self.responsavel,
            "nivel": self.nivel,
            "situacao": self.situacao,
            "prioridade": self.prioridade,
            "usuario_id": self.usuario_id,
        }

class UsuarioSimples(BaseModel):
    id: int | None | str
    nome: str = Field(min_length=3)
    usuario: str = Field(min_length=5)
    email: EmailStr

    def toDict(self):
        return {
            "nome": self.nome,
            "usuario": self.usuario,
            "email": self.email,
            "senha": self.senha,
        }

class Usuario(UsuarioSimples):
    senha: str = Field(min_length=6)

    @classmethod
    def fromDict(cls, usuario_dict):
        return Usuario(**usuario_dict, id=str(usuario_dict['_id']))

class CriarUsuario(Usuario):
    confirmacao_senha: str

class LoginData(BaseModel):
    usuario: str = Field(min_length=5)
    senha: str = Field(min_length=6)
    