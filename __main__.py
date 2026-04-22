'''
Turma: 2º DSA
Alunos: Cauã Cavalcanti, Caio Henrique, David Felipe, Guilherme Fernando, Giovana Hadassa, Henrique Eronildo, Neandro Felipe, Rohan Anthunes
'''

from modulos.formulas import velocidade_media, calculando_movimento_uniforme, aceleracao_media, calculando_movimento_uniformemente_variado, calculando_equacao_torricelli, segunda_lei_newton, forca_peso, energia_cinetica, energia_potencial, job
from modulos.texto import limpa_terminal, titulo, menu
from modulos.verificadores import verifica_int

def main():
    while True:
        
        limpa_terminal()

        titulo("Calculadora de Fórmulas de Física")

        menu()
        esc = verifica_int("\nDigite o número da fórmula que deseja calcular: ")
        
        match esc:
            case 0:
                limpa_terminal()
                print("\nSaindo do programa...")
                break
            case 1:
                velocidade_media()
            case 2:
                calculando_movimento_uniforme()
            case 3:
                aceleracao_media()
            case 4:
                calculando_movimento_uniformemente_variado()
            case 5:
                calculando_equacao_torricelli()
            case 6:
                segunda_lei_newton()
            case 7:
                forca_peso()
            case 8:
                energia_cinetica()  
            case 9:
                energia_potencial()
            case 10:
                job()
            case _:
                limpa_terminal()
                print("\nOpção inválida! Digite um número entre 0 e 10.")
                input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    main()
