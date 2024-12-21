from abc import ABC, abstractmethod


class Weapon(ABC):
    @abstractmethod
    def useful_function(self) -> str:
        pass


class Armor(ABC):
    @abstractmethod
    def useful_function(self) -> str:
        pass

    @abstractmethod
    def useful_function_with_weapon(self, collaborator: Weapon) -> str:
        pass


class Sword(Weapon):
    def useful_function(self) -> str:
        return "Sword: A sharp blade for melee combat."


class Axe(Weapon):
    def useful_function(self) -> str:
        return "Axe: A heavy weapon for powerful strikes."


class MageFireball(Weapon):
    def useful_function(self) -> str:
        return "Fireball: A magical projectile of fire."


class BodyArmor(Armor):
    def useful_function(self) -> str:
        return "BodyArmor: Provides basic protection for the body."

    def useful_function_with_weapon(self, collaborator: Weapon) -> str:
        return f"BodyArmor: Enhances the effectiveness of the {collaborator.useful_function()}."


class OrcArmor(Armor):
    def useful_function(self) -> str:
        return "OrcArmor: Tough and menacing protection for orcs."

    def useful_function_with_weapon(self, collaborator: Weapon) -> str:
        return f"OrcArmor: Amplifies the power of the {collaborator.useful_function()}."


class CloakArmor(Armor):
    def useful_function(self) -> str:
        return "CloakArmor: Provides stealth and magical resistance."

    def useful_function_with_weapon(self, collaborator: Weapon) -> str:
        return (
            f"CloakArmor: Boosts the potency of the {collaborator.useful_function()}."
        )


class AbstractFactory(ABC):
    @abstractmethod
    def create_weapon(self) -> Weapon:
        pass

    @abstractmethod
    def create_armor(self) -> Armor:
        pass


class WarriorFactory(AbstractFactory):
    def create_weapon(self) -> Weapon:
        return Sword()

    def create_armor(self) -> Armor:
        return BodyArmor()


class OrcFactory(AbstractFactory):
    def create_weapon(self) -> Weapon:
        return Axe()

    def create_armor(self) -> Armor:
        return OrcArmor()


class MageFactory(AbstractFactory):
    def create_weapon(self) -> Weapon:
        return MageFireball()

    def create_armor(self) -> Armor:
        return CloakArmor()


def client_code(factory: AbstractFactory):
    weapon = factory.create_weapon()
    armor = factory.create_armor()

    print(weapon.useful_function())
    print(armor.useful_function())
    print(armor.useful_function_with_weapon(weapon))


if __name__ == "__main__":
    print("Warrior Factory:")
    client_code(WarriorFactory())

    print("\nOrc Factory:")
    client_code(OrcFactory())

    print("\nMage Factory:")
    client_code(MageFactory())
