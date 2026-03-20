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

# ==========================================================
# ⚙️ CONFIGURAÇÕES DE ACESSO (SUBSTITUA PELOS SEUS DADOS)
# ==========================================================
URL_SISTEMA = "https://link-do-seu-sistema.com/login"
ARQUIVO_DADOS = "seus_produtos.csv"
EMAIL_USUARIO = "seu-email@exemplo.com"
SENHA_USUARIO = "sua-senha-aqui"
# ==========================================================

# 1. Configurações do Navegador
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--start-maximized")

# 2. Inicialização do Driver
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico, options=chrome_options)
wait = WebDriverWait(navegador, 20) 

# 3. Acesso ao Sistema
navegador.get(URL_SISTEMA)

# 4. Processo de Login
print("Realizando login no sistema...")
try:
    # Substitua os IDs abaixo pelos IDs reais dos campos do seu sistema
    email_field = wait.until(EC.element_to_be_clickable((By.ID, "email"))) 
    email_field.send_keys(EMAIL_USUARIO)
    time.sleep(0.5)

    password_field = navegador.find_element(By.ID, "password")
    password_field.send_keys(SENHA_USUARIO)
    time.sleep(0.5)
    password_field.send_keys(Keys.ENTER)
except Exception as e:
    print(f"Erro ao localizar campos de login: {e}")

# 5. Carregamento da Base de Dados
try:
    tabela = pd.read_csv(ARQUIVO_DADOS)
except FileNotFoundError:
    print(f"❌ Erro: O arquivo '{ARQUIVO_DADOS}' não foi encontrado.")
    navegador.quit()
    exit()

# 6. Loop de Cadastro Automatizado
print(f"Iniciando processamento de {len(tabela)} registros...")

# Aguarda um elemento da tela interna para confirmar o login
try:
    wait.until(EC.visibility_of_element_located((By.ID, "codigo")))
    time.sleep(1.0)
except:
    print("⚠️ Atenção: Tela interna não detectada ou demora no carregamento.")

for linha in tabela.index:
    try:
        # --- PREENCHIMENTO DOS CAMPOS ---
        # Certifique-se de que os IDs abaixo e os nomes das colunas no CSV coincidem
        
        navegador.find_element(By.ID, "codigo").send_keys(str(tabela.loc[linha, "codigo"]))
        time.sleep(0.4)
        
        navegador.find_element(By.ID, "marca").send_keys(str(tabela.loc[linha, "marca"]))
        time.sleep(0.4)
        
        navegador.find_element(By.ID, "tipo").send_keys(str(tabela.loc[linha, "tipo"]))
        time.sleep(0.4)
        
        navegador.find_element(By.ID, "categoria").send_keys(str(tabela.loc[linha, "categoria"]))
        time.sleep(0.4)
        
        navegador.find_element(By.ID, "preco_unitario").send_keys(str(tabela.loc[linha, "preco_unitario"]))
        time.sleep(0.4)
        
        navegador.find_element(By.ID, "custo").send_keys(str(tabela.loc[linha, "custo"]))
        time.sleep(0.4)
        
        obs = str(tabela.loc[linha, "obs"])
        if obs != "nan":
            navegador.find_element(By.ID, "obs").send_keys(obs)
        time.sleep(0.4)
        
        # --- ENVIO DO FORMULÁRIO ---
        # Tenta clicar no botão de enviar via ID
        btn_enviar = navegador.find_element(By.ID, "pgbtpython001_botao_enviar")
        navegador.execute_script("arguments[0].click();", btn_enviar)

        # Pausa de estabilização para o sistema processar o cadastro
        time.sleep(1.2) 
        navegador.execute_script("window.scrollTo(0, 0);")
        
        print(f"✅ Registro {linha + 1} processado com sucesso.")

    except Exception as e:
        print(f"❌ Erro ao cadastrar linha {linha + 1}: {e}")
        continue # Pula para o próximo item caso este dê erro

print("\n🚀 Automação concluída!")