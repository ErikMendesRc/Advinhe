from randomize import Randomize


def Main():
    print("Olá, digite um intervalo de números para eu escolher um.")

    initNumber = int(input("Primeiro Número: "))
    finalNumber = int(input("Último Número: "))

    randomize = Randomize(initNumber, finalNumber)
    savedNumber = randomize.randomize()

    print("Agora já escolhi meu número, que tal tentar advinhar ? ")

    while True:
        what_number = int(input("Digite um número para adivinhar: "))

        if what_number < savedNumber:
            print("É Mais :D")
        elif what_number > savedNumber:
            print("É Menos")
        else:
            print("Exato! Você acertou o número que escolhi.")
            break  # Sai do loop quando o número é acertado

        print("Você errou, tente novamente")


if __name__ == '__main__':
    Main()
