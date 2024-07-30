import sqlite3

class Banco:

    def __init__(self):
        self.__conexao = sqlite3.connect('banco_coodernadas.db')
        self.create_table()

    def create_table(self):
        cursor = self.__conexao.cursor()

        cursor.execute("""
            create TABLE if not exists usuario (
            ID_user integer primary key autoincrement,
            email text,
            senha text,
            x integer,
            y integer,
            x_2 integer,
            y_2 integer)
        """)

        self.__conexao.commit()
        cursor.close()

    @property
    def get_banco(self):
        return self.__conexao