from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

# 1. Configurações
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--start-maximized")

# 2. Driver
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico, options=chrome_options)
wait = WebDriverWait(navegador, 15)

# 3. Abrir site
navegador.get("https://dlp.hashtagtreinamentos.com/python/intensivao/login")

# 4. Login
email_input = wait.until(EC.element_to_be_clickable((By.ID, "email")))
email_input.send_keys("joselucassilva81493@gmail.com")
time.sleep(0.5)

password_input = navegador.find_element(By.ID, "password")
password_input.send_keys("hashtagpython2026")
time.sleep(0.5)

password_input.send_keys(Keys.ENTER) 

# Verificação de segurança para o login
try:
    if "login" in navegador.current_url:
        botao_login = navegador.find_element(By.ID, "pgbtpython001_botao_login")
        navegador.execute_script("arguments[0].click();", botao_login)
except:
    pass

# 5. Aguardar tela de cadastro
print("Iniciando registros com pausa de 0.5s...")
wait.until(EC.visibility_of_element_located((By.ID, "codigo")))

# 6. Base e Loop
tabela = pd.read_csv("produtos.csv")

for linha in tabela.index:
    # --- PREENCHIMENTO COM PAUSAS DE 0.5s ---
    
    navegador.find_element(By.ID, "codigo").send_keys(str(tabela.loc[linha, "codigo"]))
    time.sleep(0.5)
    
    navegador.find_element(By.ID, "marca").send_keys(str(tabela.loc[linha, "marca"]))
    time.sleep(0.5)
    
    navegador.find_element(By.ID, "tipo").send_keys(str(tabela.loc[linha, "tipo"]))
    time.sleep(0.5)
    
    navegador.find_element(By.ID, "categoria").send_keys(str(tabela.loc[linha, "categoria"]))
    time.sleep(0.5)
    
    navegador.find_element(By.ID, "preco_unitario").send_keys(str(tabela.loc[linha, "preco_unitario"]))
    time.sleep(0.5)
    
    navegador.find_element(By.ID, "custo").send_keys(str(tabela.loc[linha, "custo"]))
    time.sleep(0.5)
    
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        navegador.find_element(By.ID, "obs").send_keys(obs)
    time.sleep(0.5)
    
    # --- ENVIO ---
    navegador.find_element(By.ID, "obs").send_keys(Keys.ENTER)
    
    try:
        btn_enviar = navegador.find_element(By.ID, "pgbtpython001_botao_enviar")
        navegador.execute_script("arguments[0].click();", btn_enviar)
    except:
        pass

    # Pausa final um pouco maior (1.0s) para garantir que o site limpou tudo
    time.sleep(1.0) 
    navegador.execute_script("window.scrollTo(0, 0);")
    
    print(f"Produto {linha + 1} cadastrado.")

print("\n--- Tudo pronto! ---")