import math
from modulos.verificadores import verifica_int, verifica_float, verifica_numero_positivo
from modulos.texto import limpa_terminal, titulo, linha
from math import cos, radians


def velocidade_media():
   
    limpa_terminal()
    
    titulo("Calculadora de Velocidade Média")
    
    distancia = verifica_numero_positivo("Digite a distância percorrida (em km): ")
    tempo = verifica_numero_positivo("Digite o tempo gasto (em minutos): ") / 60  # Convertendo minutos para horas
    velocidade_media = distancia / tempo
    
    limpa_terminal()
    
    titulo("Resultado")
    
    linha()
    print(f"""Dados:
- Distância: {distancia:.2f} km
- Tempo: {tempo:.2f} horas 
- A velocidade média é: {velocidade_media:.2f} km/h""")
    linha()

    input("\nPressione Enter para continuar...")


def calculando_movimento_uniforme():

    limpa_terminal()

    titulo("Calculadora de Movimento Uniforme")
    
    posicao_inicial = verifica_float("Digite a posição inicial (em metros): ")
    velocidade = verifica_float("Digite a velocidade (em m/s): ")
    tempo = verifica_numero_positivo("Digite o tempo (em segundos): ")
    posicao_final = posicao_inicial + velocidade * tempo
    
    limpa_terminal()
    
    titulo("Resultado")
    
    linha()
    print(f"""Dados:
- Posição inicial: {posicao_inicial:.2f} metros
- Velocidade: {velocidade:.2f} m/s
- Tempo: {tempo:.2f} segundos
- A posição final é: {posicao_final:.2f} metros""")
    linha()

    input("\nPressione Enter para continuar...")


def aceleracao_media():
    
    limpa_terminal()
    
    titulo("Calculadora de Aceleração Média")
    
    velocidade_inicial = verifica_float("Digite a velocidade inicial (em m/s): ")
    velocidade_final = verifica_float("Digite a velocidade final (em m/s): ")
    tempo = verifica_numero_positivo("Digite o tempo (em segundos): ")
    aceleracao_media = (velocidade_final - velocidade_inicial) / tempo
    
    limpa_terminal()

    titulo("Resultado")

    linha()
    print(f"""Dados:
- Velocidade inicial: {velocidade_inicial:.2f} m/s
- Velocidade final: {velocidade_final:.2f} m/s
- Tempo: {tempo:.2f} segundos
- A aceleração média é: {aceleracao_media:.2f} m/s²""")
    linha()

    input("\nPressione Enter para continuar...")


def calculando_movimento_uniformemente_variado():
    
    limpa_terminal()

    titulo("Calculadora de Movimento Uniformemente Variado")
    
    posicao_inicial = verifica_float("Digite a posição inicial (em metros): ")
    velocidade_inicial = verifica_float("Digite a velocidade inicial (em m/s): ")
    aceleracao = verifica_float("Digite a aceleração (em m/s²): ")
    tempo = verifica_numero_positivo("Digite o tempo (em segundos): ")
    posicao_final = posicao_inicial + velocidade_inicial * tempo + (aceleracao * tempo ** 2) / 2

    limpa_terminal()

    titulo("Resultado")

    linha()
    print(f"""Dados:
- Posição inicial: {posicao_inicial:.2f} metros
- Velocidade inicial: {velocidade_inicial:.2f} m/s
- Aceleração: {aceleracao:.2f} m/s²
- Tempo: {tempo:.2f} segundos
- A posição final é: {posicao_final:.2f} metros""")
    linha()

    input("\nPressione Enter para continuar...")
    

def calculando_equacao_torricelli():
    
    limpa_terminal()
    titulo("Calculadora de Equação de Torricelli")

    velocidade_inicial = verifica_float("Digite a velocidade inicial (em m/s): ")
    aceleracao = verifica_float("Digite a aceleração (em m/s²): ")
    deslocamento = verifica_float("Digite o deslocamento (em metros): ")
    velocidade_final = (velocidade_inicial ** 2 + 2 * aceleracao * deslocamento) ** 0.5

    limpa_terminal()

    titulo("Resultado")

    linha()
    print(f"""Dados:
- Velocidade inicial: {velocidade_inicial:.2f} m/s
- Aceleração: {aceleracao:.2f} m/s²
- Deslocamento: {deslocamento:.2f} metros
- A velocidade final é: {velocidade_final:.2f} m/s""")
    linha()

    input("\nPressione Enter para continuar...")


def segunda_lei_newton():

    limpa_terminal()
    titulo("Calculadora da Segunda Lei de Newton")
    
    massa = verifica_numero_positivo("Digite a massa do objeto (em kg): ")
    aceleracao = verifica_float("Digite a aceleração (em m/s²): ")
    forca = massa * aceleracao

    limpa_terminal()

    titulo("Resultado")

    linha()
    print(f"""Dados:
- Massa: {massa:.2f} kg
- Aceleração: {aceleracao:.2f} m/s²
- A força é: {forca:.2f} N""")
    linha()

    input("\nPressione Enter para continuar...")

    
def forca_peso():
    
    limpa_terminal()
    titulo("Calculadora da Força Peso")

    massa = verifica_numero_positivo("Digite a massa do objeto (em kg): ")
    gravidade = verifica_float("Digite a aceleração da gravidade (em m/s²): ")
    peso = massa * gravidade

    limpa_terminal()

    titulo("Resultado")

    linha()
    print(f"""Dados:
- Massa: {massa:.2f} kg
- Aceleração da gravidade: {gravidade:.2f} m/s²
- A força peso é: {peso:.2f} N""")
    linha()

    input("\nPressione Enter para continuar...")


def energia_cinetica():
    
    limpa_terminal()
    titulo("Calculadora de Energia Cinética")
    
    massa = verifica_numero_positivo("Digite a massa do objeto (em kg): ")
    velocidade = verifica_float("Digite a velocidade do objeto (em m/s): ")
    energia_cinetica = (massa * velocidade ** 2) / 2

    limpa_terminal()
    titulo("Resultado")

    linha()
    print(f"""Dados:
- Massa: {massa:.2f} kg
- Velocidade: {velocidade:.2f} m/s
- A energia cinética é: {energia_cinetica:.2f} J""")
    linha()

    input("\nPressione Enter para continuar...")


def energia_potencial():
            
    limpa_terminal()
    titulo("Calculadora de Energia Potencial")

    massa = verifica_numero_positivo("Digite a massa do objeto (em kg): ")
    altura = verifica_float("Digite a altura do objeto (em metros): ")
    gravidade = verifica_float("Digite a aceleração da gravidade (em m/s²): ")
    energia_potencial = massa * gravidade * altura
    
    limpa_terminal()

    titulo("Resultado")

    linha()
    print(f"""Dados:
- Massa: {massa:.2f} kg
- Altura: {altura:.2f} metros
- Aceleração da gravidade: {gravidade:.2f} m/s²
- A energia potencial é: {energia_potencial:.2f} J""")
    linha()

    input("\nPressione Enter para continuar...")
    
def job():
            
    limpa_terminal()
    titulo("Calculadora de Trabalho")

    forca = verifica_float("Digite a força aplicada (em N): ")
    deslocamento = verifica_float("Digite o deslocamento (em metros): ")
    angulo = verifica_float("Digite o ângulo entre a força e o deslocamento (em graus): ")
    trabalho = forca * deslocamento * cos(radians(angulo))
   
    limpa_terminal()

    titulo("Resultado")

    linha()
    print(f"""Dados:
- Força: {forca:.2f} N
- Deslocamento: {deslocamento:.2f} metros
- Ângulo: {angulo:.2f} graus
- O trabalho realizado é: {trabalho:.2f} J""")
    linha()

    input("\nPressione Enter para continuar...")