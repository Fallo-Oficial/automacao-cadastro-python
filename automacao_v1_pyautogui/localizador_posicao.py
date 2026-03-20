import pyautogui
import time

# Este script serve para ajudar você a encontrar as coordenadas (X, Y) 
# dos campos de entrada no seu monitor.

print("---------------------------------------------------------")
print("📍 LOCALIZADOR DE COORDENADAS (PREPARAÇÃO)")
print("---------------------------------------------------------")
print("1. Abra a página do sistema no navegador.")
print("2. Você tem 5 segundos para posicionar o mouse sobre o campo desejado.")
print("3. Não clique, apenas deixe o mouse parado em cima do campo.")
print("---------------------------------------------------------")

# Contagem regressiva para dar tempo do usuário mudar de janela
for i in range(5, 0, -1):
    print(f"Capturando em {i}s...")
    time.sleep(1)

# Pega a posição atual do mouse
x, y = pyautogui.position()

print("---------------------------------------------------------")
print(f"✅ POSIÇÃO CAPTURADA!")
print(f"X: {x} | Y: {y}")
print("---------------------------------------------------------")
print(f"Agora, substitua esses valores no código de automação:")
print(f"Exemplo: pyautogui.click(x={x}, y={y})")
print("---------------------------------------------------------")