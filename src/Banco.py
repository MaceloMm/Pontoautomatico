# _*_ coding: utf-8 _*_

import sqlite3


class Banco:

    def __init__(self):
        self.__conexao = sqlite3.connect('src/cadastros.db')
        self.create_table()

    def create_table(self):
        cursor = self.__conexao.cursor()

        cursor.execute("""
            create TABLE if not exists usuario (
            id integer primary key autoincrement,
            email text,
            senha text)
        """)

        cursor.execute('PRAGMA foreign_keys = ON')

        cursor.execute("""
            CREATE TABLE if not exists horarios (
            id integer primary key autoincrement,
            horario1 text,
            horario2 text,
            horario3 text,
            horario4 text,
            user_id integer,
            FOREIGN KEY (user_id) REFERENCES usuario(id)
            ON DELETE CASCADE
            ON UPDATE NO ACTION
            )
        """)

        self.__conexao.commit()
        cursor.close()

    @property
    def get_banco(self):
        return self.__conexao


if __name__ == '__main__':
    banco = Banco()
