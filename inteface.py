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
        self.geometry("600x450")
        self.attributes("-topmost", True)

        icone = tk.PhotoImage(file="imagens\\check.png")
        self.iconphoto(False, icone)

        self.current_frame = None

        self.show_frame(FirstScreen)

        # style = Style(theme='vapor')
        style = Style(theme='cyborg')

        texto_principal = tk.Label(self, text='Teste')
        texto_principal.place(relx=0.1, rely=0.1, anchor='ne')

    def show_frame(self, frame_class):
        if self.current_frame is not None:
            self.current_frame.destroy()
        self.current_frame = frame_class(self)
        self.current_frame.place(relx=0.5, rely=0.5, anchor='center')

    def acabar(self):
        self.destroy()

    def user_validation(self, info):
        # existe = User.validation
        existe = True
        if existe:
            self.show_frame(Iniciar)
        else:
            info.config(text='Não existe usuario cadastrado!', fg='red')


class FirstScreen(tk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.configure()

        font = tk.font.Font(weight='bold', size=13)
        font2 = tk.font.Font(weight='bold', size=10)

        label = tk.Label(self, text='Escolha uma das opções:', font=font, )
        label.grid(column=0, row=0, columnspan=1, pady=8, sticky='e')

        label_info = tk.Label(self, text='', font=font2)
        label_info.grid(column=0, row=2, pady=10, columnspan=1)

        buttom_cadastro = tk.Button(self, text='Cadastro usuario', command=lambda: master.show_frame(Cadastro),
                                    width=20, height=2, font=font2)
        buttom_cadastro.grid(column=0, row=2, pady=6)

        buttom_iniciar = tk.Button(self, text='Iniciar o programa', width=20, height=2, font=font2,
                                   command= lambda: master.user_validation(label_info))
        buttom_iniciar.grid(column=0, row=1, pady=6)

        buttom_horarios = tk.Button(self, text='Cadastro de horarios',
                                    command=lambda: master.show_frame(Horarios), width=20, height=2, font=font2)
        buttom_horarios.grid(column=0, row=3, pady=6)

        # Ajuste a proporção das colunas para expandir conforme necessário
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        # Ajuste a proporção das linhas para expandir conforme necessário
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)


class Cadastro(tk.Frame):

    def __init__(self, master):
        super().__init__(master)

        font = tk.font.Font(weight='bold', size=13)
        font2 = tk.font.Font(weight='bold', size=10)

        label_option = tk.Label(self, text='Escolha uma das opções abaixo:', font=font)
        label_option.grid(column=0, row=0, columnspan=1, sticky='e', pady=12)

        button_cadastro = tk.Button(self, text='Cadastro', width=14, height=2, font=font2)
        button_cadastro.grid(column=0, row=1, pady=6)

        button_alterar = tk.Button(self, text='Alterar', width=14, height=2, font=font2)
        button_alterar.grid(column=0, row=2, pady=6)

        button_deletar = tk.Button(self, text='Deletar', width=14, height=2, font=font2)
        button_deletar.grid(column=0, row=3, pady=6)

        button_voltar = tk.Button(self, text='Voltar', width=14, height=2, font=font2,
                                  command=lambda: master.show_frame(FirstScreen))
        button_voltar.grid(column=0, row=4, pady=6)


class CadastroUser(tk.Frame):

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

        font2 = tk.font.Font(weight='bold', size=10)

        texto_teste = tk.Label(self, text='Estou funcionando', font=10)
        texto_teste.grid(column=0, row=0, pady=0, columnspan=2, sticky='w')

        button_horarios = tk.Button(self, text='Horarios salvos', width=12, height=2,
                                    font=font2)
        button_horarios.grid(column=0, row=1, pady=10, padx=5, sticky='we', columnspan=2)

        button_horariosp = tk.Button(self, text='Definir horario', width=12, height=2,
                                    font=font2)
        button_horariosp.grid(column=0, row=2, pady=6, padx=5, sticky='we', columnspan=2)

        voltar = tk.Button(self, command=lambda: master.show_frame(FirstScreen), text='Voltar', width=10, height=2,
                           font=font2)
        voltar.grid(column=0, row=5, padx=5, pady=6, columnspan=2, sticky='we')

        # Ajuste a proporção das colunas para expandir conforme necessário
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        # Ajuste a proporção das linhas para expandir conforme necessário
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)


class Horarios(tk.Frame):

    def __init__(self, master):
        super().__init__(master)

        font = tk.font.Font(weight='bold', size=13)
        font2 = tk.font.Font(weight='bold', size=10)

        label_option = tk.Label(self, text='Escolha uma das opções abaixo:', font=font)
        label_option.grid(column=0, row=0, columnspan=1, sticky='e', pady=12)

        button_cadastro = tk.Button(self, text='Cadastro', width=14, height=2, font=font2)
        button_cadastro.grid(column=0, row=1, pady=6)

        button_alterar = tk.Button(self, text='Alterar', width=14, height=2, font=font2)
        button_alterar.grid(column=0, row=2, pady=6)

        button_deletar = tk.Button(self, text='Deletar', width=14, height=2, font=font2)
        button_deletar.grid(column=0, row=3, pady=6)

        button_voltar = tk.Button(self, text='Voltar', width=14, height=2, font=font2,
                                  command=lambda: master.show_frame(FirstScreen))
        button_voltar.grid(column=0, row=4, pady=6)


if __name__ == '__main__':
    root = Application()
    root.mainloop()

