from abc import ABC, abstractmethod


class Furniture(ABC):
    @abstractmethod
    def furniture_function(self):
        pass

    @abstractmethod
    def show_style(self):
        pass


class ClassicCabinet(Furniture):
    def furniture_function(self):
        return "Storing items in a classic cabinet"

    def show_style(self):
        return "Classic style cabinet"


class ClassicChair(Furniture):
    def furniture_function(self):
        return "Sitting on a classic chair"

    def show_style(self):
        return "Classic style chair"


class ClassicDiningTable(Furniture):
    def furniture_function(self):
        return "Dining on a classic table"

    def show_style(self):
        return "Classic style dining table"


class ContemporaryCabinet(Furniture):
    def furniture_function(self):
        return "Storing items in a contemporary cabinet"

    def show_style(self):
        return "Contemporary style cabinet"


class ContemporaryChair(Furniture):
    def furniture_function(self):
        return "Sitting on a contemporary chair"

    def show_style(self):
        return "Contemporary style chair"


class ContemporaryDiningTable(Furniture):
    def furniture_function(self):
        return "Dining on a contemporary table"

    def show_style(self):
        return "Contemporary style dining table"


class ScandinavianCabinet(Furniture):
    def furniture_function(self):
        return "Storing items in a Scandinavian cabinet"

    def show_style(self):
        return "Scandinavian style cabinet"


class ScandinavianChair(Furniture):
    def furniture_function(self):
        return "Sitting on a Scandinavian chair"

    def show_style(self):
        return "Scandinavian style chair"


class ScandinavianDiningTable(Furniture):
    def furniture_function(self):
        return "Dining on a Scandinavian table"

    def show_style(self):
        return "Scandinavian style dining table"


class FurnitureFactory(ABC):
    @abstractmethod
    def create_cabinet(self):
        pass

    @abstractmethod
    def create_chair(self):
        pass

    @abstractmethod
    def create_dining_table(self):
        pass


class ClassicFactory(FurnitureFactory):
    def create_cabinet(self):
        return ClassicCabinet()

    def create_chair(self):
        return ClassicChair()

    def create_dining_table(self):
        return ClassicDiningTable()


class ContemporaryFactory(FurnitureFactory):
    def create_cabinet(self):
        return ContemporaryCabinet()

    def create_chair(self):
        return ContemporaryChair()

    def create_dining_table(self):
        return ContemporaryDiningTable()


class ScandinavianFactory(FurnitureFactory):
    def create_cabinet(self):
        return ScandinavianCabinet()

    def create_chair(self):
        return ScandinavianChair()

    def create_dining_table(self):
        return ScandinavianDiningTable()


def client_code(factory: FurnitureFactory):
    cabinet = factory.create_cabinet()
    chair = factory.create_chair()
    table = factory.create_dining_table()

    print(cabinet.furniture_function(), "-", cabinet.show_style())
    print(chair.furniture_function(), "-", chair.show_style())
    print(table.furniture_function(), "-", table.show_style())


if __name__ == "__main__":
    print("Testing Classic Factory:")
    client_code(ClassicFactory())

    print("\nTesting Contemporary Factory:")
    client_code(ContemporaryFactory())

    print("\nTesting Scandinavian Factory:")
    client_code(ScandinavianFactory())
