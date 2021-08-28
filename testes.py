import unittest
import classes
from datetime import datetime, timedelta


class Testes(unittest.TestCase):

    def setUp(self):
        hora = datetime.now()
        futuredate = datetime.now() + timedelta(days=10)
        self.cliente = classes.Cliente(5, 2, hora)
        self.loja = classes.Loja(50)

    ## Testes loja
    def testMostrarEstoque(self):
        print("\nTeste - mostrar estoque")
        self.assertEqual(self.loja.mostrarEstoque(), 50)

    def testLocacaoHora1(self):
        print("\nTeste - alugar 0 bikes")
        self.assertEqual(self.loja.locacaoHora(0), None)

    def testLocacaoHora2(self):
        print("\nTeste - alugar 100 bikes hora - sad")
        self.assertEqual(self.loja.locacaoHora(100), None)

    def testLocacaoSemana1(self):
        print("\nTeste - alugar 3 bikes por semana -")
        self.assertEqual(self.loja.locacaoSemana(3), datetime.now())

    def testLocacaoSemana2(self):
        print("\nTeste - alugar 300 bikes por semana -")
        self.assertEqual(self.loja.locacaoSemana(300), None)

    def testLocacaoDia1(self):
        print("\nTeste - alugar 3 bikes por dia -")
        self.assertEqual(self.loja.locacaoDia(3), datetime.now())

    def testLocacaoDia2(self):  # corrigir esses casos de validação
        print("\nTeste - alugar 'a' bikes por dia -")
        self.assertEqual(self.loja.locacaoDia("a"), None)

    def testLocacaoDia3(self):
        print("\nTeste - alugar '' bikes por dia -")  # corrigir
        self.assertEqual(self.loja.locacaoDia(""), None)

    ## Testes cliente

    def testAlugaBike1(self):
        print("\nTeste - alugar 3 bikes por hora -")
        self.assertEqual(self.cliente.alugaBike(qtBikes=3, tipoLocacao=2),(3,2) )

    def testVerEstoque(self):
        print("\nTeste - ver Estoque -") ##a referência a estoque nãoo funciona
        self.assertEqual(self.cliente.verEstoque(), 50)

    # def testLocacaoFamilia(self):
    #     print("\nTeste - alugar '' bikes por dia -")  ## corrigir
    #     self.assertEqual(self.loja.calcularConta(""), None)


if __name__ == "__main__":
    unittest.main()
