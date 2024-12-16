from abc import ABC, abstractmethod


class Drink(ABC):
    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def get_price(self):
        pass


class Caipira(Drink):
    def get_description(self):
        return "Caipira (Base drink)"

    def get_price(self):
        return 20.0


class Caipirinha(Drink):
    def get_description(self):
        return "Caipirinha (Cachaça, Limão, Gelo e Açúcar)"

    def get_price(self):
        return 25.0


# Abstract Decorator
class DrinkDecorator(Drink):
    def __init__(self, drink):
        self.drink = drink

    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def get_price(self):
        pass


class Saque(DrinkDecorator):
    def get_description(self):
        return self.drink.get_description() + ", Saquê"

    def get_price(self):
        return self.drink.get_price() + 5.0


class Abacaxi(DrinkDecorator):
    def get_description(self):
        return self.drink.get_description() + ", Abacaxi"

    def get_price(self):
        return self.drink.get_price() + 3.0


class Kiwi(DrinkDecorator):
    def get_description(self):
        return self.drink.get_description() + ", Kiwi"

    def get_price(self):
        return self.drink.get_price() + 4.0


class Acucar(DrinkDecorator):
    def get_description(self):
        return self.drink.get_description() + ", Açúcar"

    def get_price(self):
        return self.drink.get_price() + 1.0


class Vodka(DrinkDecorator):
    def get_description(self):
        return self.drink.get_description() + ", Vodka"

    def get_price(self):
        return self.drink.get_price() + 6.0


class Morango(DrinkDecorator):
    def get_description(self):
        return self.drink.get_description() + ", Morango"

    def get_price(self):
        return self.drink.get_price() + 4.0


class Adocante(DrinkDecorator):
    def get_description(self):
        return self.drink.get_description() + ", Adoçante"

    def get_price(self):
        return self.drink.get_price() + 1.0


def main():
    drink1 = Caipira()
    drink1 = Saque(drink1)
    drink1 = Abacaxi(drink1)
    drink1 = Kiwi(drink1)
    drink1 = Acucar(drink1)
    print(f"Pedido 1: {drink1.get_description()} - Preço: R${drink1.get_price():.2f}")

    drink2 = Caipira()
    drink2 = Vodka(drink2)
    drink2 = Morango(drink2)
    drink2 = Adocante(drink2)
    print(f"Pedido 2: {drink2.get_description()} - Preço: R${drink2.get_price():.2f}")

    drink3 = Caipirinha()
    print(f"Pedido 3: {drink3.get_description()} - Preço: R${drink3.get_price():.2f}")


if __name__ == "__main__":
    main()
