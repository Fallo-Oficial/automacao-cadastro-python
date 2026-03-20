import pyautogui
import time
import pandas as pd

# ==========================================================
# ⚙️ CONFIGURAÇÕES DE ACESSO E ARQUIVOS (DADOS REAIS)
# ==========================================================
URL_SISTEMA = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
ARQUIVO_DADOS = "Produtos.csv"
EMAIL_USUARIO = "TesteAutomação@gmail.com"
SENHA_USUARIO = "TesteAutomação2026"

# Pausa global entre comandos (evita atropelamento)
pyautogui.PAUSE = 0.5
# ==========================================================

# Passo 1: Entrar no sistema da empresa
print("Iniciando o navegador...")
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# Pequena pausa para o Chrome abrir
time.sleep(2)
pyautogui.write(URL_SISTEMA)
pyautogui.press("enter")

# Pausa maior para o site carregar
time.sleep(3)

# Passo 2: Fazer login
print(f"Realizando login com: {EMAIL_USUARIO}")
# Clique no campo de e-mail (coordenadas baseadas no seu código original)
pyautogui.click(x=760, y=376)
pyautogui.write(EMAIL_USUARIO)
pyautogui.press("tab") 

pyautogui.write(SENHA_USUARIO)
pyautogui.press("tab") 
pyautogui.press("enter")

# Pausa para carregar a tela interna de cadastro
time.sleep(4)

# Passo 3: Abrir a base de dados
try:
    tabela = pd.read_csv(ARQUIVO_DADOS)
    print(f"Base de dados '{ARQUIVO_DADOS}' carregada com sucesso!")
except FileNotFoundError:
    print(f"❌ Erro: O arquivo {ARQUIVO_DADOS} não foi encontrado na pasta do projeto.")
    exit()

# Passo 4 e 5: Loop de Cadastro de Produtos
print(f"Iniciando cadastro de {len(tabela)} itens...")

for linha in tabela.index:
    # Clica no primeiro campo (Código)
    pyautogui.click(x=726, y=258) 

    # Preenchimento sequencial usando as colunas do seu CSV
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")
    
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    
    # Tratamento para observações (pula se estiver vazio/nan)
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")

    # Finalizar cadastro do produto atual
    pyautogui.press("enter")
    
    # Scroll para garantir que a tela volte ao topo para o próximo item
    pyautogui.scroll(5000)
    
    print(f"✅ [{linha + 1}/{len(tabela)}] Produto {tabela.loc[linha, 'codigo']} cadastrado.")

print("\n🚀 Automação concluída com sucesso!")