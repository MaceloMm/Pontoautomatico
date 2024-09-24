# _*_ coding: utf-8 _*_
import time
import tkinter as tk
from ttkbootstrap import Style
import Functions
from Usuarios import User
from Usuarios import SchedulesMm


class Application(tk.Tk):

    def __init__(self, master=None):
        super().__init__()
        self.title('Ponto Automatico')
        self.configure()
        self.geometry("600x450")
        self.attributes("-topmost", True)

        icone = tk.PhotoImage(file="imagens\\check.png")
        self.iconphoto(False, icone)

        font_principal = tk.font.Font(size=15, weight='bold')

        principal_text = tk.Label(self, text='Ponto Automatico', font=font_principal)
        principal_text.place(x=25, y=25, anchor='nw')

        self.info = principal_text

        self.current_frame = None

        self.show_frame(FirstScreen)

        # style = Style(theme='vapor')
        style = Style(theme='cyborg')

        dev = tk.Label(self, text='Desenvolvido por Macelo')
        dev.place(x=575, y=430, anchor='se')

    def show_frame(self, frame_class, name='Ponto Automatico'):
        if self.current_frame is not None:
            self.current_frame.destroy()
        self.current_frame = frame_class(self)
        self.current_frame.place(relx=0.5, rely=0.5, anchor='center')
        self.info.config(text=name)

    def user_validation(self, info):
        exists = User.validation()
        if exists:
            self.show_frame(StartScript)
        else:
            info.config(text='Não existe usuario cadastrado!', fg='red')


# Primeira tela
class FirstScreen(tk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.configure()

        font = tk.font.Font(weight='bold', size=11)
        font2 = tk.font.Font(weight='bold', size=10)

        label = tk.Label(self, text='Escolha uma das opções:', font=font, )
        label.grid(column=0, row=0, columnspan=1, pady=8, sticky='e')

        label_info = tk.Label(self, text='', font=font2)
        label_info.grid(column=0, row=4, pady=10, columnspan=1)

        buttom_cadastro = tk.Button(self, text='Cadastro usuario',
                                    command=lambda: master.show_frame(UserInterface, 'Cadastro de Usuario'),
                                    width=20, height=2, font=font2)
        buttom_cadastro.grid(column=0, row=2, pady=6)

        buttom_iniciar = tk.Button(self, text='Iniciar o programa', width=20, height=2, font=font2,
                                   command=lambda: master.user_validation(label_info))
        buttom_iniciar.grid(column=0, row=1, pady=6)

        buttom_horarios = tk.Button(self, text='Cadastro de horarios',
                                    command=lambda: master.show_frame(SchedulesInterface, 'Cadastro de Horarios')
                                    , width=20, height=2, font=font2)
        buttom_horarios.grid(column=0, row=3, pady=6)

        # Ajuste a proporção das colunas para expandir conforme necessário
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        # Ajuste a proporção das linhas para expandir conforme necessário
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)


# Tela das opções de cadastro de usuario
class UserInterface(tk.Frame):

    def __init__(self, master):
        super().__init__(master)

        font = tk.font.Font(weight='bold', size=11)
        font2 = tk.font.Font(weight='bold', size=10)

        label_option = tk.Label(self, text='Escolha uma das opções abaixo:', font=font)
        label_option.grid(column=0, row=0, columnspan=1, sticky='we', pady=12)

        label_info = tk.Label(self, text='', font=font)
        label_info.grid(column=0, row=5, pady=13)

        button_cadastro = tk.Button(self, text='Cadastro', width=14, height=2, font=font2,
                                    command=lambda: UserInterface.validacao_cadastro(master, label_info))
        button_cadastro.grid(column=0, row=1, pady=6)

        button_alterar = tk.Button(self, text='Alterar', width=14, height=2, font=font2,
                                   command=lambda: master.show_frame(ChangeUser))
        button_alterar.grid(column=0, row=2, pady=6)

        button_deletar = tk.Button(self, text='Deletar', width=14, height=2, font=font2,
                                   command=lambda: UserInterface.deletar_user(label_info))
        button_deletar.grid(column=0, row=3, pady=6)

        button_voltar = tk.Button(self, text='Voltar', width=14, height=2, font=font2,
                                  command=lambda: master.show_frame(FirstScreen))
        button_voltar.grid(column=0, row=4, pady=6)

    @staticmethod
    def deletar_user(info):
        x = User.validation()
        if x:
            msg = User.delete_user()
            info.config(text=msg, fg='green')
        else:
            info.config(text='Não existe usuario cadastrado!', fg='red')

    @staticmethod
    def validacao_cadastro(master, info):
        cadastro = User.validation()
        if cadastro is not True:
            master.show_frame(RegistrationUser)
        else:
            info.config(text='Já existe um usuario cadastrado', fg='orange')


# Tela cadastro User
class RegistrationUser(tk.Frame):

    def __init__(self, master):
        super().__init__(master=master)

        font = tk.font.Font(weight='bold', size=11)
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

        enviar = tk.Button(self, command=lambda: RegistrationUser.acabar(email, senha, label_informacao),
                           text='Enviar', width=10, height=1, font=font2)
        enviar.grid(column=0, row=3, padx=5, pady=12, sticky='e')

        voltar = tk.Button(self, command=lambda: master.show_frame(UserInterface, 'Cadastro de Usuario'),
                           text='Voltar', width=10, height=1, font=font2)
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
    def acabar(dado1, dado2, info):
        email = dado1.get()
        senha = dado2.get()
        if email == '' and senha == '':
            info.config(text='Os campos não foram preenchidos!', fg='red')
        else:
            msg = Functions.registration_user(email=email, senha=senha)
            info.config(text=msg, fg='green')


# Tela para alterar o cadastro do usuario - Pedente
class ChangeUser(tk.Frame):

    def __init__(self, master):
        super().__init__(master)

        font = tk.font.Font(weight='bold', size=11)
        font2 = tk.font.Font(weight='bold', size=10)

        label_teste = tk.Label(self, text='Preencha os dados:')
        label_teste.grid(column=0, row=0, pady=15, columnspan=2, sticky='w')

        voltar = tk.Button(self, command=lambda: master.show_frame(UserInterface, 'Cadastro de Usuario'),
                           text='Voltar', width=10, height=1, font=font2)
        voltar.grid(column=1, row=3, padx=5, pady=12, columnspan=1, sticky='w')


# Tela com as opções de inicio
class StartScript(tk.Frame):

    def __init__(self, master):
        super().__init__(master)

        font = tk.font.Font(weight='bold', size=11)
        font2 = tk.font.Font(weight='bold', size=10)

        texto_teste = tk.Label(self, text='Escolha uma opção:', font=font)
        texto_teste.grid(column=0, row=0, pady=0, columnspan=2, sticky='w')

        info = tk.Label(self, text='', font=10)
        info.grid(column=0, row=6, pady=6, sticky='we', columnspan=2)

        button_horarios = tk.Button(self, text='Horarios salvos', width=12, height=2, font=font2,
                                    command=lambda: StartScript.horarios_salvos(info))
        button_horarios.grid(column=0, row=1, pady=10, padx=5, sticky='we', columnspan=2)

        button_horariosp = tk.Button(self, text='Definir horario', width=12, height=2, font=font2,
                                     command=lambda: master.show_frame(StartNoTimesSaved))
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

    @staticmethod
    def horarios_salvos(info):
        validation = SchedulesMm.validation_horarios()
        if validation:
            info.config(text='Estou rodando', fg='green')
            info.update()
            msg = Functions.__start_loop__(utilizar=True)
            info.config(text=msg, fg='white')
        else:
            info.config('Não tem horarios salvos cadastrados')


class StartNoTimesSaved(tk.Frame):

    def __init__(self, master):
        super().__init__(master)

        font = tk.font.Font(weight='bold', size=11)
        font2 = tk.font.Font(weight='bold', size=10)

        label_principal = tk.Label(self, text='Coloque os horarios no formato 00:00:', font=font)
        label_principal.grid(column=0, row=0, pady=12, columnspan=2)

        label_info = tk.Label(self, text='', font=font2)
        label_info.grid(column=0, row=7, pady=12, columnspan=2)

        label_time1 = tk.Label(self, text='1º Horario:', font=font2)
        label_time1.grid(column=0, row=1, padx=3, pady=8, sticky='w')

        eh1 = tk.Entry(self)
        eh1.grid(column=1, row=1, sticky='we', pady=8)

        label_time2 = tk.Label(self, text='2° Horario:', font=font2)
        label_time2.grid(column=0, row=2, padx=3, pady=8, sticky='w')

        eh2 = tk.Entry(self)
        eh2.grid(column=1, row=2, sticky='we', pady=8)

        label_time3 = tk.Label(self, text='3° Horario:', font=font2)
        label_time3.grid(column=0, row=3, padx=3, pady=8, sticky='w')

        eh3 = tk.Entry(self)
        eh3.grid(column=1, row=3, sticky='we', pady=8)

        label_time4 = tk.Label(self, text='4° Horario:', font=font2)
        label_time4.grid(column=0, row=4, padx=3, pady=8, sticky='w')

        eh4 = tk.Entry(self)
        eh4.grid(column=1, row=4, sticky='we', pady=8)

        var = tk.IntVar()

        chackbox = tk.Checkbutton(self, text='Bloquear no final', variable=var)
        chackbox.grid(column=0, row=5)

        button_cadastrar = tk.Button(self, text='Iniciar', width=15, height=1, font=font2,
                                     command=lambda: StartNoTimesSaved.initial_times(
                                         eh1, eh2, eh3, eh4, label_info, master, var
                                     ))
        button_cadastrar.grid(column=0, row=6, sticky='w', pady=15)

        button_voltar = tk.Button(self, text='Voltar', width=15, height=1, font=font2,
                                  command=lambda: master.show_frame(StartScript))
        button_voltar.grid(column=1, row=6, sticky='w', pady=15)

    @staticmethod
    def initial_times(h1, h2, h3, h4, info, master, var):
        hors = [h1.get(), h2.get(), h3.get(), h4.get()]
        list_hors = [horario for horario in hors if horario != '']
        format_validation = [Functions.format_schedules(hora) for hora in list_hors]
        if all(format_validation):
            if len(list_hors) <= 1:
                info.config(text='Por favor insira pelo o menos 2 horarios', fg='red')
            else:
                info.config(text='Estou rodando', fg='green')
                info.update()
                msg = Functions.__start_loop__(utilizar=False, __times__=list_hors, block=var)
                info.config(text=msg, fg='white')
                time.sleep(2)
                master.show_frame(StartScript)
        else:
            info.config(text='Horaios não estão no formado 00:00', fg='red')


# Tela das opções de cadastro de Horario
class SchedulesInterface(tk.Frame):

    def __init__(self, master):
        super().__init__(master)

        font = tk.font.Font(weight='bold', size=11)
        font2 = tk.font.Font(weight='bold', size=10)

        label_option = tk.Label(self, text='Escolha uma das opções abaixo:', font=font)
        label_option.grid(column=0, row=0, columnspan=1, sticky='e', pady=12)

        info = tk.Label(self, text='', font=font)
        info.grid(column=0, row=5, pady=10)

        button_cadastro = tk.Button(self, text='Cadastro', width=14, height=2, font=font2,
                                    command=lambda: master.show_frame(SchedulesRegistration))
        button_cadastro.grid(column=0, row=1, pady=6)

        button_alterar = tk.Button(self, text='Alterar', width=14, height=2, font=font2)
        button_alterar.grid(column=0, row=2, pady=6)

        button_deletar = tk.Button(self, text='Deletar', width=14, height=2, font=font2,
                                   command=lambda: SchedulesInterface.delete_hor(info))
        button_deletar.grid(column=0, row=3, pady=6)

        button_voltar = tk.Button(self, text='Voltar', width=14, height=2, font=font2,
                                  command=lambda: master.show_frame(FirstScreen))
        button_voltar.grid(column=0, row=4, pady=6)

    @staticmethod
    def delete_hor(info):
        msg = SchedulesMm.delete_horarios()
        info.config(text=msg, fg='green')


# Tela cadastro User
class SchedulesRegistration(tk.Frame):

    def __init__(self, master):
        super().__init__(master)

        font = tk.font.Font(weight='bold', size=11)
        font2 = tk.font.Font(weight='bold', size=10)

        label_principal = tk.Label(self, text='Coloque os horarios no formato 00:00:', font=font)
        label_principal.grid(column=0, row=0, pady=12, columnspan=2)

        label_info = tk.Label(self, text='', font=font2)
        label_info.grid(column=0, row=6, pady=12, columnspan=2)

        label_horario1 = tk.Label(self, text='1º Horario:', font=font2)
        label_horario1.grid(column=0, row=1, padx=3, pady=8, sticky='w')

        eh1 = tk.Entry(self)
        eh1.grid(column=1, row=1, sticky='we', pady=8)

        label_horario2 = tk.Label(self, text='2° Horario:', font=font2)
        label_horario2.grid(column=0, row=2, padx=3, pady=8, sticky='w')

        eh2 = tk.Entry(self)
        eh2.grid(column=1, row=2, sticky='we', pady=8)

        label_horario3 = tk.Label(self, text='3° Horario:', font=font2)
        label_horario3.grid(column=0, row=3, padx=3, pady=8, sticky='w')

        eh3 = tk.Entry(self)
        eh3.grid(column=1, row=3, sticky='we', pady=8)

        label_horario4 = tk.Label(self, text='4° Horario:', font=font2)
        label_horario4.grid(column=0, row=4, padx=3, pady=8, sticky='w')

        eh4 = tk.Entry(self)
        eh4.grid(column=1, row=4, sticky='we', pady=8)

        button_cadastrar = tk.Button(self, text='Enviar', width=15, height=1, font=font2,
                                     command=lambda: SchedulesRegistration.cadastrar_hors(eh1, eh2, eh3, eh4, label_info,
                                                                                          master))
        button_cadastrar.grid(column=0, row=5, sticky='w', pady=15)

        button_voltar = tk.Button(self, text='Voltar', width=15, height=1, font=font2,
                                  command=lambda: master.show_frame(SchedulesInterface, 'Cadastro de Horario'))
        button_voltar.grid(column=1, row=5, sticky='w', pady=15)

    @staticmethod
    def cadastrar_hors(h1, h2, h3, h4, info, master):
        hors = [h1.get(), h2.get(), h3.get(), h4.get()]
        list_hors = [horario for horario in hors if horario != '']
        format_validation = [Functions.format_schedules(hora) for hora in list_hors]
        if all(format_validation):
            if len(list_hors) <= 1:
                info.config(text='Por favor insira pelo o menos 2 horarios', fg='red')
            else:
                hor = SchedulesMm(list_hors)
                msg = hor.insert_horarios()
                info.config(text=msg, fg='green')
                info.update()
                time.sleep(2)
                master.show_frame(FirstScreen)
        else:
            info.config(text='Horaios não estão no formado 00:00', fg='red')


if __name__ == '__main__':
    root = Application()
    root.mainloop()
