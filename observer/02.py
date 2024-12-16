from abc import ABC, abstractmethod


class IObserver(ABC):
    @abstractmethod
    def update(self, news: str):
        pass


class IObservable(ABC):
    @abstractmethod
    def subscribe(self, observer: IObserver):
        pass

    @abstractmethod
    def unsubscribe(self, observer: IObserver):
        pass

    @abstractmethod
    def notify(self):
        pass


class Reuters(IObservable):
    def __init__(self):
        self._observers = []
        self._latest_news = None

    def subscribe(self, observer: IObserver):
        self._observers.append(observer)
        print(f"{observer.name} se inscreveu na Reuters.")

    def unsubscribe(self, observer: IObserver):
        self._observers.remove(observer)
        print(f"{observer.name} cancelou a inscrição na Reuters.")

    def notify(self):
        for observer in self._observers:
            observer.update(self._latest_news)

    def set_news(self, news: str):
        """Método para atualizar as últimas notícias."""
        self._latest_news = news
        print("\nReuters: Últimas notícias de última hora!")
        self.notify()


class Observer(IObserver):
    def __init__(self, name: str):
        self.name = name

    def update(self, news: str):
        print(f"{self.name} retransmitindo: {news}")


class FoxNews(Observer):
    def __init__(self):
        super().__init__("Fox News")


class CNN(Observer):
    def __init__(self):
        super().__init__("CNN")


class BBC(Observer):
    def __init__(self):
        super().__init__("BBC")


if __name__ == "__main__":
    reuters = Reuters()

    fox_news = FoxNews()
    cnn = CNN()
    bbc = BBC()

    reuters.subscribe(fox_news)
    reuters.subscribe(cnn)
    reuters.subscribe(bbc)

    reuters.set_news("Eleições 2024: Resultado final divulgado!")
    reuters.set_news("Bolsa de Valores em alta recorde hoje!")

    reuters.unsubscribe(cnn)

    reuters.set_news("Grande terremoto registrado na Ásia.")
