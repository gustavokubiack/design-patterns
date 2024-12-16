from abc import ABC, abstractmethod


# Interface Produto: Pagamento
class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self, amount: float):
        pass


# Produtos Concretos
class CreditCardPayment(PaymentMethod):
    def process_payment(self, amount: float):
        print(f"Pagamento de R${amount:.2f} processado via Cartão de Crédito.")


class PayPalPayment(PaymentMethod):
    def process_payment(self, amount: float):
        print(f"Pagamento de R${amount:.2f} processado via PayPal.")


class BoletoPayment(PaymentMethod):
    def process_payment(self, amount: float):
        print(f"Pagamento de R${amount:.2f} processado via Boleto Bancário.")


# Fábrica Base (Creator)
class PaymentFactory(ABC):
    @abstractmethod
    def create_payment_method(self) -> PaymentMethod:
        pass

    def process(self, amount: float):
        payment_method = self.create_payment_method()
        payment_method.process_payment(amount)


# Fábricas Concretas
class CreditCardPaymentFactory(PaymentFactory):
    def create_payment_method(self) -> PaymentMethod:
        return CreditCardPayment()


class PayPalPaymentFactory(PaymentFactory):
    def create_payment_method(self) -> PaymentMethod:
        return PayPalPayment()


class BoletoPaymentFactory(PaymentFactory):
    def create_payment_method(self) -> PaymentMethod:
        return BoletoPayment()


# Testando o sistema de pagamentos
if __name__ == "__main__":
    # Montante do pagamento
    amount = 150.75

    # Criando fábricas de pagamento
    credit_card_factory = CreditCardPaymentFactory()
    paypal_factory = PayPalPaymentFactory()
    boleto_factory = BoletoPaymentFactory()

    # Processando pagamentos
    print("=== Processando Pagamentos ===")
    credit_card_factory.process(amount)
    paypal_factory.process(amount)
    boleto_factory.process(amount)
