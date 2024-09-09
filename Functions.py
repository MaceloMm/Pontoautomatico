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

    def cerebro():
        if time.strftime("%H") == '20':
            global ultimo_horario
            funcao()
            time.sleep(4)
            whatsapp()
            time.sleep(1)
            pyautogui.click(x=20, y=1057, button='RIGHT')
            time.sleep(1)
            pyautogui.click(x=136, y=1012)
            time.sleep(1)
            pyautogui.click(x=378, y=917)
            ultimo_horario = False
        else:
            funcao()
    return cerebro

@final
def bater_ponto(email='', __password__='', coodernadas=None):
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
            navegador.find_element('xpath', '//*[@id="Login"]').send_keys('macelo.matos@e-deploy.com.br')
            navegador.find_element('xpath', '//*[@id="form0"]/div[3]/p/button').click()
            time.sleep(1)
            navegador.find_element('xpath', '//*[@id="Senha"]').send_keys('784512@Ma')
            navegador.find_element('xpath', '//*[@id="form0"]/div[3]').click()
            time.sleep(15)
            navegador.find_element('xpath', '//*[@id="app"]/div/section/section/div[1]/div[2]/div/div/div/div[1]/div[1]').click()
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
            pyautogui.click(x=638, y=634)
            time.sleep(3)
            pyautogui.click(x=954, y=698)
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

def cadastro(email='', senha=''):
    servico = Service(ChromeDriverManager().install())
    navegador = webdriver.Chrome(service=servico)
    navegador.get('https://login.lg.com.br/login/bluke_edeploy')
    time.sleep(3)
    navegador.find_element('xpath', '//*[@id="Login"]').send_keys(email)
    navegador.find_element('xpath', '//*[@id="form0"]/div[3]/p/button').click()
    time.sleep(1)
    navegador.find_element('xpath', '//*[@id="Senha"]').send_keys(senha)
    navegador.find_element('xpath', '//*[@id="form0"]/div[3]').click()
    time.sleep(5)
    #navegador.find_element('xpath',
    #                       '//*[@id="app"]/div/section/section/div[1]/div[2]/div/div/div/div[1]/div[1]').click()
    messagebox.showinfo('Importante!', 'Clique em marcar')


def __start_loop__(horaios):
    schedule.every().day.at("11:55").do(bater_ponto)
    schedule.every().day.at("18:02").do(bater_ponto)
    schedule.every().day.at("19:02").do(bater_ponto)
    schedule.every().day.at("20:58").do(bater_ponto)

    while ultimo_horario:
        schedule.run_pending()
        time.sleep(1)


