# _*_ coding: utf-8 _*_

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common import ElementNotInteractableException
import selenium
import schedule
import time
import pyautogui
import datetime
import keyboard
from tkinter import messagebox
import os

import Usuarios
from Usuarios import User

ultimo_horario = True


def final(funcao):

    def whatsapp():
        time.sleep(2)
        pyautogui.click(x=459, y=1057)
        time.sleep(5)
        pyautogui.click(x=218, y=198)
        time.sleep(1)
        pyautogui.click(x=871, y=1018)
        time.sleep(1)
        pyautogui.write('Bateu o ponto!')
        keyboard.press('enter')
        keyboard.release('enter')

    def brain(__email__, __password__, cords1, cords2, last_time_=None, var=None):
        if last_time_ is not None:
            if time.strftime("%H") == last_time_.split(':')[0]:
                global ultimo_horario
                funcao(__email__, __password__, cords1, cords2)
                time.sleep(4)
                # whatsapp()
                if var == 1:
                    os.system('rundll32.exe user32.dll,LockWorkStation')
                ultimo_horario = False
            else:
                funcao(__email__, __password__, cords1, cords2)
        else:
            funcao(__email__, __password__, cords1, cords2)
    return brain


@final
def bater_ponto(__email__='', __password__='', cords1=None, cords2=None, last_time_=None, var=None):
    cords1 = cords1 or {'x': 0, 'y': 0}
    cords2 = cords2 or {'x': 0, 'y': 0}
    while True:
        try:
            keyboard.press('win')
            keyboard.press('d')
            keyboard.release('win')
            keyboard.release('d')
            time.sleep(2)
            servico = Service(ChromeDriverManager().install())
            navegador = webdriver.Chrome(service=servico)
            navegador.get('https://login.lg.com.br/login/bluke_edeploy')
            time.sleep(3)
            navegador.find_element('xpath', '//*[@id="Login"]').send_keys(__email__)
            navegador.find_element('xpath', '//*[@id="form0"]/div[3]/p/button').click()
            time.sleep(1)
            navegador.find_element('xpath', '//*[@id="Senha"]').send_keys(__password__)
            navegador.find_element('xpath', '//*[@id="form0"]/div[3]').click()
            time.sleep(15)
            try:
                navegador.find_element('xpath',
                                       '//*[@id="app"]/div/section/section/div[1]/div[2]/div/div/div/div[1]/div[1]').click()
            except:
                try:
                    navegador.find_element('xpath',
                                           '//*[@id="app"]/div/section/section/div[1]/div'
                                           '[2]/div/div/div/div[2]/div/div/div/div/div[1]/div/div').click()
                except:
                    pass
        except (ElementNotInteractableException, selenium.common.NoSuchWindowException) as err:
            with open('log.txt', 'a') as arquivo:
                arquivo.write(f'ERROR: Ocorreu um ERRO!\n')
            with open('log_ERRO.txt', 'a') as arquivo:
                arquivo.write(f'ERROR: {err}\n')
        else:
            break
    while True:
        try:
            time.sleep(15)
            pyautogui.click(x=cords1['x'], y=cords1['y'])
            time.sleep(3)
            pyautogui.click(x=cords2['x'], y=cords2['y'])
            time.sleep(5)
            print(f'ponto batido com sucesso')
            with open('log.txt', 'a') as arquivo:
                arquivo.write(f'Ponto batido as {datetime.datetime.today()}\n')
        except pyautogui.FailSafeException:
            pass
        except:
            with open('log_ERRO.txt', 'a') as file:
                file.write('Ocorreu um erro ao bater o ponto')
        else:
            break


def registration_user(email='', senha=''):
    try:
        servico = Service(ChromeDriverManager().install())
        navegador = webdriver.Chrome(service=servico)
        navegador.get('https://login.lg.com.br/login/bluke_edeploy')
        time.sleep(3)
        navegador.find_element('xpath', '//*[@id="Login"]').send_keys(email)
        navegador.find_element('xpath', '//*[@id="form0"]/div[3]/p/button').click()
        time.sleep(1)
        navegador.find_element('xpath', '//*[@id="Senha"]').send_keys(senha)
        navegador.find_element('xpath', '//*[@id="form0"]/div[3]').click()
        time.sleep(10)
    except (ElementNotInteractableException, selenium.common.NoSuchWindowException,
            selenium.common.exceptions.NoSuchWindowException) as err:
        with open('log_ERRO.txt', 'a') as arquivo:
            arquivo.write(f'ERROR: {err}\n')
    else:
        try:
            navegador.find_element('xpath',
                              '//*[@id="app"]/div/section/section/div[1]/div[2]/div/div/div/div[1]/div[1]').click()
        except:
            navegador.find_element('xpath',
                                   '//*[@id="app"]/div/section/section/div[1]/div'
                                   '[2]/div/div/div/div[2]/div/div/div/div/div[1]/div/div').click()
        messagebox.showinfo('Importante!', 'Deixei o mouse em cima de marcar ponto')
        time.sleep(6)
        positions = pyautogui.position()
        messagebox.showinfo('Importante!', 'Agora clique em "Marca ponto" e deixe no botão verde')
        time.sleep(6)
        positions2 = pyautogui.position()
        usuario = User(email, senha, positions[0], positions[1], positions2[0], positions2[1])
        resultado = usuario.insert_user()
        return resultado


def __start_loop__(utilizar=None, __times__=None, block=None):
    # Pensar num jeito de fazer essa birosca que vc invetou funcioanar, cabeça de rola.
    if utilizar:
        email, senha, cord1, cord2 = User.select_user()
        __times__ = Usuarios.SchedulesMm.select_horario()
        __times__ = [h for h in __times__ if h is not None]
        last_time = __times__[len(__times__) - 1]

        if len(__times__) == 2:
            schedule.every().day.at(__times__[0]).do(
                lambda: bater_ponto(__email__=email, __password__=senha, cords1=cord1, cords2=cord2))
            schedule.every().day.at(__times__[1]).do(
                lambda: bater_ponto(__email__=email, __password__=senha, cords1=cord1, cords2=cord2,
                                    last_time_=last_time, var=block))
        elif len(__times__) == 3:
            schedule.every().day.at(__times__[0]).do(
                lambda: bater_ponto(__email__=email, __password__=senha, cords1=cord1, cords2=cord2))
            schedule.every().day.at(__times__[1]).do(
                lambda: bater_ponto(__email__=email, __password__=senha, cords1=cord1, cords2=cord2))
            schedule.every().day.at(__times__[2]).do(
                lambda: bater_ponto(__email__=email, __password__=senha, cords1=cord1, cords2=cord2,
                                    last_time_=last_time, var=block))
        elif len(__times__) == 4:
            schedule.every().day.at(__times__[0]).do(
                lambda: bater_ponto(__email__=email, __password__=senha, cords1=cord1, cords2=cord2))
            schedule.every().day.at(__times__[1]).do(
                lambda: bater_ponto(__email__=email, __password__=senha, cords1=cord1, cords2=cord2))
            schedule.every().day.at(__times__[2]).do(
                lambda: bater_ponto(__email__=email, __password__=senha, cords1=cord1, cords2=cord2))
            schedule.every().day.at(__times__[3]).do(
                lambda: bater_ponto(__email__=email, __password__=senha, cords1=cord1, cords2=cord2,
                                    last_time_=last_time, var=block))
        else:
            return 'Não existe horarios validos cadastrados'
        while ultimo_horario:
            schedule.run_pending()
            time.sleep(1)
        return 'Terminei o dia!'
    else:
        # Programar essa parte depois cabeça de pika
        email, senha, cord1, cord2 = User.select_user()
        __times__ = [h for h in __times__ if h != '']
        last_time = __times__[len(__times__) - 1]
        if len(__times__) == 2:
            schedule.every().day.at(__times__[0]).do(
                lambda: bater_ponto(__email__=email, __password__=senha, cords1=cord1, cords2=cord2))
            schedule.every().day.at(__times__[1]).do(
                lambda: bater_ponto(__email__=email, __password__=senha, cords1=cord1, cords2=cord2,
                                    last_time_=last_time, var=block))
        elif len(__times__) == 3:
            schedule.every().day.at(__times__[0]).do(
                lambda: bater_ponto(__email__=email, __password__=senha, cords1=cord1, cords2=cord2))
            schedule.every().day.at(__times__[1]).do(
                lambda: bater_ponto(__email__=email, __password__=senha, cords1=cord1, cords2=cord2))
            schedule.every().day.at(__times__[2]).do(
                lambda: bater_ponto(__email__=email, __password__=senha, cords1=cord1, cords2=cord2,
                                    last_time_=last_time, var=block))
        elif len(__times__) == 4:
            schedule.every().day.at(__times__[0]).do(
                lambda: bater_ponto(__email__=email, __password__=senha, cords1=cord1, cords2=cord2))
            schedule.every().day.at(__times__[1]).do(
                lambda: bater_ponto(__email__=email, __password__=senha, cords1=cord1, cords2=cord2))
            schedule.every().day.at(__times__[2]).do(
                lambda: bater_ponto(__email__=email, __password__=senha, cords1=cord1, cords2=cord2))
            schedule.every().day.at(__times__[3]).do(
                lambda: bater_ponto(__email__=email, __password__=senha, cords1=cord1, cords2=cord2,
                                    last_time_=last_time, var=block))
        else:
            return 'Não existe horarios validos cadastrados'
        while ultimo_horario:
            schedule.run_pending()
            time.sleep(1)
        return 'Terminei o dia'

def format_schedules(horario):
    try:
        hor_separate = horario.split(':')
    except AttributeError:
        return False
    else:
        if len(hor_separate[0]) == 2 and len(hor_separate[1]) == 2:
            try:
                first_num = int(hor_separate[0])
                second_num = int(hor_separate[1])
            except ValueError:
                return False
            else:
                if type(first_num) is int and type(second_num) is int:
                    if 1 <= first_num <= 23:
                        if 59 >= second_num >= 0:
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
        else:
            return False


if __name__ == '__main__':
    format_schedules('09:16')