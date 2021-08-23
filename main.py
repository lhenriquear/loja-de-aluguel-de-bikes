from classes import Loja, Cliente

def main():
    loja = Loja(100)
    cliente = Cliente()

while True:
    print("""
    |----| DLM | ALUGUEL DE BICICLETAS |----|
    1. Exibir bicicletas disponíveis
    2. Alugar bicicleta(s)
    3. Devolver bicicleta(s)
    4. Sair
    """)

    opcao = input("Escolha uma das opções acima: ")

    try:
        opcao = int(opcao)
    except ValueError:
        print("Opção inválida!\nA opção deve ser um número inteiro positivo.")
        continue

    if opcao == 1:
        loja.mostrarEstoque()
    elif opcao == 2:
        cliente.alugaBike()
        print("Obrigado por alugar com a DLM!")
    elif opcao == 3:
        loja.calcularConta(cliente.alugaBike())
    elif opcao == 4:
        break
    else:
        print("Opção inválida!\nFavor digitar um número de 1 a 4.")
print("Obrigado por alugar com a DLM!")

if __name__ == "__main__":
    main()