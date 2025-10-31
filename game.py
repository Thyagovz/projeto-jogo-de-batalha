class Character:
    def __init__(self, name, life, level):
        self.__name = name
        self.__life = life
        self.__level = level

    def get_name(self):
        return self.__name

    def get_life(self):
        return self.__life

    def get_level(self):
        return self.__level

    def show_details(self):
        return f"Nome:{self.get_name()}\nVida: {self.get_life()}\nNível: {self.get_level()}"


class Hero(Character):
    def __init__(self, name, life, level, skill):
        super().__init__(name, life, level)
        self.__skill = skill

    def get_skill(self):
        return self.__skill

    def show_details(self):
        return f"{super().show_details()}\nHabilidade: {self.get_skill()}\n"


class Enemy(Character):
    def __init__(self, name, life, level, element):
        super().__init__(name, life, level)
        self.__element = element

    def get_element(self):
        return self.__element

    def show_details(self):
        return f"{super().show_details()}\nTipo: {self.get_element()}\n"


class Game:
    """Classe orquestradora do jogo"""

    def __init__(self):
        self.hero = Hero(name="Herói", life=100, level=5, skill="Super força")
        self.enemy = Enemy(name="Morcego", life=50, level=3, element="Voador")

    def start_battle(self):
        """ Fazer a gestão de batalha em turnos"""
        print("Iniciando batalha")
        while self.hero.get_life() > 0 and self.enemy.get_life() > 0:
            print("\nDetalhes dos Personagens:")
            print(self.hero.show_details())
            print(self.enemy.show_details())

            input("Pressione Enter para atacar...")
            choose = input(
                "Escolha (1 - Ataque Normal, 2 - Ataque Especial): ")


# Criar instãncia do jogo e iniciar batalha"
game = Game()
game.start_battle()
