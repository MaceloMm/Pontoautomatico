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
            cadastros = int(list(__cursor__.execute("select count(id) from usuario"))[0][0])
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
                __cursor__.execute("""update sqlite_sequence SET seq = 0 where name = 'usuario';""")
                __banco__.get_banco.commit()
                __banco__.get_banco.close()
            except:
                return 'Ocorreu um erro ao apagar o usuario!'
            else:
                return 'Usuario deletado!'
        else:
            return 'Nenhum Usuario cadastrado!'

    @staticmethod
    def select_user():
        __banco__ = Banco()
        validador = User.validation()

        try:
            __cursor__ = __banco__.get_banco.cursor()
            if validador:
                dados = list(__cursor__.execute(f"SELECT * FROM usuario;"))[0]
                dados = [dado for dado in dados if dado != 1]
                __banco__.get_banco.close()
                return dados[0], dados[1], {'x': dados[2], 'y': dados[3]}, {'x': dados[4], 'y': dados[5]}
            else:
                return 'Nenhum dado cadastrado!'
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


class SchedulesMm:
    def __init__(self, hours):
        self.__horarios = hours

    @staticmethod
    def validation_horarios():
        __banco__ = Banco()

        try:
            __cursor__ = __banco__.get_banco.cursor()
            cadastros = len(list(__cursor__.execute("""select horario1, horario2, horario3, horario4 from horarios 
                                                    where id = 1; """))[0])
        except:
            print('dei um erro')
        else:
            if cadastros != 0:
                return True
            elif cadastros <= 0:
                return False

    def quant_horarios(self):
        quant = [__horario__ for __horario__ in self.__horarios if __horario__ is not None]
        return len(quant)

    def insert_horarios(self):
        __banco__ = Banco()
        quant_hor = self.quant_horarios()
        validacao = self.validation_horarios()

        try:
            __cursor__ = __banco__.get_banco.cursor()
            if validacao:
                return 'Já existe um horario cadastrado'
            else:
                if quant_hor >= 1:
                    if quant_hor == 2:
                        __cursor__.execute("""
                        INSERT into horarios (horario1, horario2) values (?, ?)
                        """, (self.__horarios[0], self.__horarios[1]))
                        __banco__.get_banco.commit()
                        __banco__.get_banco.close()
                        return f'Cadastrado os {quant_hor} horarios'
                    elif quant_hor == 3:
                        __cursor__.execute("""
                        INSERT into horarios (horario1, horario2, horario3) values (?, ?, ?)
                        """, (self.__horarios[0], self.__horarios[1], self.__horarios[2]))
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
        except:
            return 'Ocorreu um erro ao cadastrar os horarios'

    @staticmethod
    def delete_horarios():
        __banco__ = Banco()
        validador = SchedulesMm.validation_horarios()

        try:
            __cursor__ = __banco__.get_banco.cursor()
            if validador:
                __cursor__ = __banco__.get_banco.cursor()
                __cursor__.execute(f"""delete from horarios where id = {1};""")
                __cursor__.execute("""update sqlite_sequence SET seq = 0 where name = 'horarios';""")
                __banco__.get_banco.commit()
                __banco__.get_banco.close()
                return 'Horario deletado com sucesso!'
            else:
                return 'Não existe horario cadastrado'
        except:
            return 'Ocorreu algum erro'

    @staticmethod
    def select_horario():
        __banco__ = Banco()
        validacao = SchedulesMm.validation_horarios()

        try:
            if validacao:
                __cursor__ = __banco__.get_banco.cursor()
                hor_cadastros = list(__cursor__.execute("""
                SELECT horario1, horario2, horario3, horario4 from horarios"""))[0]
                hor_cadastros = [hor for hor in hor_cadastros]
                __banco__.get_banco.close()
                return hor_cadastros
            else:
                return 'Não existe horarios cadastrados!'
        except:
            return 'Ocorreu um erro ao retorna os cadastros'


if __name__ == '__main__':
    pass
    macelo = User('macelo.matos@e-deploy.com.br', '784512@Ma', 641, 628, 952, 697)
    print(macelo.insert_user())
    #email, senha, cord1, cord2 = User.select_user()
    #print(email, senha, cord1, cord2)
    #horario = Horario(['12:00', '18:00', '19:00', '21:00'])
    #print(horario.delete_horarios())
    #print(horario.insert_horarios())
    #print(Horario.select_horario())
    #print(msg)

