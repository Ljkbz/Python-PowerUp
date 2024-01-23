#Passo a passo do projeto

#Passo1-entrar no sistema da empresa
#https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui
import time

#clicar -> pyautogui.click
#escrever -> pyautogui.write
#apertar um tecla -> pyautogui.press
#apertar -> pyautogui.hotkey
#rolar-pyautogui.scroll
pyautogui.PAUSE = 0.5
#aperta a tecla do windows(command + barra de espaço)
pyautogui.press("win")

#digita o nome do programa(chrome)
pyautogui.write("chrome")

#aperta enter
pyautogui.press("enter")

#digitar o link
link= 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
pyautogui.write(link)

#apertar enter
pyautogui.press("enter")

#esperar cinco segundos
time.sleep(3)


#Passo 2- Fazer Login
pyautogui.click(x=750, y=417)
#digitar o email
pyautogui.write("luizgustavodossantos@gmail.com")
pyautogui.press("tab")
pyautogui.write("Luiz@2610")
pyautogui.click(x=677, y=572)
time.sleep(3)

#Passo 3-Importar a base dados
#pip install pandas numpy openpyxl
import pandas as pd

tabela = pd.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:
    #Passo 4- Cadastrar o produto
    pyautogui.click(x=819, y=289)
    #codigo
    codigo= tabela.loc[linha,"codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    #marca
    pyautogui.write(tabela.loc[linha,"marca"])
    pyautogui.press("tab")

    #tipo
    pyautogui.write(tabela.loc[linha,"tipo"])
    pyautogui.press("tab")
 

    #categoria
    pyautogui.write(str(tabela.loc[linha,"categoria"]))
    pyautogui.press("tab")

    #preco_unitario
    pyautogui.write(str(tabela.loc[linha,"preco_unitario"]))
    pyautogui.press("tab")

    #custo
    pyautogui.write(str(tabela.loc[linha,"custo"]))
    pyautogui.press("tab")

    #obs
    obs:tabela.loc[linha,"obs"]
    pyautogui.write(str(tabela.loc[linha,"obs"]))
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))

    #enviar o produto
    pyautogui.write("tab")
    pyautogui.press("enter")

    pyautogui.scroll(5000)

#Passo 5- 