from abc import ABC, abstractmethod


class Coffee(ABC):
    @abstractmethod
    def cost(self) -> float:
        pass

    @abstractmethod
    def description(self) -> str:
        pass


class SimpleCoffee(Coffee):
    def cost(self) -> float:
        return 5.0

    def description(self) -> str:
        return "Café simples"


class CoffeeDecorator(Coffee):
    def __init__(self, wrapped: Coffee):
        self._wrapped = wrapped

    def cost(self) -> float:
        return self._wrapped.cost()

    def description(self) -> str:
        return self._wrapped.description()


class SteamedMilk(CoffeeDecorator):
    def cost(self) -> float:
        return super().cost() + 1.5

    def description(self) -> str:
        return super().description() + ", leite vaporizado"


class Chocolate(CoffeeDecorator):
    def cost(self) -> float:
        return super().cost() + 2.0

    def description(self) -> str:
        return super().description() + ", chocolate"


class Cinnamon(CoffeeDecorator):
    def cost(self) -> float:
        return super().cost() + 0.75

    def description(self) -> str:
        return super().description() + ", canela"


if __name__ == "__main__":
    coffee = SimpleCoffee()
    print(f"{coffee.description()} custa R${coffee.cost():.2f}")

    coffee_with_milk = SteamedMilk(coffee)
    print(f"{coffee_with_milk.description()} custa R${coffee_with_milk.cost():.2f}")

    coffee_with_chocolate_cinnamon = Cinnamon(Chocolate(coffee))
    print(
        f"{coffee_with_chocolate_cinnamon.description()} custa R${coffee_with_chocolate_cinnamon.cost():.2f}"
    )

    full_custom_coffee = Cinnamon(Chocolate(SteamedMilk(coffee)))
    print(f"{full_custom_coffee.description()} custa R${full_custom_coffee.cost():.2f}")
