from abc import ABC, abstractmethod


class Notifier(ABC):
    @abstractmethod
    def send(self, message: str):
        pass


class BaseNotifier(Notifier):
    def send(self, message: str):
        print(f"Notificação Base: {message}")


class NotifierDecorator(Notifier):
    def __init__(self, notifier: Notifier):
        self._notifier = notifier

    def send(self, message: str):
        self._notifier.send(message)


class EmailNotifier(NotifierDecorator):
    def send(self, message: str):
        super().send(message)
        self._send_email(message)

    def _send_email(self, message: str):
        print(f"Enviando notificação pelo E-mail: {message}")


class SMSNotifier(NotifierDecorator):
    def send(self, message: str):
        super().send(message)
        self._send_sms(message)

    def _send_sms(self, message: str):
        print(f"Enviando notificação pelo SMS: {message}")


class SlackNotifier(NotifierDecorator):
    def send(self, message: str):
        super().send(message)
        self._send_slack(message)

    def _send_slack(self, message: str):
        print(f"Enviando notificação pelo Slack: {message}")


if __name__ == "__main__":
    notifier = BaseNotifier()

    notifier = EmailNotifier(notifier)
    notifier = SMSNotifier(notifier)
    notifier = SlackNotifier(notifier)

    notifier.send("Olá, mundo!")
