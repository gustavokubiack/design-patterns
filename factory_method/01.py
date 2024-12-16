from abc import ABC, abstractmethod


class MotorVehicle(ABC):
    @abstractmethod
    def build(self) -> str:
        pass


class Motorcycle(MotorVehicle):
    def build(self) -> str:
        return "Construindo uma motocicleta"


class Car(MotorVehicle):
    def build(self) -> str:
        return "Construindo um carro"


class MotorVehicleFactory(ABC):
    @abstractmethod
    def create_motor_vehicle(self) -> MotorVehicle:
        pass

    def create(self) -> MotorVehicle:
        vehicle = self.create_motor_vehicle()
        print(vehicle.build())
        return vehicle


class MotorcycleFactory(MotorVehicleFactory):
    def create_motor_vehicle(self) -> MotorVehicle:
        return Motorcycle()


class CarFactory(MotorVehicleFactory):
    def create_motor_vehicle(self) -> MotorVehicle:
        return Car()


if __name__ == "__main__":
    motorcycle_factory = MotorcycleFactory()
    motorcycle = motorcycle_factory.create()

    car_factory = CarFactory()
    car = car_factory.create()
