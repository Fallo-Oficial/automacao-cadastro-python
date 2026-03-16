# Automação de Cadastro de Produtos (Python) 🤖

Este projeto automatiza o processo de login e cadastro de produtos em um sistema web a partir de uma base de dados em formato CSV. O repositório demonstra a evolução de uma automação simples para uma solução robusta e escalável.

## 🚀 Evolução do Projeto

Organizei este repositório em duas etapas para demonstrar o aprendizado e a otimização do código:

### v1: Automação com PyAutoGUI
- **Abordagem:** Simulação de periféricos (mouse e teclado) através de coordenadas de tela.
- **Características:** - Utiliza `pyautogui` para cliques e digitação.
  - Dependente da resolução e posição das janelas na tela.
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
  - `Selenium`: Para automação web robusta.
  - `PyAutoGUI`: Para automação baseada em interface gráfica.
  - `Webdriver Manager`: Para gestão automática do ChromeDriver.

## 📦 Como Usar

1. **Clone este repositório:**
   ```bash
   git clone [https://github.com/seu-usuario/nome-do-repositorio.git](https://github.com/seu-usuario/nome-do-repositorio.git)