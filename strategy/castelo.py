from abc import ABC, abstractmethod


class Arma(ABC):
    @abstractmethod
    def usar_arma(self):
        pass


class Machado(Arma):
    def usar_arma(self):
        print("Usando o Machado para atacar!")


class Espada(Arma):
    def usar_arma(self):
        print("Usando a Espada para atacar!")


class ArcoFlecha(Arma):
    def usar_arma(self):
        print("Usando o Arco e Flecha para atacar!")


class Faca(Arma):
    def usar_arma(self):
        print("Usando a Faca para atacar!")


class Personagem(ABC):
    def __init__(self):
        self.arma: Arma = None

    def atribui_arma(self, arma: Arma):
        """Método para mudar a arma do personagem."""
        self.arma = arma

    @abstractmethod
    def lutar(self):
        pass


class Rei(Personagem):
    def lutar(self):
        print("Rei está lutando!")
        if self.arma:
            self.arma.usar_arma()
        else:
            print("Rei está desarmado!")


class Rainha(Personagem):
    def lutar(self):
        print("Rainha está lutando!")
        if self.arma:
            self.arma.usar_arma()
        else:
            print("Rainha está desarmada!")


class Guerreiro(Personagem):
    def lutar(self):
        print("Guerreiro está lutando!")
        if self.arma:
            self.arma.usar_arma()
        else:
            print("Guerreiro está desarmado!")


class Duende(Personagem):
    def lutar(self):
        print("Duende está lutando!")
        if self.arma:
            self.arma.usar_arma()
        else:
            print("Duende está desarmado!")


if __name__ == "__main__":
    machado = Machado()
    espada = Espada()
    arco_flecha = ArcoFlecha()
    faca = Faca()

    rei = Rei()
    rainha = Rainha()
    guerreiro = Guerreiro()
    duende = Duende()

    rei.atribui_arma(espada)
    rei.lutar()

    rainha.atribui_arma(arco_flecha)
    rainha.lutar()

    guerreiro.atribui_arma(machado)
    guerreiro.lutar()

    duende.atribui_arma(faca)
    duende.lutar()

    print("\nMudando a arma do Rei para o Machado...")
    rei.atribui_arma(machado)
    rei.lutar()
