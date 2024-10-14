from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, value_1: int, value_2: int) -> None:
        pass


class DivObserver(Observer):
    def update(self, value_1: int, value_2: int):
        if value_2 != 0:
            print(f"O valor da divisão por 2 é: {value_1 / value_2}")


class ModObserver(Observer):
    def update(self, value_1: int, value_2: int):
        print(f"O valor do resto da divisão por 2: {value_1 % value_2}")


class MultiObserver(Observer):
    def update(self, value_1: int, value_2: int):
        print(f"O valor da multiplicação é: {value_1 * value_2}")


class Subject(ABC):
    @abstractmethod
    def register_observer(observer: Observer):
        pass

    @abstractmethod
    def remove_observer(self, observer: Observer):
        pass

    @abstractmethod
    def notify_observer():
        pass


class ConcreteSubject(Subject):
    def __init__(self) -> None:
        self._value_1 = 0
        self._value_2 = 0
        self._observers = []

    @property
    def value_1(self):
        return self._value_1

    @value_1.setter
    def value_1(self, value_1: int):
        self._value_1 = value_1
        self.notify_observer()

    @property
    def value_2(self):
        return self._value_2

    @value_2.setter
    def value_2(self, value_2: int):
        self._value_2 = value_2
        self.notify_observer()

    def register_observer(self, observer: Observer) -> None:
        self._observers.append(observer)

    def remove_observer(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify_observer(self):
        for observer in self._observers:
            observer.update(self._value_1, self._value_2)


def main():
    subject = ConcreteSubject()
    div = DivObserver()
    multi = MultiObserver()
    mod = ModObserver()

    print("Alterando valores...")
    subject.value_1 = 4
    subject.value_2 = 2

    print(f"Adicionando div, multi e mod no sujeito.")
    subject.register_observer(div)
    subject.register_observer(multi)
    subject.register_observer(mod)

    print(f"{50 * '-'}")
    print("Notificando...")
    subject.notify_observer()

    print(f"{50 * '-'}")
    print("Removendo o div")
    subject.remove_observer(div)

    print("Notifcando...")
    subject.notify_observer()


if __name__ == "__main__":
    main()
