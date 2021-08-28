from classes import Loja, Cliente
from datetime import datetime, timedelta


def main():
    novaLoja = Loja(100)
    novoCliente = Cliente(0, 0, 0)

    while True:
        print("""
        |----| D.L.M | ALUGUEL DE BICICLETAS |----|
        1. Exibir bicicletas disponíveis
        2. Alugar bicicleta(s)
        3. Devolver bicicleta(s)
        4. Sair
        """)

        opcao = input("Escolha uma das opções acima: ")

        try:
            opcao = int(opcao)
        except ValueError:
            print("Opção Inválida!\nA opção deve ser um número inteiro positivo.")
            continue

        if opcao == 1:
            novaLoja.mostrarEstoque()
        elif opcao == 2:
            qtBikes, tipoLocacao, horaLocacao = novoCliente.alugaBike(
                0, 0, novaLoja)
            print("Obrigado por alugar com a DLM!")
        elif opcao == 3:
            novaLoja.calcularConta(horaLocacao, tipoLocacao, qtBikes)
        elif opcao == 4:
            break
        else:
            print("Opção inválida!\nFavor digitar um número de 1 a 4.")
    print("Obrigado por alugar com a DLM!")


if __name__ == "__main__":
    main()
