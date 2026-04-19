def verifica_int(txt) -> int:
    '''
    Função para verificar se o valor é inteiro
    :txt: Texto que será mostrado no input
    :return: int
    '''

    while True:
        label = input(txt).strip()

        try:
            num = int(label)
            return num

        except (ValueError, TypeError):
            print('\033[31m[ERROR] Valor inválido! Digite apenas números inteiros.\n \033[m')


def verifica_float(txt) -> float:
    '''
    Função para verificar se o valor é decimal
    :txt: Texto que será mostrado no input
    :return: float
    '''

    while True:
        label = input(txt).strip().replace(',', '.')

        try:
            num = float(label)
            return num

        except (ValueError, TypeError):
            print('\033[31m[ERROR] Valor inválido! Digite apenas números.\n \033[m')

def verifica_numero_positivo(txt) -> float:
    '''
    Função para verificar se o valor é decimal
    :txt: Texto que será mostrado no input
    :return: float
    '''

    while True:
        label = input(txt).strip().replace(',', '.')

        try:
            num = float(label)
            
            if num < 0:
                print('\033[31m[ERROR] Valor inválido! Digite um número positivo.\n \033[m')
                continue
            return num

        except (ValueError, TypeError):
            print('\033[31m[ERROR] Valor inválido! Digite apenas números.\n \033[m')
