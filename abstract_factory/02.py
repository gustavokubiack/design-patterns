from abc import ABC, abstractmethod


class MotorVehicle(ABC):
    @abstractmethod
    def motor_function(self):
        pass


class ElectricVehicle(ABC):
    @abstractmethod
    def electric_function(self):
        pass


class FutureVehicleMotorcycle(MotorVehicle):
    def motor_function(self):
        return "Future motorcycle powered by an advanced motor."


class FutureVehicleElectricCar(ElectricVehicle):
    def electric_function(self):
        return "Future electric car with next-gen battery technology."


class NextGenMotorcycle(MotorVehicle):
    def motor_function(self):
        return "Next-generation motorcycle with cutting-edge engine."


class NextGenElectricCar(ElectricVehicle):
    def electric_function(self):
        return "Next-generation electric car with self-charging capabilities."


class Corporation(ABC):
    @abstractmethod
    def create_motor_vehicle(self) -> MotorVehicle:
        pass

    @abstractmethod
    def create_electric_vehicle(self) -> ElectricVehicle:
        pass


class FutureVehicleCorporation(Corporation):
    def create_motor_vehicle(self) -> MotorVehicle:
        return FutureVehicleMotorcycle()

    def create_electric_vehicle(self) -> ElectricVehicle:
        return FutureVehicleElectricCar()


class NextGenCorporation(Corporation):
    def create_motor_vehicle(self) -> MotorVehicle:
        return NextGenMotorcycle()

    def create_electric_vehicle(self) -> ElectricVehicle:
        return NextGenElectricCar()


def client_code(corporation: Corporation):
    motor_vehicle = corporation.create_motor_vehicle()
    electric_vehicle = corporation.create_electric_vehicle()

    print(motor_vehicle.motor_function())
    print(electric_vehicle.electric_function())


if __name__ == "__main__":
    print("Future Vehicle Corporation:")
    client_code(FutureVehicleCorporation())

    print("\nNext Generation Corporation:")
    client_code(NextGenCorporation())
