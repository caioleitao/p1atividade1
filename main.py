from datetime import datetime
from time import sleep
import msvcrt
import os

n1 = 0
n2 = 0
n3 = 0
resultado = 0
escolha = 0

def iniciar():
    global escolha
    print("=" * 26, "\n* Selecione a atividade: * \n", "=" * 24, "\n Selecione o numero corresponde ao algoritmo desejado\n 1: Atividade 1\n 2: Atividade 2\n 3: Atividade 3\n 4: Atividade 4")
    escolha = input()
    calcular()

def aguarde():
    print("\nDigite enter para reiniciar o programa")
    while not msvcrt.kbhit():
        pass
    msvcrt.getch()
    print("\n\n\n\nReiniciando o programa, aguarde...\n\n\n")
    sleep(2)
    os.system('cls')

def calcular():
    global n1, n2, n3, resultado
    match escolha:
        case '0':
            print("Nenhuma opção foi selecionada.")
        case '1':
            n1,n2,n3,resultado = 0, 0, 0, 0
            n1 = float(input("Digite o primeiro numero: "))
            n2 = float(input("Digite o segundo numero: "))
            n3 = float(input("Digite o terceiro numero: "))

            resultado = n1 / (n2 / n3)

            print("O resultado é: ", resultado)

            sleep(3)
            aguarde()

            iniciar()

        case '2':
            n1,n2,n3,resultado = 0, 0, 0, 0
            n1 = float(input("Digite o primeiro numero: "))
            n2 = float(input("Digite o segundo numero: "))
            n3 = float(input("Digite o terceiro numero: "))

            resultado = (n1 % n2) 
            if resultado > n3:
                print("O resultado é maior")
            else: 
                print("O resultado é menor")

            sleep(3)
            aguarde()

            iniciar()

        case '3':
            n1,n2,n3,resultado = 0, 0, 0, 0
            n1 = int(input("Digite o valor de A: "))
            n2 = int(input("Digite o valor de B: "))
            n3 = int(input("Digite o valor de C: "))

            resultado = n2 ** 2 - 4 * n1 * n3

            print("O delta é ", resultado)

            sleep(3)
            aguarde()

            iniciar()

        case '4':
            n1,n2,n3,resultado = 0, 0, 0, 0

            n1 = datetime.now().year
            n2 = int(input("Digite o ano que você nasceu: "))
            n3 = n1 - n2

            if n3 > 110:
                print("Você não está mais vivo")
            elif n3 < 110 and n3 >= 0:
                print("\nVocê tem ", n3, " anos")
            else:
                print("Você está preste a nascer")

            sleep(3)
            aguarde()

            iniciar()

iniciar()
