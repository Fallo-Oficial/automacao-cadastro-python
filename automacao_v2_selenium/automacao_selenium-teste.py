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

# ==========================================
# ⚙️ CONFIGURAÇÕES E ACESSOS
# ==========================================
URL_SISTEMA = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
ARQUIVO_DADOS = "produtos.csv"
EMAIL_USUARIO = "TesteAutomação@gmail.com"
SENHA_USUARIO = "TesteAutomação2026"

# 1. Configuração do Navegador
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--start-maximized")

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico, options=chrome_options)

# Espera inteligente: o Selenium aguarda até 20 segundos se o elemento não aparecer de imediato
wait = WebDriverWait(navegador, 20) 

# 3. Acesso ao Sistema
navegador.get(URL_SISTEMA)

# 4. Processo de Login (com pausas de segurança)
print("Realizando login...")
email_field = wait.until(EC.element_to_be_clickable((By.ID, "email")))
email_field.send_keys(EMAIL_USUARIO)
time.sleep(0.5) # Pausa para o sistema processar o texto

password_field = navegador.find_element(By.ID, "password")
password_field.send_keys(SENHA_USUARIO)
time.sleep(0.5)

password_field.send_keys(Keys.ENTER)

# 5. Carregamento da Base de Dados
try:
    tabela = pd.read_csv(ARQUIVO_DADOS)
except FileNotFoundError:
    print(f"Erro: O arquivo {ARQUIVO_DADOS} não foi encontrado na pasta!")
    navegador.quit()
    exit()

# 6. Loop de Cadastro Automatizado
print(f"Sucesso! Iniciando cadastro de {len(tabela)} produtos...")

# Aguarda a tela interna carregar (o campo 'codigo' é o sinal de que entrou)
wait.until(EC.visibility_of_element_located((By.ID, "codigo")))
time.sleep(1.0) # Respiro extra após o login

for linha in tabela.index:
    # --- PREENCHIMENTO RÍTMICO (0.4s entre campos evita erros de digitação) ---
    
    # Código
    navegador.find_element(By.ID, "codigo").send_keys(str(tabela.loc[linha, "codigo"]))
    time.sleep(0.4)
    
    # Marca
    navegador.find_element(By.ID, "marca").send_keys(str(tabela.loc[linha, "marca"]))
    time.sleep(0.4)
    
    # Tipo
    navegador.find_element(By.ID, "tipo").send_keys(str(tabela.loc[linha, "tipo"]))
    time.sleep(0.4)
    
    # Categoria
    navegador.find_element(By.ID, "categoria").send_keys(str(tabela.loc[linha, "categoria"]))
    time.sleep(0.4)
    
    # Preço
    navegador.find_element(By.ID, "preco_unitario").send_keys(str(tabela.loc[linha, "preco_unitario"]))
    time.sleep(0.4)
    
    # Custo
    navegador.find_element(By.ID, "custo").send_keys(str(tabela.loc[linha, "custo"]))
    time.sleep(0.4)
    
    # Observação
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        navegador.find_element(By.ID, "obs").send_keys(obs)
    time.sleep(0.4)
    
    # --- ENVIO DO FORMULÁRIO ---
    # Tenta enviar pelo botão específico usando JavaScript (mais seguro)
    try:
        btn_enviar = navegador.find_element(By.ID, "pgbtpython001_botao_enviar")
        navegador.execute_script("arguments[0].click();", btn_enviar)
    except:
        navegador.find_element(By.ID, "obs").send_keys(Keys.ENTER)

    # Pausa de estabilização: Essencial para o site limpar o formulário e carregar o próximo
    time.sleep(1.2) 
    
    # Feedback visual no terminal
    print(f"✅ [{linha + 1}/{len(tabela)}] Produto {tabela.loc[linha, 'codigo']} cadastrado.")

print("\n🚀 Automação finalizada! Todos os produtos foram processados.")