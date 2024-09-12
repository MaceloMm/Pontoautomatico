# _*_ coding: utf-8 _*_
import time
import tkinter as tk
from ttkbootstrap import Style
import Functions
from Usuarios import User
from Functions import cadastro


class Application(tk.Tk):

    def __init__(self, master=None):
        super().__init__()
        self.title('Ponto Automatico')
        self.configure()
        self.geometry("400x300")
        self.attributes("-topmost", True)

        icone = tk.PhotoImage(file="imagens\\check.png")
        self.iconphoto(False, icone)

        self.current_frame = None

        self.show_frame(FirstScreen)

        style = Style(theme='cyborg')

    def show_frame(self, frame_class):
        if self.current_frame is not None:
            self.current_frame.destroy()
        self.current_frame = frame_class(self)
        self.current_frame.place(relx=0.5, rely=0.5, anchor='center')

    def acabar(self):
        self.destroy()

    def user_validation(self, info):
        existe = User.validation
        if existe:
            self.show_frame(Iniciar)
        else:
            info.config(text='Não existe usuario cadastrado!', fg='red')


class FirstScreen(tk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.configure()

        font = tk.font.Font(weight='bold', size=15)
        font2 = tk.font.Font(weight='bold', size=8)

        label = tk.Label(self, text='Escolha uma das opções:', font=font, )
        label.grid(column=0, row=0, pady=15, columnspan=2)

        label_info = tk.Label(self, text='', font=font2)
        label_info.grid(column=0, row=2, pady=10, columnspan=2)

        buttom_cadastro = tk.Button(self, text='Cadastro', command=lambda: master.show_frame(Cadastro),
                                    width=13, height=2, font=font2)
        buttom_cadastro.grid(column=0, row=1, pady=15)

        buttom_iniciar = tk.Button(self, text='Iniciar', width=13, height=2, font=font2,
                                   command= lambda: master.user_validation(label_info))
        buttom_iniciar.grid(column=1, row=1, pady=15)

        # Ajuste a proporção das colunas para expandir conforme necessário
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        # Ajuste a proporção das linhas para expandir conforme necessário
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)


class Cadastro(tk.Frame):

    def __init__(self, master):
        super().__init__(master=master)

        font = tk.font.Font(weight='bold', size=13)
        font2 = tk.font.Font(weight='bold', size=10)

        label = tk.Label(self, text='Preencha as informações:', font=font)
        label.grid(column=0, row=0, pady=15, columnspan=2, sticky='w')

        label_informacao = tk.Label(self, text='', font=font2)
        label_informacao.grid(column=0, row=4, pady=15, columnspan=2, sticky='ew')

        label_email = tk.Label(self, text='Email:', font=font2)
        label_email.grid(column=0, row=1, sticky='w', padx=5)
        label_senha = tk.Label(self, text='Senha:', font=font2)
        label_senha.grid(column=0, row=2, pady=10, sticky='w', padx=5)

        email = tk.Entry(self, width=35)
        email.grid(column=1, row=1, sticky='w')
        senha = tk.Entry(self, show='*', width=35)
        senha.grid(column=1, row=2, pady=10, sticky='w')

        enviar = tk.Button(self, command=lambda: Cadastro.acabar(master, email, senha, label_informacao),
                           text='Enviar', width=10, height=1, font=font2)
        enviar.grid(column=0, row=3, padx=5, pady=12, sticky='e')

        voltar = tk.Button(self, command=lambda: master.show_frame(FirstScreen), text='Voltar', width=10, height=1,
                           font=font2)
        voltar.grid(column=1, row=3, padx=5, pady=12, columnspan=1, sticky='w')

        # Ajuste a proporção das colunas para expandir conforme necessário
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        # Ajuste a proporção das linhas para expandir conforme necessário
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)

    @staticmethod
    def acabar(master, dado1, dado2, info):
        email = dado1.get()
        senha = dado2.get()
        if email == '' and senha == '':
            info.config(text='Os campos não foram preenchidos!', fg='red')
        else:
            msg = Functions.cadastro(email=email, senha=senha)
            info.config(text=msg, fg='green')


class Iniciar(tk.Frame):

    def __init__(self, master):
        super().__init__(master)

        texto_teste = tk.Label(self, text='Estou funcionando')
        texto_teste.grid(column=0, row=0, pady=15, columnspan=2, sticky='ew')

        voltar = tk.Button(self, command=lambda: master.show_frame(FirstScreen), text='Voltar', width=10, height=1)
        voltar.grid(column=1, row=3, padx=5, pady=12, columnspan=1, sticky='w')


if __name__ == '__main__':
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