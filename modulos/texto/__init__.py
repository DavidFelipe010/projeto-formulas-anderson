import os

def limpa_terminal() -> none:
    os.system('cls' if os.name == 'nt' else 'clear')


def titulo(txt: str) -> none:
    texto = txt.strip()
    linha = '=' * (len(texto) + 16)

    print(f'''{linha}
        {texto.title()}
{linha}''')


def menu() -> none:
    print(f'''[0] - Sair
[1] - Velocidade Média
[2] - Movimeto uniforme
[3] - Aceleração Média
[4] - Movimento Uniformemente Variado
[5] - Equação de Torricelli
[6] - Segunda Lei de Newton
[7] - Força Peso
[8] - Energia Cinética
[9] - Energia Potencial Gravitacional
[10] - Trabalho de uma Força''')
