# ------------------------------------------------------- #
#    Gohan 1.0.0 - Assistente virtual para deficientes    #
# ------------------------------------------------------- #

import speech_recognition as sr
import pyautogui as pag
import os


# - Reconhecimento de voz - #
while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        print('Ouvindo ...')
        Result = str(r.recognize_google(audio, language="pt-BR"))
        print(Result)
    except sr.UnknownValueError:
        print("Desculpe, não consegui entender!")
    except sr.RequestError as e:
        print("Erro ao chamar Google Speech Recognizer Service; {e}".format(e))
    # - Tratamento do aplicativo - #
    if Result == "iniciar aplicativo" or Result == "iniciar aplicativo matemático":
        os.startfile('C:/Users/Marcio/Desktop/Applications/winplot_2.exe')

    elif Result == "reiniciar" or Result == "Reiniciar aplicativo":
        pag.hotkey("alt", "f4")

    elif Result == "fechar janela" or Result == "fechar" or Result == "fechar aplicativo" or Result == "Fechar aplicativo":
        pag.hotkey("alt", "f4")
    elif Result == "ok" or Result == "Ok" or Result == "enter" or Result == "Enter":
        pag.press("enter")

    # - Tratamento da aplicação - #    
    else:
        if (Result == "duas dimensões" or Result == "2 dimensões" or Result == "duas dimensoes"):
            pag.press("f2")
        elif (Result == "três dimensões" or Result == "3 dimensões" or Result == "tres dimensoes"):
            pag.press("f3")
        elif Result == "abrir" or Result == "abrir arquivo" or Result == " abrir projeto":
            pag.hotkey("Ctrl", "o")
        elif Result == "novo" or Result == "novo arquivo" or Result == "novo projeto":
            pag.hotkey("Ctrl", "n")
        elif Result == "salvar" or Result == "salvar arquivo" or Result == "salvar projeto":
            pag.hotkey("Ctrl", "s")
        elif Result == "salvar como" or Result == "salvar arquivo como" or Result == "salvar projeto como":
            pag.hotkey("Ctrl", "shift", "s")
        elif Result == "imprimir" or Result == "imprimir arquivo" or Result == "imprimir projeto":
            pag.hotkey("Ctrl", "p")
        elif Result == "formato" or Result == "formatar":
            pag.hotkey("Ctrl", "shift", "p")

# Simula a digitação da string, tecla a tecla.
# pyautogui.typewrite("PROJETO INICIANDO!")
