"""4. Implemente um jogo simples onde diferentes personagens podem atacar usando estratégias de
ataque variadas (por exemplo, ataque corpo a corpo, ataque à distância, ataque mágico).
Passos:
• Crie uma interface EstrategiaDeAtaque com o método atacar().
• Implemente três estratégias: AtaqueCorpoACorpo, AtaqueDistancia, e AtaqueMagico.
• Crie uma classe Personagem que tenha um nome e uma estratégia de ataque, permitindo alterar a
estratégia dinamicamente.
• Crie uma função principal para criar personagens e simular diferentes ataques."""

from abc import ABC, abstractmethod


class AttackStrategy(ABC):
    @abstractmethod
    def attack(self):
        pass


class MeleeAttack(AttackStrategy):
    def attack(self) -> str:
        return "Atacando corpo a corpo"


class DistanceAttack(AttackStrategy):
    def attack(self) -> str:
        return "Atacando à distância com um arco e flecha"


class MagicAttack(AttackStrategy):
    def attack(self) -> str:
        return "Atacando com poder mágico"


class Character:
    def __init__(self, name: str, attack_strategy: AttackStrategy) -> None:
        self.name = name
        self._attack_strategy = attack_strategy

    @property
    def attack_strategy(self) -> AttackStrategy:
        return self._attack_strategy

    @attack_strategy.setter
    def attack_strategy(self, attack_strategy: AttackStrategy):
        self._attack_strategy = attack_strategy

    def handle_attack(self):
        attack = self.attack_strategy.attack()
        return f"{self.name}: {attack}"


def main():
    mike = Character(name="Mike", attack_strategy=MeleeAttack())
    print(mike.handle_attack())

    john = Character(name="John", attack_strategy=DistanceAttack())
    print(john.handle_attack())

    josh = Character(name="Josh", attack_strategy=MagicAttack())
    print(josh.handle_attack())

    print(f"{50 * '-'}")

    josh.attack_strategy = DistanceAttack()
    print(josh.handle_attack())


if __name__ == "__main__":
    main()
