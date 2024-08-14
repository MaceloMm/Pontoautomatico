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

    @property
    def validation(self):
        banco = Banco()

        try:
            cursor = banco.get_banco.cursor()
            cadastros = int(list(cursor.execute("select count(id_user) from usuario"))[0][0])
        except:
            pass
        else:
            if cadastros != 0:
                return True
            elif cadastros <= 0:
                return False

    def insert_user(self):

        banco = Banco()

        validador = Usuario.validation

        if validador:
            return 'Usuario já cadastrado!'
        else:
            try:

                cursor = banco.get_banco.cursor()

                cursor.execute("""insert into usuario (email, senha, x, y, x_2, y_2) values ('{}', '{}', '{}', '{}', '{}',
                '{}')""".format(self.__email, self.__senha, self.__coord_x, self.__coord_y, self.__coord_x_2, self.__coord_y_2))

                banco.get_banco.commit()
                cursor.close()

                return "Cadastro realizado com sucesso"
            except:
                return "Aconteceu algum erro no cadastro"


    @staticmethod
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

    @staticmethod
    def select_user(self, id):
        banco = Banco()

        try:
            cursor = banco.get_banco.cursor()
            quant_users = list(cursor.execute(f"select count(id_user) from usuario"))[0]
            if quant_users == 0:
                return 'Nenhum dado cadastrado!'
            elif quant_users == 1:
                dados = list(cursor.execute(f"select * from usuario"))[0]
                dados = [dado for dado in dados]
                dados.pop(0)
                return dados[0], dados[1], dados[2], dados[3], dados[4], dados[5]
            else:
                try:
                    id = int(input('Digite o id: '))
                except (ValueError, TypeError) as err:
                    print('ID invalido!')
                else:
                    dados = cursor.execute(f"select * from usuario where id_user = {id};")[0]
                    dados = [dado for dado in dados]
                    dados.pop(0)
                    return dados[0], dados[1], dados[2], dados[3], dados[4], dados[5]
        except:
            return 'Ocorreu um erro ao procurar o usuario!'


    @staticmethod
    def update_user(self, email, senha, x, y, x2, y2):
        banco = Banco()

        try:
            cursor = banco.get_banco.cursor()


        except:
            pass


# user = Usuario('macelo.matos@e-deploy.com.br', '784512@Ma', 0,0,0,0)
# user.insert_user()
banco = Banco()
cursor = banco.get_banco.cursor()

# select = list(cursor.execute("select COUNT(ID_user) from usuario;"))[0][0]

# email, senha, x, y, x2, y2 = Usuario.select_user(id=1)

# print(email, senha, x, y, x2, y2)

# teste
