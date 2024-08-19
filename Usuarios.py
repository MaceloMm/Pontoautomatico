# _*_ coding: utf-8 _*_

from Banco import Banco


class User:

    def __init__(self, email, password, coordernada_x, coordenada_y, coordenada_x_2, coordenada_y_2, __id__=0):
        self.__id = __id__
        self.__email = email
        self.__senha = password
        self.__coord_x = coordernada_x
        self.__coord_y = coordenada_y
        self.__coord_x_2 = coordenada_x_2
        self.__coord_y_2 = coordenada_y_2

    @property
    def validation(self):
        __banco__ = Banco()

        try:
            __cursor__ = __banco__.get_banco.cursor()
            cadastros = int(list(__cursor__.execute("select count(id_user) from usuario"))[0][0])
        except:
            pass
        else:
            if cadastros != 0:
                return True
            elif cadastros <= 0:
                return False

    def insert_user(self):

        __banco__ = Banco()

        validador = User.validation

        if validador:
            return 'Usuario já cadastrado!'
        else:
            try:

                __cursor__ = __banco__.get_banco.cursor()

                __cursor__.execute("""insert into usuario (email, senha, x, y, x_2, y_2) values ('{}', '{}', '{}', '{}', '{}',
                '{}')""".format(self.__email, self.__senha, self.__coord_x, self.__coord_y, self.__coord_x_2, self.__coord_y_2))

                __banco__.get_banco.commit()
                __banco__.get_banco.close()

                return "Cadastro realizado com sucesso"
            except:
                return "Aconteceu algum erro no cadastro"

    @staticmethod
    def delete_user():
        __banco__ = Banco()

        validador = User.validation

        if validador:
            try:
                __cursor__ = __banco__.get_banco.cursor()
                __cursor__.execute(f"""delete from usuario where id = {1};""")
                __banco__.get_banco.commit()
                __banco__.get_banco.close()
            except:
                return 'Ocorreu um erro ao apagar o usuario!'
        else:
            return 'Nenhum Usuario cadastrado!'

    @staticmethod
    def select_user():
        __banco__ = Banco()

        try:
            __cursor__ = __banco__.get_banco.cursor()
            quant_users = list(__cursor__.execute(f"select count(id_user) from usuario"))[0]
            __banco__.get_banco.close()
            if quant_users == 0:
                return 'Nenhum dado cadastrado!'
            elif quant_users == 1:
                dados = list(__cursor__.execute(f"select * from usuario"))[0]
                dados = [dado for dado in dados]
                dados.pop(0)
                return dados[0], dados[1], dados[2], dados[3], dados[4], dados[5]
            """
            else:
                try:
                    credetials = list(__cursor__.execute("select id_user from usuario"))
                except (ValueError, TypeError) as err:
                    print('ID invalido!')
                else:
                    for credetial in credetials:
                        if credetial == __id__:
                            id_filtrado = __id__
                            if id_filtrado != None:
                                dados = __cursor__.execute(f"select * from usuario where id_user = {id_filtrado};")[0]
                                dados = [dado for dado in dados]
                                dados.pop(0)
                                return dados[0], dados[1], dados[2], dados[3], dados[4], dados[5]
                            else:
                                pass
                        else:
                            pass
            """
        except:
            return 'Ocorreu um erro ao procurar o usuario!'

    @staticmethod
    def update_user(email, password, x, y, x2, y2):
        __banco__ = Banco()

        try:
            __cursor__ = __banco__.get_banco.cursor()
            __cursor__.execute("""
            UPDATE usuario SET (email, senha, x, y, x_2, y_2) = ({}, {}, {}, {}, {}, {});
            """.format(email, password, x, y, x2, y2))
            __banco__.get_banco.commit()
            __banco__.get_banco.close()
            return 'Alteração realizada com Sucesso!'

        except:
            pass


# user = Usuario('macelo.matos@e-deploy.com.br', '784512@Ma', 0,0,0,0)
# user.insert_user()


# select = list(cursor.execute("select COUNT(ID_user) from usuario;"))[0][0]

# email, senha, x, y, x2, y2 = Usuario.select_user(id=1)

# print(email, senha, x, y, x2, y2)

# teste
