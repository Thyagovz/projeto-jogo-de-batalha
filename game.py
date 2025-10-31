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


hero = Hero(name="Herói", life=100, level=5, skill="Super força")
print(hero.show_details())
enemy = Enemy(name="Morcego", life=50, level=3, element="Voador")
print(enemy.show_details())
