import math
from math import cos, radians

def velocidade_media():
    while True:
        try: 
            #title(Calculadora de Velocidade Média)
            print("\nAperte Ctrl+C para sair.\n")

            distancia = float(input("Digite a distância percorrida (em km): "))
            tempo = float(input("Digite o tempo gasto (em minutos): ")) / 60  # Convertendo minutos para horas
                    
            if tempo <= 0:
                print("O tempo gasto tem que ser positivo.")
            else:
                velocidade_media = distancia / tempo
                
                #limpa()

                #title(A velocidade média é: {velocidade_media:.2f} km/h)
        
        except ValueError:
            print("Por favor, digite valores numéricos válidos.")
        except KeyboardInterrupt:
            #limpa()
            print("\nPrograma interrompido pelo usuário.")
            break

def calculando_movimento_uniforme():
    while True:
        try:
            #title(Calculadora de Movimento Uniforme)
            print("\nAperte Ctrl+C para sair.\n")

            posicao_inicial = float(input("Digite a posição inicial (em metros): "))
            velocidade = float(input("Digite a velocidade (em m/s): ")) 
            tempo = float(input("Digite o tempo (em segundos): "))
            
            if tempo < 0:
                print("Digite valores positivos para tempo.")  

            else:
                posicao_final = posicao_inicial + velocidade * tempo

                #limpa()
                #title(A posição final é: {posicao_final:.2f} metros)

        except ValueError:
            print("Por favor, digite valores numéricos válidos.")

        except KeyboardInterrupt:
            #limpa()
            print("\nPrograma interrompido pelo usuário.")
            break 

def aceleracao_media():
    while True:
        try:
            #title(Calculadora de Aceleração Média)
            print("\nAperte Ctrl+C para sair.\n")

            velocidade_inicial = float(input("Digite a velocidade inicial (em m/s): "))
            velocidade_final = float(input("Digite a velocidade final (em m/s): "))
            tempo = float(input("Digite o tempo (em segundos): "))

            if tempo <= 0:
                print("O tempo deve ser maior que zero.")
            
            else:
                aceleracao_media = (velocidade_final - velocidade_inicial) / tempo

                #limpa()
                #title(A aceleração média é: {aceleracao:.2f} m/s²)

        except ValueError:
            print("Por favor, digite valores numéricos válidos.")

        except KeyboardInterrupt:
            #limpa()
            print("\nPrograma interrompido pelo usuário.")
            break

def calculando_movimento_uniformemente_acelerado():
    while True:
        try:
            #title(Calculadora de Movimento Uniformemente Acelerado)
            print("\nAperte Ctrl+C para sair.\n")

            posicao_inicial = float(input("Digite a posição inicial (em metros): "))
            velocidade_inicial = float(input("Digite a velocidade inicial (em m/s): "))
            aceleracao = float(input("Digite a aceleração (em m/s²): "))
            tempo = float(input("Digite o tempo (em segundos): "))
            
            if tempo < 0:
                print("O tempo deve ser maior ou igual a zero.")
            else:
                posicao_final = posicao_inicial + velocidade_inicial * tempo + (aceleracao * tempo ** 2) / 2

                #limpa()
                #title(A posição final é: {posicao_final:.2f} metros)
        except ValueError:
            print("Por favor, digite valores numéricos válidos.")       
        except KeyboardInterrupt:
            #limpa()
            print("\nPrograma interrompido pelo usuário.")
            break

def calculando_equacao_torricelli():
    while True:
        try:
            #title(Calculadora de Equação de Torricelli)
            print("\nAperte Ctrl+C para sair.\n")

            velocidade_inicial = float(input("Digite a velocidade inicial (em m/s): "))
            aceleracao = float(input("Digite a aceleração (em m/s²): "))
            deslocamento = float(input("Digite o deslocamento (em metros): "))

            velocidade_final = (velocidade_inicial ** 2 + 2 * aceleracao * deslocamento) ** 0.5

            #limpa()
            #title(A velocidade final é: {velocidade_final:.2f} m/s)

        except ValueError:
            print("Por favor, digite valores numéricos válidos.")
        except KeyboardInterrupt:
            #limpa()
            print("\nPrograma interrompido pelo usuário.")
            break

def segunda_lei_newton():
    while True:
        try:
            #title(Calculadora da Segunda Lei de Newton)
            print("\nAperte Ctrl+C para sair.\n")
            
            massa = float(input("Digite a massa do objeto (em kg): "))
            forca = float(input("Digite a força aplicada (em N): "))

            if massa <= 0:
                print("A massa deve ser maior que zero.")
            else:
                aceleracao = forca / massa

                #limpa()
                #title(A aceleração é: {aceleracao:.2f} m/s²)

        except ValueError:
            print("Por favor, digite valores numéricos válidos.")
        except KeyboardInterrupt:
            #limpa()
            print("\nPrograma interrompido pelo usuário.")
            break

def forca_peso():
    while True:
        try:
            #title(Calculadora da Força Peso)
            print("\nAperte Ctrl+C para sair.\n")

            massa = float(input("Digite a massa do objeto (em kg): "))
            gravidade = float(input("Digite a aceleração da gravidade (em m/s²): "))

            if massa <= 0:
                print("A massa deve ser maior que zero.")
            else:
                peso = massa * gravidade

                #limpa()
                #title(O peso do objeto é: {peso:.2f} N)

        except ValueError:
            print("Por favor, digite valores numéricos válidos.")
        except KeyboardInterrupt:
            #limpa()
            print("\nPrograma interrompido pelo usuário.")
            break

def energia_cinetica():
    while True:
        try:
            #title(Calculadora de Energia Cinética)
            print("\nAperte Ctrl+C para sair.\n")

            massa = float(input("Digite a massa do objeto (em kg): "))
            velocidade = float(input("Digite a velocidade do objeto (em m/s): "))

            if massa <= 0:
                print("A massa deve ser maior que zero.")
            else:
                energia_cinetica = (massa * velocidade ** 2) / 2

                #limpa()
                #title(A energia cinética do objeto é: {energia:.2f} J)

        except ValueError:
            print("Por favor, digite valores numéricos válidos.")
        except KeyboardInterrupt:
            #limpa()
            print("\nPrograma interrompido pelo usuário.")
            break

def energia_potencial():
    while True:
        try:
            #title(Calculadora de Energia Potencial)
            print("\nAperte Ctrl+C para sair.\n")

            massa = float(input("Digite a massa do objeto (em kg): "))
            altura = float(input("Digite a altura do objeto (em metros): "))
            gravidade = float(input("Digite a aceleração da gravidade (em m/s²): "))

            if massa <= 0:
                print("A massa deve ser maior que zero.")
            else:
                energia_potencial = massa * gravidade * altura

                #limpa()
                #title(A energia potencial do objeto é: {energia:.2f} J)

        except ValueError:
            print("Por favor, digite valores numéricos válidos.")
        except KeyboardInterrupt:
            #limpa()
            print("\nPrograma interrompido pelo usuário.")
            break

def trabalho():
    while True:
        try:
            #title(Calculadora de Trabalho)
            print("\nAperte Ctrl+C para sair.\n")
            
            forca = float(input("Digite a força aplicada (em N): "))
            deslocamento = float(input("Digite o deslocamento (em metros): "))
            angulo = float(input("Digite o ângulo entre a força e o deslocamento (em graus): "))

            trabalho = forca * deslocamento * cos(radians(angulo))

            #limpa()
            #title(O trabalho realizado é: {trabalho:.2f} J)

        except ValueError:
            print("Por favor, digite valores numéricos válidos.")
        except KeyboardInterrupt:
            #limpa()
            print("\nPrograma interrompido pelo usuário.")
            break