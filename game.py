import random
# Personagem:classe mãe
# Herói: controlado pelo usuário
# Inimigo: adversário do usuário


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

    def receive_attack(self, damage):
        self.__life -= damage
        if self.__life < 0:
            self.__life = 0

    def attack(self, target):
        damage = random.randint(self.get_level() * 2,
                                self.get_level() * 4)  # baseado no nível
        target.receive_attack(damage)
        print(
            f"{self.get_name()} atacou {target.get_name()} e causou {damage} de dano!")


class Hero(Character):
    def __init__(self, name, life, level, skill):
        super().__init__(name, life, level)
        self.__skill = skill

    def get_skill(self):
        return self.__skill

    def show_details(self):
        return f"{super().show_details()}\nHabilidade: {self.get_skill()}\n"

    def special_attack(self, target):
        damage = damage = random.randint(self.get_level() * 5,
                                         self.get_level() * 8)  # dano aumentado
        target.receive_attack(damage)
        print(f"{self.get_name()} usou a habilidade especial {self.get_skill()} em {target.get_name()} e causou {damage} de dano!")


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
        self.enemy = Enemy(name="Morcego", life=80, level=5, element="Voador")

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

            if choose == "1":
                self.hero.attack(self.enemy)
            elif choose == "2":
                self.hero.special_attack(self.enemy)
            else:
                print("Escolha inválida. Escolha novamente.")
            if self.enemy.get_life() > 0:
                # inimigo ataca o heroi
                self.enemy.attack(self.hero)

        if self.hero.get_life() > 0:
            print("\nParabéns, você venceu a batalha!")
        else:
            print("\nVocê foi derrotado!")


# Criar instãncia do jogo e iniciar batalha"
game = Game()
game.start_battle()
