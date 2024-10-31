import pyautogui, sys
import pyautogui
import time
import cv2
import numpy as np
import random

import time
import math

def movimento_mouse_humano(duration=5, intervalo=0.1):
    """
    Move o mouse de forma aleatória e 'humana' na tela.

    Parameters:
        duration (int): duração total da movimentação em segundos.
        intervalo (float): intervalo entre cada movimento em segundos.
    """
    # Obtém as dimensões da tela
    largura, altura = pyautogui.size()
    inicio_tempo = time.time()

    while time.time() - inicio_tempo < duration:
        # Gera um ponto alvo aleatório na tela
        alvo_x = random.randint(0, largura)
        alvo_y = random.randint(0, altura)
        
        # Obtém a posição atual do mouse
        x_atual, y_atual = pyautogui.position()

        # Calcula a distância até o ponto alvo
        distancia = math.hypot(alvo_x - x_atual, alvo_y - y_atual)
        
        # Define uma velocidade aleatória e ajusta o intervalo entre movimentos
        velocidade = random.uniform(0.2, 0.5)
        passos = int(distancia / velocidade)

        # Gera a trajetória com pequenas variações para simular um movimento humano
        for i in range(passos):
            if time.time() - inicio_tempo >= duration:
                break
            # Cálculo da posição intermediária
            t = i / passos
            x_intermediario = int(x_atual + (alvo_x - x_atual) * t + random.randint(-3, 3))
            y_intermediario = int(y_atual + (alvo_y - y_atual) * t + random.randint(-3, 3))

            # Move o mouse para a posição intermediária
            pyautogui.moveTo(x_intermediario, y_intermediario)
            time.sleep(intervalo * random.uniform(0.5, 1.5))

        # Pausa aleatória entre movimentos
        time.sleep(random.uniform(0.5, 2))

# Exemplo de uso da função



def movimento_humano(destino_x, destino_y):
    # Adiciona um desvio aleatório à posição destino
    destino_x += random.randint(-10, 10)
    destino_y += random.randint(-10, 10)

    # Define uma duração aleatória para o movimento
    duracao = random.uniform(0.5, 1.0)

    # Seleciona uma função de easing aleatória
    funcoes_easing = [
        pyautogui.easeInQuad,
        pyautogui.easeOutQuad,
        pyautogui.easeInOutQuad,
        pyautogui.easeInBounce,
        pyautogui.easeOutElastic
    ]
    tween = random.choice(funcoes_easing)

    # Move o mouse para a posição destino
    pyautogui.moveTo(destino_x, destino_y, duration=duracao, tween=tween)

    # Aguarda um tempo aleatório antes de clicar
    time.sleep(random.uniform(0.2, 0.6))

    # Realiza o clique
    pyautogui.click()
	
	
def icone_na_tela(icon_path, threshold=0.8):
    # Captura de tela
    screen = pyautogui.screenshot()
    screen = np.array(screen)
    screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)

    # Carrega o ícone de referência
    icon = cv2.imread(icon_path, 0)

    # Aplica a correspondência de template
    res = cv2.matchTemplate(screen, icon, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)

    # Verifica se há alguma correspondência
    return any(loc[0])



def verificarIcone(caminho_icone):


	# Carregue a imagem do ícone
	icone = cv2.imread(caminho_icone, cv2.IMREAD_UNCHANGED)

	# Capture a tela inteira
	screenshot = pyautogui.screenshot()

	# Converta a captura de tela para um array NumPy
	screenshot_np = np.array(screenshot)

	# Converta a captura de tela para o formato BGR (o padrão usado pelo OpenCV)
	screenshot_bgr = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2BGR)

	# Procure o ícone na tela
	resultado = cv2.matchTemplate(screenshot_bgr, icone, cv2.TM_CCOEFF_NORMED)

	# Defina um limiar de correspondência
	limiar = 0.9

	# Encontre as localizações onde a correspondência atende ao limiar
	loc = np.where(resultado >= limiar)

	# Verifique se o ícone foi encontrado

    

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True



time.sleep(2)

pyautogui.keyDown('win')
pyautogui.press('r')
pyautogui.keyUp('win')
pyautogui.typewrite("https://www.nfe.fazenda.gov.br/portal/principal.aspx", interval=0.00001)
pyautogui.keyDown('enter')
pyautogui.keyUp('enter')
pyautogui.click(x=981,y=23) #maximizar

def notas(qtdLoop=0):

    contador=0
    with open("C:\\Users\\leandro\\Desktop\\roboxml\\roboxml.csv") as f:
        next(f)

    
 
        for line in f:

            try:
                while not(icone_na_tela('C:\\Users\\leandro\\Desktop\\roboxml\\iconeOK.png')):	

                    time.sleep(0.5)

                    movimento_mouse_humano(random.randint(1,5))

                    print("Aguardando ativação anti-robo!")				

					
                    if icone_na_tela('C:\\Users\\leandro\\Desktop\\roboxml\\tela_entrada.png'):				
                        pyautogui.click(pyautogui.locateCenterOnScreen("C:\\Users\\leandro\\Desktop\\roboxml\\tela_entrada.png", confidence=0.8), duration=0.5)#botao continuar
                        movimento_humano(324,578)
				
                        time.sleep(0.5)					

            except:
                print("Erro imagem ICONEOK")
                pass
				
            if icone_na_tela('C:\\Users\\leandro\\Desktop\\roboxml\\iconeOK.png'):				
                pyautogui.click(x=519,y=429) #posição campo chave eletronica
				
			   # movimento_humano(519,429)#posição campo chave eletronica
                pyautogui.keyDown('ctrl')   #deletará chave digitada anteriormente
                pyautogui.press('a')  #deletará chave digitada anteriormente
                pyautogui.keyUp('ctrl')  #deletará chave digitada anteriormente
			


                line=line.strip()
                line=line.split(";")
                print("Dados: ", line)

                chaveteste= line[0]
                chaveteste=chaveteste[0:]   #elimando ' da string

				#pyautogui.typewrite(chaveteste, interval=0.05)  #darf codigo #alterado 05/01/2023
                pyautogui.typewrite(chaveteste, interval=0.001)  #darf codigo  #alterado 05/01/2023

			
            try:				
                while not(icone_na_tela('C:\\Users\\leandro\\Desktop\\roboxml\\download1.png')):			
                    time.sleep(0.5)
                    pyautogui.click(pyautogui.locateCenterOnScreen("C:\\Users\\leandro\\Desktop\\roboxml\\continuar.png", confidence=0.8), duration=0.5)#botao continuar

		
                    pyautogui.click(pyautogui.locateCenterOnScreen("C:\\Users\\leandro\\Desktop\\roboxml\\download1.png", confidence=0.8), duration=0.5)#botao continuar
            except:
                pass

            time.sleep(0.5) 

            try:
                pyautogui.click(pyautogui.locateCenterOnScreen("C:\\Users\\leandro\\Desktop\\roboxml\\ok.png", confidence=0.8), duration=0.5)
                pyautogui.click(pyautogui.locateCenterOnScreen("C:\\Users\\leandro\\Desktop\\roboxml\\ok.png", confidence=0.8), duration=0.5)
                pyautogui.click(pyautogui.locateCenterOnScreen("C:\\Users\\leandro\\Desktop\\roboxml\\ok.png", confidence=0.8), duration=0.5)
            except:
                pass
            

            try:
                time.sleep(1) 
                pyautogui.click(pyautogui.locateCenterOnScreen("C:\\Users\\leandro\\Desktop\\roboxml\\VOLTAR.png", confidence=0.8), duration=0.5)                
                time.sleep(0.5)
            except:
                pass

notas(0)

