from Banco import Banco

class Usuario:

    def __init__(self, email, senha, coordernada_x, coordenada_y, coordenada_x_2, coordenada_y_2, id=0):
        self.__id = id
        self.__email = email
        self.__senha = senha
        self.__coord_x = coordernada_x
        self.__coord_y = coordenada_y
        self.__coord_x_2 = coordenada_x_2
        self.__coord_y_2 = coordenada_y_2

    def inserir_usuario(self):
        banco = Banco()

        try:
            cursor = banco.get_banco.cursor()

            cursor.execute("""insert into usuario (email, senha, x, y, x_2, y_2) values ('{}', '{}', '{}', '{}', '{}',
            '{}')""".format(self.__email, self.__senha, self.__coord_x, self.__coord_y, self.__coord_x_2, self.__coord_y_2))

            banco.get_banco.commit()
            cursor.close()

            return "Cadastro realizado com sucesso"
        except:
            return "Aconteceu algum erro no cadastro"

    @classmethod
    def delete_user(self, email='', id=''):
        banco = Banco()

        try:
            cursor = banco.get_banco.cursor()

            if email != '':
                cursor.execute(f"delete from usuario where email = '{email}';")
                banco.get_banco.commit()
                return ('Usuario exluido com sucesso')
            elif id != '':
                cursor.execute(f"delete from usuario where id = '{id}';")
                banco.get_banco.commit()
                return ('Usuario exluido com sucesso')
            else:
                return 'O usuario não foi encontrado'
        except:
            return 'Ocorreu um erro ao apagar o usuario!'

    def select_user(self, id):
        banco = Banco()

        try:
            cursor = banco.get_banco.cursor()
            dados = cursor.execute(f"select * from usuario where id_user = {id};")[0]
            dados = [dado for dado in dados]
            dados.pop(0)
            return dados[0], dados[1], dados[2], dados[3], dados[4], dados[5]
        except:
            pass

    def update_user(self):
        banco = Banco()

        try:
            cursor = banco.get_banco.cursor()

        except:
            pass


user = Usuario('macelo.matos@e-deploy.com.br', '784512@Ma', 0,0,0,0)
# user.inserir_usuario()
banco = Banco()
cursor = banco.get_banco.cursor()

# select = list(cursor.execute("select COUNT(ID_user) from usuario;"))[0][0]

email, senha, x, y, x2, y2 = Usuario.select_user(id=2)

print(email, senha, x, y, x2, y2)