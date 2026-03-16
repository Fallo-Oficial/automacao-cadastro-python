# bibliotecas = pacotes de código
# pip install pyautogui

import pyautogui
import time

# pyautogui.click -> clica
# pyautogui.write -> escreve um texto
# pyautogui.press -> aperta uma tecla
# pyautogui.hotkey -> aperta um atalho (hotkey)
pyautogui.PAUSE = 0.5
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
# Passo a passo do seu programa
# Passo 1: Entrar no sistema da empresa
# abriria o navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

pyautogui.write(link)
pyautogui.press("enter")
# fazer uma pausa maior pro site carregar
time.sleep(3) # pyautogui hashtag

# Passo 2: Fazer login
# clciar no campo de email
pyautogui.click(x=760, y=376)
pyautogui.write("joselucassilva81493@gmail.com")
pyautogui.press("tab") # passar para o próximo campo
pyautogui.write("hashtagpython2026") # qualquer senha serve
pyautogui.press("tab") # passar para o botão
pyautogui.press("enter")
# fazer uma pausa maior pro site carregar
time.sleep(4)

# Passo 3: Abrir a base de dados
# pip install pandas openpyxl
import pandas

tabela = pandas.read_csv("Produtos.csv")
print(tabela)

for linha in tabela.index:
    # Passo 4: Cadastrar 1 produto
    # codigo
    pyautogui.click(x=726, y=258) # clicar no campo do código
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab") # passar para o próximo campo
    # marca
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")
    # tipo
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")  
    # categoria
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")
    # preco
    preco = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco)
    pyautogui.press("tab")
    # custo
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")
    # obs
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab") # passar para o botão enviar

    pyautogui.press("enter") # clicou no enviar

    # voltar para o início da tela
    pyautogui.scroll(5000)

# Passo 5: Repetir o passo 4 até acabar a lista de produtos


