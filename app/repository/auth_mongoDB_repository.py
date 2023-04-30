from bson.objectid import ObjectId
from decouple import config
from pymongo import MongoClient

from ..models.viewmodels import Usuario

class AuthMongoDBRepository():

    def __init__(self):
        uri = 'mongodb://localhost:27017'
        #uri = config('MONGO_URL')
        client = MongoClient(uri)
        db = client['tarefasUsuarios']
        self.usuarios = db['usuarios']
        try:
            print('Conexão Bem-Sucedida')
        except Exception:
            print('erro!')

    def criar_usuario(self, usuario):
        _id = self.usuarios.insert_one(usuario.toDict()).inserted_id
        usuario.id = str(_id)
        return usuario

    def obter_usuario_por_id(self, id):
        filtro = {'_id': ObjectId(id)}
        usuario = self.usuarios.find_one(filter=filtro)
        return Usuario.fromDict(usuario) if usuario else None

    def obter_usuario_por_email(self, email):
        filtro = {'email': email}
        usuario = self.usuarios.find_one(filter=filtro)
        return Usuario.fromDict(usuario) if usuario else None

    def obter_usuario_por_usuario(self, usuario):
        filtro = {'usuario': usuario}
        usuario = self.usuarios.find_one(filter=filtro)
        return Usuario.fromDict(usuario) if usuario else None