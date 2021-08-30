from datetime import datetime, timedelta

# Criação da Classe/Objeto "LOJA":


class Loja(object):
    def __init__(self, estoque=0):
        """
        Construtor da classe, instância a Loja de Bicicletas.
        """
        self.estoque = estoque

    # Mostrar o estoque de bicicletas:

    def mostrarEstoque(self):
        """
        Mostra o estoque de bicicletas disponíveis para locação.
        """
        print(
            f"No momento, temos {self.estoque} bicicletas disponíveis para locação.")
        return self.estoque

    # Receber pedidos de aluguéis por hora, diários ou semanais validando
    # a possibilidade com o estoque:

    # Locação por hora:
    def locacaoHora(self, qtBikes):
        """
        Locação de bicicleta(s) por hora ao Cliente.
        """
        # Caso seja informado um número negativo de bicicletas:
        if qtBikes <= 0:
            print("A quantidade de bicicletas para locação deve ser um número positivo!")
            return None
        # Verificação de bicicletas solicitadas versus estoque atual:
        elif qtBikes > self.estoque:
            print(f"Desculpe! Você solicitou {qtBikes} bicicleta(s), mas no momento temos apenas {self.estoque} bicicleta(s) disponível(eis) em estoque.")
            return None
        # Havendo estoque, exibe as informações da locação para o Cliente na tela e
        # retorna a hora atual para posterior cálculo do valor a ser pago:
        else:
            horaLocacao = datetime.now()
            print(f"Olá!\nVocê solicitou o aluguel de {qtBikes} bicicleta(s), às {horaLocacao} de hoje.\nO valor para locação por hora é de R$ 5,00 por hora, por bicicleta.")
            self.estoque -= qtBikes
            return horaLocacao

    # Locação por dia:
    def locacaoDia(self, qtBikes):
        """
        Locação de bicicleta(s) por dia ao Cliente.
        """
        if qtBikes <= 0:
            print("A quantidade de bicicletas para locação deve ser um número positivo!")
            return None
        elif qtBikes > self.estoque:
            print(f"Desculpe! Você solicitou {qtBikes} bicicleta(s), mas no momento temos apenas {self.estoque} bicicleta(s) disponível(eis) em estoque.")
            return None
        else:
            horaLocacao = datetime.now()
            print(f"Olá!\nVocê solicitou o aluguel de {qtBikes} bicicleta(s), às {horaLocacao} de hoje.\nO valor para locação por dia é de R$ 25,00 por dia, por bicicleta.")
            self.estoque -= qtBikes
            return horaLocacao

    # Locação por semana:
    def locacaoSemana(self, qtBikes):
        """
        Locação de bicicleta(s) por semana ao Cliente.
        """
        if qtBikes <= 0:
            print("A quantidade de bicicletas para locação deve ser um número positivo!")
            return None
        elif qtBikes > self.estoque:
            print(f"Desculpe! Você solicitou {qtBikes} bicicleta(s), mas no momento temos apenas {self.estoque} bicicleta(s) disponível(eis) em estoque.")
            return None
        else:
            horaLocacao = datetime.now()
            print(f"Olá!\nVocê solicitou o aluguel de {qtBikes} bicicleta(s), às {horaLocacao} de hoje.\nO valor para locação semanal é de R$ 100,00 por semana, por bicicleta.")
            self.estoque -= qtBikes
            return horaLocacao

    # Locação familiar:
    def locacaoFamilia(self, qtBikes):
        """
        Locação de bicicleta(s) sob a Promoção Família ao Cliente. Aplica um desconto de
        30% ao valor total da locação para 3 a 5 empréstimos de qualquer tipo.
        """
        # Verifica se é possível aplicar a Promoção Família:
        if not(3 <= qtBikes <= 5):
            print(f"Desconto da 'Promoção Família' não aplicável.\nAgradecemos a preferência e volte sempre.")
            return False
        # Caso positivo, informa a aplicação do desconto e retorna um booleano para
        # verificação posterior no momento do pagamento:
        else:
            print(f"Você receberá o desconto da 'Promoção Família' e terá 30% (trinta por cento) de desconto sobre o valor total final da locação.\nAgradecemos a preferência e volte sempre.")
            return True

    # Calcular a conta quando o cliente decide devolver a bicicleta:
    def calcularConta(self, horaLocacao, tipoLocacao, qtBikes, objCliente, objLoja):
        """
        Método para calcular a conta a ser paga pelo cliente e atualizar o estoque. Deverá
        ser alimentada a partir de argumentos do método 'alugaBike' do objeto Cliente.
        Deverá retornar o valor da conta.
        """
        conta = 0

        # Caso esteja tudo de acordo com os valores recebidos do método alugaBike:
        if horaLocacao and tipoLocacao and qtBikes:
            self.estoque += qtBikes
            horaAtual = datetime.now()
            tempoLocacao = horaAtual - horaLocacao
            # Locação por hora:
            if tipoLocacao == 1:
                conta = round(tempoLocacao.seconds / 3600) * 5 * qtBikes
            # Locação por dia:
            elif tipoLocacao == 2:
                conta = round(tempoLocacao.days) * 25 * qtBikes
            # Locação por semana:
            else:  # tipoLocacao == 3:
                conta = round(tempoLocacao.days / 7) * 100 * qtBikes

            # Verificação do desconto família:
            if objLoja.locacaoFamilia(objCliente.qtBikes) == True:
                conta = conta * (0.7)
            else:
                objLoja.locacaoFamilia(objCliente.qtBikes)

            # Imprime uma mensagem de agradecimento ao Cliente e retorna o valor total
            # devido (conta):
            print(f"Obrigado por devolver a(s) bicicleta(s)! \nO valor total da sua locação é de: R$ {conta}.")
            return conta
       # Caso haja algum problema com os valores recebidos do método alugaBike:
        else:
            print("Locação não encontrada no sistema.")
            return None

# Criação da Classe/Objeto "CLIENTE":


class Cliente(object):
    def __init__(self, qtBikes, tipoLocacao, horaLocacao):
        """
        Construtor da classe, instancia o Cliente da Loja.
        """
        self.qtBikes = qtBikes
        self.tipoLocacao = tipoLocacao
        self.horaLocacao = horaLocacao

    # Métodos:
    # Ver as bicicletas disponíveis na Loja:
    def verEstoque(self, objLoja):
        return print(f"O estoque disponível é de {objLoja.estoque} bicicleta(s)")

    # Alugar bicicletas, sob as diferentes modalidades:
    def alugaBike(self, qtBikes, tipoLocacao, objLoja):
        """
        Realiza o pedido de locação de bicicletas, conforme quantidade e 
        modalidade escolhidas pelo Cliente.
        Retorna os dados: qtBikes, tipoLocacao e horaLocacao, que serão
        utilizados para calcular o valor devido.
        """

        qtBikes = input("Quantas bicicletas gostaria de alugar? ")
        try:
            qtBikes = int(qtBikes)
        except ValueError:
            print(
                "A quantidade de bicicletas para locação deve ser um número inteiro positivo!")
            return -1

        if qtBikes < 1:
            print("Entrada inválida.\nA quantidade de bicicletas para locação deve ser maior do que zero!")
            return -1
        else:
            self.qtBikes = qtBikes

        tipoLocacao = 0
        while tipoLocacao == 0:
            tipoLocacao = input("Qual o tipo de locação que deseja?\n(Digite o número)\n1 - Locação por hora (R$ 5,00/hora); \n2 - Locação por dia (R$ 25,00/dia); \n3 - Locação por semana (R$ 100,00/semana).\n")
            try:
                tipoLocacao = int(tipoLocacao)
            except ValueError:
                print("O tipo de locação deve ser um número inteiro positivo!")
                return -1

        while tipoLocacao not in [1, 2, 3]:
            print("Entrada inválida.\nFavor escolher entre as opções 1, 2 ou 3, acima.")
            tipoLocacao = 0

        if tipoLocacao == 1:
            self.horaLocacao = objLoja.locacaoHora(self.qtBikes)
            self.tipoLocacao = 1
        elif tipoLocacao == 2:
            self.horaLocacao = objLoja.locacaoDia(self.qtBikes)
            self.tipoLocacao = 2
        else:
            self.horaLocacao = objLoja.locacaoSemana(self.qtBikes)
            self.tipoLocacao = 3

        return self.qtBikes, self.tipoLocacao, self.horaLocacao