import pyautogui
import time
import os

try:
    while True:
        x, y = pyautogui.position()  # Obtém as coordenadas do cursor do mouse
        os.system("cls")
        print(f'Posição do Cursor: X: {x}, Y: {y}',end='\r')

except KeyboardInterrupt:
    print("\nMonitoramento interrompido.")
