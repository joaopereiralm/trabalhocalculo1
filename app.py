from fractions import Fraction


while True:
    print("-----------")
    print(" Frações ")
    print("-----------")
    print("\nPrimeira fração")
    n1 = int(input("Digite o 1° número da fração: (número de cima)"))
    n2 = int(input("Digite o 2° número da fração: (número de baixo)"))
    if n1 == 0 or n2 == 0:
        print("\nEntrada inválida! O número 0 não é permitido nesta aplicação. Encerrando...")
        break
    print("\nSegunda fração")
    n3 = int(input("Digite o número 1° número da fração 2: (número de cima)"))
    n4 = int(input("Digite o 2° númerod a fração 2: (número de baixo)"))
    if n3 == 0 or n4 == 0:
        print("\nEntrada inválida! O número 0 não é permitido nesta aplicação. Encerrando...")
        break

    fracao1 = Fraction(n1, n2)
    fracao2 = Fraction(n3, n4)

    print("\nFração 1: ", n1, " / ", n2)
    print("Fração 2: ", n3, " / ", n4)
    print("\nVocê deseja quais das opções: ")
    print("1 - Multiplicar")
    print("2 - Dividir")
    print("3 - Subtrair")
    print("4 - Somar")
    print("0 - Sair")
    
    op = int(input("\nDigite o número: "))

    if op == 0:
        print("Programa encerrado :)")
        break

    else:
        match op:
            case 1:
                print("\n----------------")
                print(" Multiplicação ")
                print("----------------")

                multiplica = fracao1 * fracao2

                print("Valor da multiplicação: ", fracao1, "x", fracao2, ":", multiplica)
                
            case 2:
                print("\n-----------")
                print("  Divisão ")
                print("-----------")
            

                divisao = fracao1 / fracao2

                print("Valor da divisão: ", fracao1, "/", fracao2, ":", divisao)

            case 3:
                print("\n--------------")
                print("  Subtração ")
                print("----------------")

                subtr = fracao1 - fracao2

                print("Valor da subtração: ", fracao1, "-", fracao2, ":", subtr)

            case 4:
                print("\n----------")
                print("  Soma ")
                print("----------")

                soma = fracao1 + fracao2

                print("Valor da soma: ", fracao1, "+", fracao2, ":", soma)

        print("\nDeseja efetuar uma nova conta?")
        continua = input("S == Sim / N == Não: ").upper()

        if continua != "S" :
            print("Programa encerrado :)")
            break 