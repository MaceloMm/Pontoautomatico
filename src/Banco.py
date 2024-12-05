# _*_ coding: utf-8 _*_

import sqlite3
import os, sys


def get_resource_path(relative_path):
    """Retorna o caminho correto do arquivo, dentro ou fora do executável."""
    base_path = getattr(sys, '_MEIPASS', os.path.abspath("."))
    return os.path.join(base_path, relative_path)


class Banco:

    def __init__(self):
        db_path = get_resource_path(r'src\cadastros.db')
        self.__conexao = sqlite3.connect(db_path)
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
