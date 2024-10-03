""""
1. Criar um sistema que utilize o padrão Strategy para simular diferentes estratégias de deslocamento
usando meios de transporte variados.
Descrição: Crie uma aplicação Python que simule diferentes formas de transporte (carro, bicicleta, a pé),
permitindo ao usuário alternar entre elas e calcular o tempo necessário para percorrer uma determinada
distância.
Passos:
    • Crie uma interface TravelStrategy com um método travel_time que aceite uma distância em quilômetros.
    • Implemente três classes de estratégia: CarStrategy, BicycleStrategy e WalkStrategy. Cada classe deve retornar
o tempo estimado para percorrer a distância fornecida com base em uma velocidade fixa (por exemplo:
carro 60 km/h, bicicleta 15 km/h, a pé 5 km/h).
    • Crie uma classe TravelContext que contenha o método set_strategy para definir o meio de transporte atual e
um método calculate_time para calcular o tempo de viagem.
    • Desenvolva uma interface simples que permita ao usuário escolher o meio de transporte e inserir a
distância.
"""

from abc import ABC, abstractmethod


class TravelStrategy(ABC):

    @abstractmethod
    def travel_time(self, distance: float):
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass


class CarStrategy(TravelStrategy):

    def travel_time(self, distance: float):
        return round(distance / 60, 2)

    def __str__(self) -> str:
        return "Carro"


class BicycleStrategy(TravelStrategy):

    def travel_time(self, distance: float):
        return round(distance / 15, 2)

    def __str__(self) -> str:
        return "Bicicleta"


class WalkStrategy(TravelStrategy):

    def travel_time(self, distance: float):
        return round(distance / 5, 2)

    def __str__(self) -> str:
        return "À pé"


class TravelContext:
    def __init__(self, distance: float, travel_strategy: TravelStrategy = None) -> None:
        self._travel_strategy = travel_strategy
        self.distance = distance

    @property
    def travel_strategy(self):
        return self._travel_strategy

    @travel_strategy.setter
    def travel_strategy(self, travel_strategy: TravelStrategy) -> TravelStrategy:
        self._travel_strategy = travel_strategy

    def calculate_time(self):
        result = self._travel_strategy.travel_time(self.distance)
        return result


if __name__ == "__main__":
    distance = float(input("Insira a distância em km: "))
    travel = input(
        "Insira o meio de transporte: \n 1 - Carro \n 2 - Bicicleta \n 3 - A pé\n"
    )
    map_strategy = {
        "1": CarStrategy(),
        "2": BicycleStrategy(),
        "3": WalkStrategy(),
    }
    if travel not in map_strategy.keys():
        raise Exception("Meio de transporte inexistente!")
    
    instance = TravelContext(distance, map_strategy[travel])
    result = instance.calculate_time()
    hours = int(result)
    minutes = int((result - hours) * 60)
    print(
        f"O tempo necessário para percorrer {distance}km de {instance.travel_strategy} é {hours} hora e {minutes} minutos"
    )
