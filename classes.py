from datetime import datetime

# Criação da Classe/Objeto "LOJA":
class Loja(object):
    def __init__(self, estoque = 0):
        """
        Construtor da classe, instancia a Loja de Bicicletas.
        """
        self.estoque = estoque

    # Métodos:
    
    ## Mostrar o estoque de bicicletas:
    def mostrarEstoque(self):
        """
        Mostra o estoque de bicicletas disponíveis para locação.
        """
        print(f"No momento, temos {self.estoque} bicicletas disponíveis para locação.")
        return self.estoque
    
    
    ## Receber pedidos de aluguéis por hora, diários ou semanais validando
    ## a possibilidade com o estoque: 
    
    ### Locação por hora:
    def locacaoHora(self, qtBikes):
        """
        Locação de bicicleta(s) por hora ao Cliente.
        """
        ### Caso seja informado um número negativo de bicicletas:
        if qtBikes <= 0:
            print("A quantidade de bicicletas para locação deve ser um número positivo!")
            return None
        ### Verificação de bicicletas solicitadas versus estoque atual:
        elif qtBikes > self.estoque:
            print(f"Desculpe! Você solicitou {qtBikes} bicicleta(s), mas no momento temos \
                apenas {self.estoque} bicicleta(s) disponível(eis) em estoque.")
            return None
        ### Havendo estoque, exibe as informações da locação para o Cliente na tela e
        ### retorna a hora atual para posterior cálculo do valor a ser pago:
        else:
            horaLocacao = datetime.datetime.now()
            print(f"Olá!\nVocê solicitou o aluguel de {qtBikes} bicicleta(s), às \
                {horaLocacao} de hoje.\n O valor para locação por hora é de R$ 5,00 \
                por hora, por bicicleta.\nAgradecemos a preferência e volte sempre!")
            self.estoque -= qtBikes
            return horaLocacao
    
    ### Locação por dia:
    def locacaoDia(self, qtBikes):
        """
        Locação de bicicleta(s) por dia ao Cliente.
        """
        if qtBikes <= 0:
            print("A quantidade de bicicletas para locação deve ser um número positivo!")
            return None
        elif qtBikes > self.estoque:
            print(f"Desculpe! Você solicitou {qtBikes} bicicleta(s), mas no momento temos \
                apenas {self.estoque} bicicleta(s) disponível(eis) em estoque.")
            return None
        else:
            horaLocacao = datetime.datetime.now()
            print(f"Olá!\nVocê solicitou o aluguel de {qtBikes} bicicleta(s), às \
                {horaLocacao} de hoje.\n O valor para locação diária é de R$ 25,00 \
                por dia, por bicicleta.\nAgradecemos a preferência e volte sempre!")
            self.estoque -= qtBikes
            return horaLocacao
    
    ### Locação por semana:
    def locacaoSemanal(self, qtBikes):
        """
        Locação de bicicleta(s) por semana ao Cliente.
        """
        if qtBikes <= 0:
            print("A quantidade de bicicletas para locação deve ser um número positivo!")
            return None
        elif qtBikes > self.estoque:
            print(f"Desculpe! Você solicitou {qtBikes} bicicleta(s), mas no momento temos \
                apenas {self.estoque} bicicleta(s) disponível(eis) em estoque.")
            return None
        else:
            horaLocacao = datetime.datetime.now()
            print(f"Olá!\nVocê solicitou o aluguel de {qtBikes} bicicleta(s), às \
                {horaLocacao} de hoje.\n O valor para locação semanal é de R$ 100,00 \
                por semana, por bicicleta.\nAgradecemos a preferência e volte sempre!")
            self.estoque -= qtBikes
            return horaLocacao
    
    ### Locação familiar:
    def locacaoFamilia(self, qtBikes):
        """
        Locação de bicicleta(s) sob a Promoção Família ao Cliente. Aplica um desconto de
        30% ao valor total da locação para 3 a 5 empréstimos de qualquer tipo.
        """
        ### Verifica se é possível aplicar a Promoção Família:
        if not(3 <= qtBikes <= 5):
            print(f"Desconto da 'Promoção Família' não aplicável.")
            return False
        ### Caso positivo, informa a aplicação do desconto e retorna um booleano para
        ### verificação posterior no momento do pagamento:
        else:
            print(f"Olá!\nVocê solicitou o aluguel de {qtBikes} e receberá o desconto da \
                'Promoção Família'!\nVocê terá 30% (trinta por cento) de desconto sobre \
                o valor total final da locação.\nAproveite!")
            return True    
    
    ## Calcular a conta quando o cliente decide devolver a bicicleta:
    def calcularConta(self, alugaBike, locacaoFamilia):
        """
        Método para calcular a conta a ser paga pelo cliente e atualizar o estoque. Deverá
        ser alimentada a partir de argumentos do método 'alugaBike' do objeto Cliente.
        Deverá retornar o valor da conta.
        """
        horaLocacao, tipoLocacao, qtBikes = alugaBike
        conta = 0

        ### Caso esteja tudo de acordo com os valores recebidos do método alugaBike:
        if horaLocacao and tipoLocacao and qtBikes:
            self.estoque += qtBikes
            horaAtual = datetime.datetime.now()
            tempoLocacao = horaAtual - horaLocacao
            ### Locação por hora:
            if tipoLocacao == 1:
                conta = round(tempoLocacao.seconds / 3600) * 5 * qtBikes
            ### Locação por dia:
            elif tipoLocacao == 2:
                conta = round(tempoLocacao.days) * 25 * qtBikes
            ### Locação por semana:
            else: # tipoLocacao == 3:
                conta = round(tempoLocacao.days / 7) * 100 * qtBikes
            ### Verificação do desconto família:
            if locacaoFamilia == True:
                conta = conta * (0.7)
            ### Imprime uma mensagem de agradecimento ao Cliente e retorna o valor total
            ### devido (conta):
            print(f"Obrigado por devolver a(s) bicicleta(s)! \n \
                O valor total da sua locação é de: R$ {conta}.")
            return conta
       ### Caso haja algum problema com os valores recebidos do método alugaBike:
        else:
            print("Locação não encontrada no sistema.")
            return None

# Criação da Classe/Objeto "CLIENTE":

class Cliente(object):
    def __init__(self, nome, carteira):
        self.nome = nome
        self.carteira = carteira
        self.conta = 0

    # verifica o estoque disponível de bicicletas

    def verEstoque(self, estoque, objetoLoja):
        self.estoque = estoque
        return print(f'O estoque disponível é {estoque} bike(s)')

    def alugaBike(self, qtdeBikes, tempoLocacao, objetoLoja):
        try:
            if qtdeBikes <= 0:
                raise ValueError("Digite uma quantidade maior do que 1")

            if not isinstance(objetoLoja, loja):
                raise SystemError("Não recebeu uma loja")

            self.conta += objetoLoja.receberPedido(qtdeBikes)
            print(
                f"Cliente {self.nome} - O aluguel de {qtdeBikes} bike(s) foi realizado. Conta: R${self.conta}")
            return self.conta

        except ValueError:
            print(
                f"Cliente {self.nome} - Aluguel de {qtdeBikes} bike(s) não efetuado por quantidade inválida. Conta: R${self.conta}")
            return -1

        except SystemError:
            print(
                f"Cliente {self.nome} - Aluguel de {qtdeBikes} bike(s) não efetuado por loja inválida. Conta: R${self.conta}")
            return -1

        except:
            print(
                f"Cliente {self.nome} - Aluguel de {qtdeBikes} bike(s) não efetuado. Conta: R${self.conta}")
            return -1

    def pagaConta(self, conta, objetoLoja):
        try:
            if conta <= 0:
                raise ValueError("Valor inválido")

            if conta > self.carteira:
                raise ArithmeticError("Você não tem dinheiro para pagar.")

            if not isinstance(objetoLoja, loja):
                raise SystemError("Você não estabeleceu uma loja")

            self.carteira -= conta
            divida = objetoLoja.receberPagamento(self.conta, conta)
            print(
                f"Cliente {self.nome} - Pagamento de R${conta} da conta de R${self.conta} feito. Saldo devedor: R${self.conta}. Carteira: R${self.carteira}")
            if divida == 0:
                self.conta = 0
            elif divida > 0:
                self.conta = divida
            else:
                self.carteira -= divida
                self.conta = 0
            return self.carteira

        except ValueError:
            print(f"Cliente {self.nome} - Pagamento de R${conta} da conta de R${self.conta} não realizado (valor menor ou igual a zero). Conta: R${self.conta}. Carteira: R${self.carteira}")
            return -1
        except ArithmeticError:
            print(f"Cliente {self.nome} - Pagamento de R${conta} da conta de R${self.conta} não realizado (saldo insuficiente). Conta: R${self.conta}. Carteira: R${self.carteira}")
            return -1
        except SystemError:
            print(f"Cliente {self.nome} - Pagamento de R${conta} da conta de R${self.conta} não realizado (estabeleça uma loja). Conta: R${self.conta}. Carteira: R${self.carteira}")
            return -1
        except:
            print(f"Cliente {self.nome} - Pagamento de R${conta} da conta de R${self.conta} não realizado. Operação cancelada. Conta: R${self.conta}. Carteira: R${self.carteira}")
            return -1