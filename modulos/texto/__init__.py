import os

def limpa_terminal() -> none:
    os.system('cls' if os.name == 'nt' else 'clear')


def titulo(txt: str) -> none:
    texto = txt.strip()
    linha = '=' * (len(texto) + 16)

    print(f'''{linha}
        {texto.title()}
{linha}''')

