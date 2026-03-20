# Automação de Cadastro de Produtos (Python) 🤖

Este projeto automatiza o processo de login e cadastro de produtos em um sistema web a partir de uma base de dados em formato CSV. O repositório demonstra a evolução de uma automação baseada em interface gráfica para uma solução robusta utilizando manipulação direta do navegador.

## 🚀 Evolução do Projeto

Organizei este repositório em duas etapas para demonstrar o aprendizado e a otimização do código:

### v1: Automação com PyAutoGUI
- **Abordagem:** Simulação de periféricos (mouse e teclado) através de coordenadas de tela.
- **Características:** - Utiliza `pyautogui` para cliques e digitação.
  - Dependente da resolução e posição das janelas na tela.
  - Inclui um script de **localizador de posição** para calibração em diferentes monitores.
  - Ideal para automações rápidas em softwares de desktop que não possuem integração web.

### v2: Automação com Selenium (Otimizada)
- **Abordagem:** Manipulação direta do navegador através do DOM (HTML).
- **Melhorias:**
  - Uso de **Esperas Explícitas** (`WebDriverWait`), tornando o código mais rápido e menos propenso a erros de carregamento.
  - Integração com `webdriver-manager` para gestão automática de drivers.
  - Maior resiliência: a automação funciona mesmo com o navegador em segundo plano.

## 🛠️ Tecnologias Utilizadas
- **Linguagem:** Python 3.11+
- **Bibliotecas:** - `Pandas`: Para manipulação e leitura da base de dados (CSV).
  - `Selenium`: Para automação web de alta performance.
  - `PyAutoGUI`: Para automação baseada em coordenadas de interface.
  - `Webdriver Manager`: Para instalação automática do ChromeDriver.

## 📦 Como Usar

1. **Clone este repositório:**
  ```bash
  git clone https://github.com/Fallo-Oficial/automacao-cadastro-python
  ```

2. **Instale as dependências necessárias:**
  ```bash
  pip install pandas selenium pyautogui webdriver-manager openpyxl
  ```

3. **Configuração e Calibração**
* Para a versão PyAutoGUI (v1):
  Como esta versão depende da sua tela, use o localizador para ajustar os cliques:
  1. Execute `python localizador_posicao.py`.
  2. Posicione o mouse sobre os campos do sistema e anote as coordenadas X e Y.
  3. Atualize os valores no arquivo `automacao_pyautogui.py`.

* Para a versão Selenium (v2):
  1. Certifique-se de que o arquivo `produtos.csv` está na raiz do projeto.
  2. Abra o arquivo `automacao_selenium.py` e insira sua URL e credenciais nas variáveis de configuração no topo do script.

## 📊 Estrutura do CSV
O arquivo `produtos.csv` deve conter as seguintes colunas:
  * `codigo`
  * `marca`
  * `tipo`
  * `categoria`
  * `preco_unitario`
  * `custo`
  * `obs`

---

## 📩 Contato
- **GitHub**: [Fallo-Oficial](https://github.com/Fallo-Oficial)
- **LinkedIn**: [José Lucas Leite da Silva](https://www.linkedin.com/in/josé-lucas-leite-da-silva)