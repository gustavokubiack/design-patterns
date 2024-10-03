"""
2. Usar o padrão Strategy para aplicar diferentes estratégias de desconto em um sistema de compras.
Descrição: Desenvolva uma aplicação Python que simule a aplicação de descontos variáveis (desconto por
fidelidade, desconto sazonal, desconto por volume de compra) em um valor total de compra. A estratégia de
desconto deve poder ser trocada dinamicamente.
Passos:
• Crie uma interface DiscountStrategy com um método apply_discount que aceite um valor de compra e
retorne o valor com desconto aplicado.
• Implemente três classes de estratégia: LoyaltyDiscount, SeasonalDiscount e BulkPurchaseDiscount. Cada
uma deve calcular o desconto de uma forma diferente (por exemplo, 5% para fidelidade, 10% para
compras em promoção, 15% para grandes quantidades).
• Crie uma classe ShoppingCart que use a estratégia de desconto. Essa classe deve ter o método
set_discount_strategy para alterar a estratégia de desconto e o método get_final_price para calcular o
valor total após aplicar o desconto.
• Permita que o usuário insira o valor total da compra e escolha o tipo de desconto a ser aplicado.
"""
from abc import ABC, abstractmethod


class DiscountStrategy(ABC):
    
    @abstractmethod
    def apply_discount(self, value: float):
        pass


class LoyaltyDiscount(DiscountStrategy):
    def apply_discount(self, value: float):
        ...


class SeasonalDiscount(DiscountStrategy):
    def apply_discount(self, value: float):
        ...


class BulkPurchaseDiscount(DiscountStrategy):
    def apply_discount(self, value: float):
        ...


class ShoppingCart:
    def __init__(self, value: float,  discount_strategy: DiscountStrategy) -> None: 
        self.value = value
        self._discount_strategy = discount_strategy

    @property
    def discount_strategy(self):
        return self._discount_strategy
    
    @discount_strategy.setter
    def discount_strategy(self, discount_strategy: DiscountStrategy):
        self._discount_strategy = discount_strategy

    def total_price(self):
        ...