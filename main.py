#!python

import os
import sys
from random import choice
from selenium.webdriver import ActionChains
import pyttsx3
import speech_recognition as sr
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui
from y0004 import lista
from datetime import time, datetime
import time
from selenium.webdriver.chrome.options import Options

engine = pyttsx3.init()
engine.setProperty("voice", "brazil")
engine.setProperty("rate", 200)
engine.setProperty("volume", 1.)


def cadastro():
    engine.say('Olá sou Felipa, sua Assistente virtual')
    engine.runAndWait() 
    engine.say('você já possui um cadastro?')
    engine.runAndWait()
    if 'sim' in entrar_audiosn():
        login()
    else:
        engine.say('Deseja fazer seu cadastro')
        engine.runAndWait()
        cadas = entrar_audiosn()
        if 'sim' in cadas:
            engine.say('Iniciando cadastro...')
            engine.runAndWait()
            while True:
                id = len(lista) + 1
                engine.say('qual é o seu nome?')
                engine.runAndWait()
                nome = entrar_audio()
                engine.say(
                    f'ok {nome}, escolha um número, entre 1 e 100 , para ser seu usuário')
                engine.runAndWait()
                usuario = entrar_audio()
                for c in lista:
                    used = c['usuario']
                    while usuario in used:
                        engine.say('número já foi utilizado, escolha outro')
                        engine.runAndWait()
                        usuario = entrar_audio()

                # engine.say('Qual cidade você mora?')
                # engine.runAndWait()
                # cidade = entrar_audio()
                engine.say('agora crie uma senha')
                engine.runAndWait()
                senha = entrar_audio().lower()
                engine.say(f'Finalizando... seu nome é {nome}, seu usuário é {usuario},'
                           f' sua senha é {senha}, Está correto?')
                engine.runAndWait()
                if 'sim' in entrar_audiosn():
                    engine.say('lembrando é importante ter o download do spotify em seu computador'
                               ' para que eu consiga usar a função plei, de tocar músicas')
                    engine.runAndWait()
                    engine.say(
                        'deseja que eu faça a instalação? Se já possuir, diga que não')
                    engine.runAndWait()
                    spotify = entrar_audio()
                    if 'sim' in spotify or 'desejo' in spotify or 'quero' in spotify:
                        nav = webdriver.Chrome()
                        nav.minimize_window()
                        nav.maximize_window()
                        nav.get('https://www.spotify.com/br/download/windows/')
                        nav.find_element(
                            By.XPATH, '//*[@id="__next"]/main/section[1]/div/div/button/div[1]').click()
                        engine.say(
                            'ja iniciei a instalação, como não tenho acesso finalize-a para mim')
                        engine.runAndWait()
                        engine.say('quando finalizar digite pronto no console')
                        engine.runAndWait()
                        k = input('->')

                    informacoes = {'id': f'{id}', 'senha': f'{senha}', 'nome': f'{nome}', 'usuario': f'{usuario}'
                                   }
                    lista.append(informacoes)

                    with open('ziafelipa\y0004.py', 'w') as tempf:
                        tempf.write(f'lista = {lista}')
                    break
                else:
                    continue

            engine.say('salvando...')
            engine.runAndWait()
            engine.say('downloads concluídos..')
            engine.runAndWait()
            engine.say('você deseja entrar em sua assistente virtual?')
            engine.runAndWait()
            resp = entrar_audiosn()
            if 'sim' in resp:
                login()
            else:
                engine.say('ok, finalizando...')
                engine.runAndWait()
                sair()




def login():
    engine.say('qual é seu nome')
    engine.runAndWait()
    nome = entrar_audio()
    for p in lista:
        if p['nome'] == nome:
            dic = p
            while True:
                engine.say('qual é seu número para logiin')
                engine.runAndWait()
                usuario = entrar_audio()
                if usuario in dic['usuario']:
                    while True:
                        engine.say(f'ok {nome}, me informe sua senha')
                        engine.runAndWait()
                        senha = entrar_audio()
                        print(senha)
                        if senha in dic['senha']:
                            engine.say(f'Autenticado...')
                            engine.runAndWait()
                            break
                        elif senha not in dic['senha']:
                            engine.say('senha incorreta, tente novamente')
                            engine.runAndWait()
                    break
                else:
                    engine.say('número para logiin incorreto, tente novamente')
                    engine.runAndWait()
    return usuario


def entrar_audio():
    frase = ''
    while frase == '':
        microfone = sr.Recognizer()
        with sr.Microphone() as source:
            microfone.adjust_for_ambient_noise(source)
            audio = microfone.listen(source)
        try:
            frase = microfone.recognize_google(audio, language='pt-BR')

        except sr.UnknownValueError:
            engine.say('')
            engine.runAndWait()
        return frase


def entrar_audiosn():
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)
        audio = microfone.listen(source)
    try:
        frase = microfone.recognize_google(audio, language='pt-BR')

    except sr.UnknownValueError:
        engine.say('')
        engine.runAndWait()
    if frase != 'sim' and frase != 'não':
        engine.say('lembrando só consigo responder perguntas com sim e não')
        engine.runAndWait()
        while True:
            with sr.Microphone() as source:
                microfone.adjust_for_ambient_noise(source)
                audio = microfone.listen(source)
            try:
                frase = microfone.recognize_google(audio, language='pt-BR')

            except sr.UnknownValueError:
                engine.say('')
                engine.runAndWait()
            return frase
    elif frase == 'sim' or frase == 'não':
        return frase


def google(pesquisa):
    palavrasp = 'pesquise', 'pesquisar', 'por', 'busque', 'buscar', 'felipa', 'pesquisa'
    for x in range(len(palavrasp)):
        pesquisa = pesquisa.replace(palavrasp[x], '')
    nav = webdriver.Chrome()
    nav.minimize_window()
    nav.maximize_window()
    nav.get('https://www.google.com.br/?gws_rd=ssl')
    nav.execute_script("document.body.style_zoom='50%'")
    nav.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')\
        .send_keys(pesquisa)
    nav.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')\
        .send_keys(Keys.ENTER)
    engine.say(f'está aqui oque achei sobre {pesquisa}')
    engine.runAndWait()
    while True:
        feche = entrar_audio().lower()
        print(feche)
        if 'fechar' in feche or 'feche' in feche or 'google' in feche or 'aba' in feche:
            nav.close()
            break
        elif 'link' in feche or 'página' in feche or 'entrar' in feche:
            engine.say('me fale o nome da página em que deseja entrar')
            engine.runAndWait()
            site = entrar_audio()
            site1 = site.title()
            if nav.find_element(By.PARTIAL_LINK_TEXT, site1).is_displayed() == True:
                nav.find_element(By.PARTIAL_LINK_TEXT, site1).click()
            elif nav.find_element(By.PARTIAL_LINK_TEXT, site1).is_displayed() == False:
                site2 = site.upper()
                if nav.find_element(By.PARTIAL_LINK_TEXT, site2).is_displayed() == True:
                    nav.find_element(By.PARTIAL_LINK_TEXT, site2).click()
                if nav.find_element(By.PARTIAL_LINK_TEXT, site2).is_displayed() == False:
                    site3 = site.lower()
                    if nav.find_element(By.PARTIAL_LINK_TEXT, site3).is_displayed() == True:
                        nav.find_element(By.PARTIAL_LINK_TEXT, site3)
                    elif nav.find_element(By.PARTIAL_LINK_TEXT, site3).is_displayed() == False:
                        engine.say(
                            'nao encontrei esse site, tente ser mais específico')
                        engine.runAndWait()

        elif 'voltar' in feche or 'volte' in feche:
            nav.back()
        elif 'descer' in feche or 'abaixar' in feche or 'desça' in feche or 'descer a página' \
                in feche or 'seta para baixo' in feche or 'baixa' in feche:
            for c in range(1, 6):
                pyautogui.hotkey('down')
        elif 'subir' in feche or 'levantar' in feche or 'suba' in feche or 'suba a página' \
                in feche or 'seta para cima' in feche or 'cima' in feche:
            for c in range(1, 6):
                pyautogui.hotkey('up')
        princi(feche)


def periodos():
    timeee = datetime.now().strftime('%H:%M')
    if '06:00:00' < timeee < '11:59:00':
        return 'bom dia !!'
    elif '12:00:00' < timeee < '17:59:00':
        return 'boa tarde !!'
    elif '18:00:00' < timeee < '23:59:00':
        return 'boa noite !!'
    elif '00:00:00' < timeee < '05:59:00':
        return 'boa noite !!'


def wpp():
    opt = Options()
    opt.add_argument("--disable-infobars")
    opt.add_argument("start-maximized")
    opt.add_argument("--disable-extensions")
    # Pass the argument 1 to allow and 2 to block
    opt.add_experimental_option("prefs", {
        "profile.default_content_setting_values.media_stream_mic": 1,
        "profile.default_content_setting_values.media_stream_camera": 1,
        "profile.default_content_setting_values.geolocation": 1,
        "profile.default_content_setting_values.notifications": 1
    })
    nav = webdriver.Chrome(chrome_options=opt)
    nav.minimize_window()
    nav.maximize_window()
    nav.get('https://web.whatsapp.com/')
    engine.say('abra o aplicativo em seu celular e valide o QR code')
    engine.runAndWait()
    while len(nav.find_elements(By.ID, "side")) < 1:
        time.sleep(1)
    engine.say('posso enviar mensagens e gravar áudios,  oque precisa ')
    engine.runAndWait()
    while True:
        deswpp = entrar_audio()
        if 'enviar' in deswpp or 'envie' in deswpp or 'escrever' in deswpp or 'envia' in deswpp:
            while True:
                engine.say('para quem deseja enviar uma mensagem ?')
                engine.runAndWait()
                pessoa = entrar_audio()
                engine.say(f'ok! oque deseja enviar para {pessoa}?')
                engine.runAndWait()
                msg = entrar_audio()
                nav.find_element(
                    By.XPATH, '//*[@id="side"]/div[1]/div/label/div/div[2]').send_keys(pessoa)
                time.sleep(2)
                pyautogui.hotkey('tab')
                time.sleep(3)
                pyautogui.hotkey('enter')
                time.sleep(3)
                nav.find_element(
                    By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]').send_keys(msg)
                time.sleep(2)
                nav.find_element(
                    By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]').send_keys(Keys.ENTER)
                engine.say('aguarde um momento para concluir o envio')
                engine.runAndWait()
                time.sleep(3)
                engine.say(f'enviado {msg} para {pessoa}')
                engine.runAndWait()
                engine.say('deseja enviar mas alguma mensagem ?')
                engine.runAndWait()
                sorn = entrar_audio()
                if 'sim' in sorn or 'desejo' in sorn or 'quero' in sorn:
                    pass
                elif 'não' in sorn or 'não desejo' in sorn:
                    nav.close()
                    break

        elif 'gravar' in deswpp or 'audio' in deswpp or 'áudio' in deswpp:
            while True:
                engine.say('deixe eu me configurar para gravar um áudio')
                engine.runAndWait()
                engine.say('para quem deseja enviar uma mensagem de voz ?')
                engine.runAndWait()
                pessoa = entrar_audio()
                nav.find_element(
                    By.XPATH, '//*[@id="side"]/div[1]/div/label/div/div[2]').send_keys(pessoa)
                time.sleep(2)
                pyautogui.hotkey('tab')
                time.sleep(3)
                pyautogui.hotkey('enter')
                time.sleep(3)
                engine.say(f'fale oque quer falar a {pessoa}')
                engine.runAndWait()
                nav.find_element(
                    By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]').click()
                tes = entrar_audio()
                nav.find_element(
                    By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[1]/div/div/button[2]').click()
                time.sleep(4)
                engine.say('audio enviado.')
                engine.runAndWait()
                engine.say('deseja enviar mas alguma mensagem de voz ?')
                engine.runAndWait()
                sornmvoz = entrar_audio()
                if 'sim' in sornmvoz or 'desejo' in sornmvoz or 'quero' in sornmvoz:
                    pass
                elif 'não' in sornmvoz or 'não desejo' in sornmvoz:
                    nav.close()
                    break

        princi(deswpp)
        break

def sair():
    engine.say('encerrando...')
    engine.runAndWait()
    exit()



def perguntas(perg):
    timee = datetime.now().strftime('%H:%M')
    if '06:00:00' < timee < '11:59:00':
        boas = 'bom dia !!'
    elif '12:00:00' < timee < '17:59:00':
        boas = 'boa tarde !!'
    elif '18:00:00' < timee < '23:59:00':
        boas = 'boa noite !!'
    elif '00:00:00' < timee < '05:59:00':
        boas = 'boa noite !!'

    oisresp = ['oii', 'olá', 'oi tudo bem?',
               'olá como você está', 'oi tudo joia?', 'E aí', boas]
    tdbemresp = ['estou ótima', 'nunca estive tão bem', 'estou muito bem',
                 'estou incrivelmente melhor agora', 'tudo ótimo', 'nunca estive melhor']
    if 'oi' in perg or 'olá' in perg or 'eai' in perg or 'iai' in perg or 'iae' in perg or 'opa' in perg:
        engine.say(choice(oisresp))
        engine.runAndWait()
    elif 'tudo bem?' in perg or 'tudo bem' in perg or 'você está bem' in perg or 'bem' in perg or 'tudo' in perg or 'está' in perg:
        engine.say(choice(tdbemresp))
        engine.runAndWait()


def spotify(musica):
    os.system('taskkill /f /im Spotify.exe')
    palavrasp = 'tocar', 'toque', 'play', 'pley', 'toca'
    for x in range(len(palavrasp)):
        musica = musica.replace(palavrasp[x], '')
    if 'chuva' in musica:
        nav = webdriver.Chrome()
        nav.get('https://www.youtube.com/watch?v=j23U-_EFoVE')
        time.sleep(2)
        pyautogui.hotkey('enter')
        nav.minimize_window
        bla = entrar_audio
    else:
        pyautogui.hotkey('win')
        time.sleep(2)
        pyautogui.write('spotify')
        pyautogui.hotkey('enter')
        time.sleep(6)
        engine.say(f'aguarde, estamos dando plei em {musica}')
        engine.runAndWait()
        time.sleep(2)
        pyautogui.hotkey('tab')
        pyautogui.hotkey('tab')
        pyautogui.hotkey('tab')
        pyautogui.hotkey('enter')
        time.sleep(2)
        pyautogui.write(musica)
        time.sleep(2)
        pyautogui.hotkey('enter')
        pyautogui.hotkey('tab')
        pyautogui.hotkey('enter')
        time.sleep(4)
        pyautogui.hotkey('enter')
        engine.say(f'tocando {musica}')
        engine.runAndWait()
        pyautogui.hotkey('win', 'down')
        pyautogui.hotkey('win', 'down')


def horas():
    engine.say('agora são')
    engine.runAndWait()
    engine.say(datetime.now().strftime('%H:%M:%S'))
    engine.runAndWait()


def data():
    engine.say('hoje é dia ')
    engine.runAndWait()
    engine.say(datetime.now().strftime('%d-%m-%Y'))
    engine.runAndWait()


def princi(depende):
    if 'pesquise' in depende or 'busque' in depende or 'por' in depende:
        google(depende)
    elif 'horas' in depende or 'horário' in depende:
        horas()
    elif 'data' in depende or 'dia' in depende or 'ano' in depende or 'mês' in depende:
        data()
    elif 'whatsapp' in depende:
        wpp()
    elif 'felipa encerrar' in depende or 'felipa sair' in \
            depende or 'parar felipa' in depende or 'sair' in depende or 'encerrar' in depende:
        sair()
    elif 'música' in depende or 'tocar' in depende or 'spotify' in depende or 'play' in depende or 'toque' in depende:
        spotify(depende)
    elif 'descansar' in depende or 'suspender' in depende or 'suspenda' in depende or 'descansa' in depende:
        engine.say('suspendendo, chame por felipa para que eu retorne')
        engine.runAndWait()
        while True:
            back = entrar_audio().lower()
            if back == 'felipa' or back == 'Felipa':
                engine.say('estou te ouvindo')
                engine.runAndWait()
                break
            else:
                pass
    else:
        perguntas(depende)





def pos():
    cadastro()
    engine.say(f'olá nome {periodos()}')
    engine.runAndWait()
    engine.say('estou te ouvindo, se quiser um tempo peça que eu suspenda')
    engine.runAndWait()
    while True:
        resp = entrar_audio().lower()
        princi(resp)
    


pos()
