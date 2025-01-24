# _*_ coding: utf-8 _*_

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException, TimeoutException
import selenium
import schedule
import time
import pyautogui
import datetime
import keyboard
from tkinter import messagebox
import os
import threading
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

    def brain(__email__, __password__, last_time_=None, var=None):
        if last_time_ is not None:
            if time.strftime("%H") == last_time_.split(':')[0]:
                global ultimo_horario
                funcao(__email__, __password__)
                time.sleep(4)
                # whatsapp()
                if var == 1:
                    os.system('rundll32.exe user32.dll,LockWorkStation')
                ultimo_horario = False
            else:
                funcao(__email__, __password__)
        else:
            funcao(__email__, __password__)
    return brain


@final
def bater_ponto(__email__='', __password__='', last_time_=None, var=None):
    sucess = False
    while not sucess:
        try:
            # Configurações do navegador
            servico = Service(ChromeDriverManager().install())
            navegador = webdriver.Chrome(service=servico)
            navegador.get('https://login.lg.com.br/login/bluke_edeploy')

            # login
            WebDriverWait(navegador, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="Login"]'))
            ).send_keys(__email__)

            WebDriverWait(navegador, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="form0"]/div[3]/p/button'))
            ).click()

            WebDriverWait(navegador, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="Senha"]'))
            ).send_keys(__password__)

            WebDriverWait(navegador, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="form0"]/div[3]'))
            ).click()
            if navegador.get_window_size()["width"] >= 1265 and navegador.get_window_size()["height"] >= 1020:
                time.sleep(10)
                navegador.find_element(By.XPATH, '//*[@id="app"]/div/section/section/div[1]/div[2]/div/div/div/div[1]/div[1]').click()
            else:
                time.sleep(10)
                navegador.find_element(By.XPATH, '//*[@id="app"]/div/section/section/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div[1]/div/div')

            WebDriverWait(navegador, 15).until(
                EC.presence_of_element_located((By.TAG_NAME, 'iframe'))
            )
            iframe = navegador.find_element(By.TAG_NAME, 'iframe')
            navegador.switch_to.frame(iframe)
            time.sleep(10)
            WebDriverWait(navegador, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, '//*[@id="bodyApp"]/div/div/div/div/div/div[2]/div/div[2]/div[2]/button')
                )
            ).click()
            time.sleep(10)
            WebDriverWait(navegador, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="bodyApp"]/div[3]/div[7]/div/button'))
            ).click()
            time.sleep(5)
            texto = WebDriverWait(navegador, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="bodyApp"]/div[3]/h2'))
            ).text
            if texto.lower() == 'Marcação realizada com sucesso.'.lower():
                print(f'ponto batido com sucesso')
                with open('log.txt', 'a') as arquivo:
                    arquivo.write(f'Ponto batido as {datetime.datetime.today()}\n')
                sucess = True

        except (ElementNotInteractableException, NoSuchElementException, TimeoutException) as err:
            with open('log.txt', 'a') as arquivo:
                arquivo.write(f'{datetime.datetime.now()}ERROR: Ocorreu um ERRO!\n')
            with open('log_ERRO.txt', 'a') as arquivo:
                arquivo.write(f'{datetime.datetime.now()}ERROR: {err}\n')

        finally:
            try:
                navegador.quit()
            except:
                pass
            if not sucess:
                print("Tentando novamente em 10 segundos....")
                time.sleep(10)


def registration_user(email='', senha=''):
    usuario = User(email, senha)
    resultado = usuario.insert_user()
    return resultado


def __start_loop__(utilizar=None, __times__=None, block=None):
    def rodar_schedules():
        while True:
            print(f'{datetime.datetime.now()} - estou rodando...')
            schedule.run_pending()
            time.sleep(1)

    def rodar_loops(__times__=__times__):
        last_time = __times__[len(__times__) - 1]
        email, senha = User.select_user()
        for time in __times__[:-1]:
            schedule.every().day.at(time).do(
                lambda: bater_ponto(__email__=email, __password__=senha)
            )
        schedule.every().day.at(last_time).do(
            lambda: bater_ponto(__email__=email, __password__=senha, last_time_=last_time, var=block)
        )

    # Pensar num jeito de fazer essa birosca que vc invetou funcioanar, cabeça de pica.
    if utilizar:
        __times__ = Usuarios.SchedulesMm.select_horario()
        __times__ = [h for h in __times__ if h is not None]

        rodar_loops(__times__)

        thread = threading.Thread(target=rodar_schedules, daemon=True)
        thread.start()

        """
        if len(__times__) == 2:
            schedule.every().day.at(__times__[0]).do(
                lambda: bater_ponto(__email__=email, __password__=senha))
            schedule.every().day.at(__times__[1]).do(
                lambda: bater_ponto(__email__=email, __password__=senha, last_time_=last_time, var=block))
        elif len(__times__) == 3:
            schedule.every().day.at(__times__[0]).do(
                lambda: bater_ponto(__email__=email, __password__=senha))
            schedule.every().day.at(__times__[1]).do(
                lambda: bater_ponto(__email__=email, __password__=senha))
            schedule.every().day.at(__times__[2]).do(
                lambda: bater_ponto(__email__=email, __password__=senha, last_time_=last_time, var=block))
        elif len(__times__) == 4:
            schedule.every().day.at(__times__[0]).do(
                lambda: bater_ponto(__email__=email, __password__=senha))
            schedule.every().day.at(__times__[1]).do(
                lambda: bater_ponto(__email__=email, __password__=senha))
            schedule.every().day.at(__times__[2]).do(
                lambda: bater_ponto(__email__=email, __password__=senha))
            schedule.every().day.at(__times__[3]).do(
                lambda: bater_ponto(__email__=email, __password__=senha, last_time_=last_time, var=block))
        else:
            return 'Não existe horarios validos cadastrados'
        thread = threading.Thread(target=rodar_schedules(), daemon=True)
        thread.start()
        return 'Terminei o dia!'
        """
    else:
        # Programar essa parte depois cabeça de pika
        __times__ = [h for h in __times__ if h != '']

        rodar_loops(__times__)
        thread = threading.Thread(target=rodar_schedules, daemon=True)
        thread.start()
        """
        if len(__times__) == 2:
            schedule.every().day.at(__times__[0]).do(
                lambda: bater_ponto(__email__=email, __password__=senha))
            schedule.every().day.at(__times__[1]).do(
                lambda: bater_ponto(__email__=email, __password__=senha, last_time_=last_time, var=block))
        elif len(__times__) == 3:
            schedule.every().day.at(__times__[0]).do(
                lambda: bater_ponto(__email__=email, __password__=senha))
            schedule.every().day.at(__times__[1]).do(
                lambda: bater_ponto(__email__=email, __password__=senha))
            schedule.every().day.at(__times__[2]).do(
                lambda: bater_ponto(__email__=email, __password__=senha, last_time_=last_time, var=block))
        elif len(__times__) == 4:
            schedule.every().day.at(__times__[0]).do(
                lambda: bater_ponto(__email__=email, __password__=senha))
            schedule.every().day.at(__times__[1]).do(
                lambda: bater_ponto(__email__=email, __password__=senha))
            schedule.every().day.at(__times__[2]).do(
                lambda: bater_ponto(__email__=email, __password__=senha))
            schedule.every().day.at(__times__[3]).do(
                lambda: bater_ponto(__email__=email, __password__=senha, last_time_=last_time, var=block))
        else:
            return 'Não existe horarios validos cadastrados'
        thread = threading.Thread(target=rodar_schedules(), daemon=True)
        thread.start()
        return 'Terminei o dia'
        """


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
                if isinstance(first_num, int) and isinstance(second_num, int):
                    if 1 <= first_num <= 23:
                        if 59 >= second_num >= 0:
                            return True
        return False


if __name__ == '__main__':
    format_schedules('09:16')