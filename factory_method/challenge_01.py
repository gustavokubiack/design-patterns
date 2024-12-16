from abc import ABC, abstractmethod


# Interface Produto: Notificador
class Notifier(ABC):
    @abstractmethod
    def send(self, message: str):
        pass


# Produtos Concretos
class EmailNotifier(Notifier):
    def send(self, message: str):
        print(f"Enviando Email: {message}")


class SMSNotifier(Notifier):
    def send(self, message: str):
        print(f"Enviando SMS: {message}")


class PushNotifier(Notifier):
    def send(self, message: str):
        print(f"Enviando Notificação Push: {message}")


# Fábrica Base (Creator)
class NotifierFactory(ABC):
    @abstractmethod
    def create_notifier(self) -> Notifier:
        pass

    def notify(self, message: str):
        # Cria o notificador e envia a mensagem
        notifier = self.create_notifier()
        notifier.send(message)


# Fábricas Concretas
class EmailNotifierFactory(NotifierFactory):
    def create_notifier(self) -> Notifier:
        return EmailNotifier()


class SMSNotifierFactory(NotifierFactory):
    def create_notifier(self) -> Notifier:
        return SMSNotifier()


class PushNotifierFactory(NotifierFactory):
    def create_notifier(self) -> Notifier:
        return PushNotifier()


# Testando o sistema
if __name__ == "__main__":
    # Criando as fábricas de notificadores
    email_factory = EmailNotifierFactory()
    sms_factory = SMSNotifierFactory()
    push_factory = PushNotifierFactory()

    # Enviando notificações
    email_factory.notify("Olá! Você recebeu um email.")
    sms_factory.notify("Olá! Você recebeu um SMS.")
    push_factory.notify("Olá! Você recebeu uma notificação Push.")
