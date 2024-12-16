from abc import ABC, abstractmethod


class Product(ABC):
    def __init__(self, color: str, width: float, height: float, depth: float):
        self.color = color
        self.width = width
        self.height = height
        self.depth = depth

    @abstractmethod
    def to_string(self) -> str:
        pass


class ModernArmchair(Product):
    def to_string(self) -> str:
        return f"Modern Armchair - Color: {self.color}, Width: {self.width}, Height: {self.height}, Depth: {self.depth}"


class ModernCoffeeTable(Product):
    def to_string(self) -> str:
        return f"Modern Coffee Table - Color: {self.color}, Width: {self.width}, Height: {self.height}, Length: {self.depth}"


class ModernSofa(Product):
    def to_string(self) -> str:
        return f"Modern Sofa - Color: {self.color}, Width: {self.width}, Height: {self.height}, Depth: {self.depth}"


class FurnitureFactory(ABC):
    @abstractmethod
    def make_armchair(self) -> Product:
        pass

    @abstractmethod
    def make_coffee_table(self) -> Product:
        pass

    @abstractmethod
    def make_sofa(self) -> Product:
        pass


class ModernFurnitureFactory(FurnitureFactory):
    def make_armchair(self) -> Product:
        return ModernArmchair(color="White", width=0.75, height=1.0, depth=0.8)

    def make_coffee_table(self) -> Product:
        return ModernCoffeeTable(color="Black", width=1.2, height=0.5, depth=0.6)

    def make_sofa(self) -> Product:
        return ModernSofa(color="Gray", width=2.0, height=0.9, depth=1.0)


if __name__ == "__main__":
    factory = ModernFurnitureFactory()

    armchair = factory.make_armchair()
    coffee_table = factory.make_coffee_table()
    sofa = factory.make_sofa()

    print(armchair.to_string())
    print(coffee_table.to_string())
    print(sofa.to_string())
