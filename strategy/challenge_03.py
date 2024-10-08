"""
3. Implemente uma calculadora de impostos que use o padrão Strategy para aplicar diferentes tipos de
impostos (por exemplo, imposto sobre renda, imposto sobre vendas, imposto sobre produtos).
Passos:
• Crie uma interface ImpostoStrategy com o método calcular.
• Implemente três estratégias: ImpostoRenda, ImpostoVendas e ImpostoProduto, cada uma com sua fórmula
de cálculo.
• Crie uma classe CalculadoraDeImposto que receba diferentes estratégias e aplique o cálculo.
• Crie uma função principal para testar o cálculo dos impostos com diferentes valores.
"""
from abc import ABC, abstractmethod


class TaxStrategy(ABC):
    @abstractmethod
    def calculate(self, value: float) -> float:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass


class IncomeTax(TaxStrategy):
    def calculate(self, value: float) -> float:
        return value * 0.15

    def __str__(self) -> str:
        return "Imposto de Renda"


class SalesTax(TaxStrategy):
    def calculate(self, value: float) -> float:
        return value * 0.10

    def __str__(self) -> str:
        return "Imposto de Venda"


class ProductTax(TaxStrategy):
    def calculate(self, value: float) -> float:
        return value * 0.18

    def __str__(self) -> str:
        return "Imposto de Produto"


class TaxCalculator:
    def __init__(self, value: float, tax_strategy: TaxStrategy) -> None:
        self._tax_strategy = tax_strategy
        self.value = value

    @property
    def tax_strategy(self):
        return self._tax_strategy

    @tax_strategy.setter
    def tax_strategy(self, tax_strategy: TaxStrategy) -> TaxStrategy:
        self._tax_strategy = tax_strategy

    def tax_final_price(self) -> float:
        return self._tax_strategy.calculate(self.value)


if __name__ == "__main__":
    value = float(input("Insira o valor da compra: "))
    tax = input(
        "Insira o tipo de imposto: \n 1 - Imposto de Renda \n 2 - Imposto de Venda \n 3 - Imposto de Produto\n"
    )
    map_strategy = {
        "1": IncomeTax(),
        "2": SalesTax(),
        "3": ProductTax(),
    }
    if tax not in map_strategy.keys():
        raise Exception("Tipo de imposto inexistente!")

    instance = TaxCalculator(value, map_strategy[tax])
    tax = instance.tax_final_price()
    print(
        f"Utilizando o {instance.tax_strategy} o valor de R${value} terá um imposto de R${tax}"
    )
