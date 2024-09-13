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

    @staticmethod
    def validation():
        __banco__ = Banco()

        try:
            __cursor__ = __banco__.get_banco.cursor()
            cadastros = int(list(__cursor__.execute("select count(id_user) from usuario"))[0][0])
        except:
            print('dei um erro')
        else:
            if cadastros != 0:
                return True
            elif cadastros <= 0:
                return False

    def insert_user(self):

        __banco__ = Banco()

        validador = User.validation()

        if validador:
            return 'Usuario já cadastrado!'
        else:
            try:

                __cursor__ = __banco__.get_banco.cursor()

                __cursor__.execute("""insert into usuario (email, senha, x, y, x_2, y_2) values 
                ('{}', '{}', '{}', '{}', '{}','{}')""".format
                                   (self.__email, self.__senha, self.__coord_x, self.__coord_y,
                                    self.__coord_x_2, self.__coord_y_2))

                __banco__.get_banco.commit()
                __banco__.get_banco.close()

                return "Cadastro realizado com sucesso"
            except:
                return "Aconteceu algum erro no cadastro"

    @staticmethod
    def delete_user():
        __banco__ = Banco()

        validador = User.validation()

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
            return 'Erro ao alterar o usuário!'

    def user_consult(self):
        print(self.__email, self.__senha, self.__coord_x, self.__coord_y, self.__coord_x_2, self.__coord_y_2)


class Horario:
    def __init__(self, h1=None, h2=None, h3=None, h4=None):
        self.__horarios = [h1, h2, h3, h4]

    def quant_horarios(self):
        quant = [horario for horario in self.__horarios if horario != None]
        return len(quant)

    def insert_horarios(self):
        __banco__ = Banco()
        quant_hor = self.quant_horarios()

        # try:
        __cursor__ = __banco__.get_banco.cursor()
        if quant_hor >= 1:
            if quant_hor == 2:
                __cursor__.execute("""
                INSERT into horarios (horario1, horario2) values ({}, {})
                """.format(self.__horarios[0], self.__horarios[1]))
                __banco__.get_banco.commit()
                __banco__.get_banco.close()
                return f'Cadastrado os {quant_hor} horarios'
            elif quant_hor == 3:
                __cursor__.execute("""
                INSERT into horarios (horario1, horario2, horario3) values ({}, {}, {})
                """.format(self.__horarios[0], self.__horarios[1], self.__horarios[2]))
                __banco__.get_banco.commit()
                __banco__.get_banco.close()
                return f'Cadastrado os {quant_hor} horarios'
            elif quant_hor == 4:
                __cursor__.execute("""
                INSERT into horarios (horario1, horario2, horario3, horario4) values 
                (?, ?, ?, ?);
                """, (self.__horarios[0], self.__horarios[1], self.__horarios[2], self.__horarios[3]))
                __banco__.get_banco.commit()
                __banco__.get_banco.close()
                return f'Cadastrado os {quant_hor} horarios'
        else:
            return 'Precisa cadastrar mais que um horario'
        # except:
            # return 'Ocorreu um erro ao cadastrar os horarios'



if __name__ == '__main__':
    # macelo = User('macelo.matos@e-deploy.com.br', '784512@Ma', 641, 628, 952, 697)
    # macelo.insert_user()
    horario = Horario('12:00', '18:00', '19:00', '21:00')
    msg = horario.insert_horarios()
    print(msg)

# user = Usuario('macelo.matos@e-deploy.com.br', '784512@Ma', 0,0,0,0)
# user.insert_user()
# select = list(cursor.execute("select COUNT(ID_user) from usuario;"))[0][0]

