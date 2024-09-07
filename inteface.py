# _*_ coding: utf-8 _*_
import time
import tkinter as tk
from ttkbootstrap import Style
import PySimpleGUI as sg


import Functions
from Usuarios import User
from Functions import cadastro


fundo = 'lightblue'


class Application(tk.Tk):

    def __init__(self, master=None):
        super().__init__()
        self.title('Ponto Automatico')
        self.configure(bg=fundo)
        self.geometry("400x300")

        self.current_frame = None

        self.show_frame(FirstScreen)

        style = Style(theme='cyborg')

    def show_frame(self, frame_class):
        if self.current_frame is not None:
            self.current_frame.destroy()
        self.current_frame = frame_class(self)
        self.current_frame.place(relx=0.5, rely=0.5, anchor='center')

class FirstScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(bg=fundo)

        font = tk.font.Font(weight='bold', size=15)
        font2 = tk.font.Font(weight='bold', size=8)

        label = tk.Label(self, text='Escolha uma das opções:', bg=fundo, font=font, )
        label.grid(column=0, row=0, pady=15, columnspan=2)

        buttom_cadastro = tk.Button(self, text='Cadastro', command=Functions.cadastro, width=13, height=2, font=font2)
        buttom_cadastro.grid(column=0, row=1, pady=15)

        buttom_iniciar = tk.Button(self, text='Iniciar', width=13, height=2, font=font2)
        buttom_iniciar.grid(column=1, row=1, pady=15)


        # Ajuste a proporção das colunas para expandir conforme necessário
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        # Ajuste a proporção das linhas para expandir conforme necessário
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

root = Application()
root.mainloop()

"""
def testando_texto():
    text = label.get()
    print(text)
    return text

root = tk.Tk()
root.title('Teste')
label = tk.Entry(root)
label.pack(pady=10)
label2 = tk.Button(root, text='clique aqui', command=testando_texto)
label2.pack(pady=10)

text = testando_texto()
print(text)

root.mainloop()
"""
"""
layout = [
    [sg.Text('Ponto Automatico', font=30)],
    [sg.Button('Iniciar'), sg.Button('Cadastro')],
    [sg.Text('Não iniciado!', key='mudanca')]
]

janela = sg.Window('Testando', layout)

while True:
    eventos, valores = janela.read()

    if eventos == 'Cadastro':
        janela['mudanca'].update('Rodando...')
        Functions.cadastro()

    if eventos == sg.WIN_CLOSED:
        break

janela.close()
"""