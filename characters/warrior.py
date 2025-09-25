from characters.character import Character


class Warrior(Character):
    def __init__(self, name):
        super().__init__(name=name, level=1, health=100, attack_power=15)

    def attack(self, target):
        damage = self.attack_power
        print(f"{self.name}이(가) 기본 공격으로 {damage} 피해를 입힙니다!")
        target.take_damage(damage)

    def special_attack(self, target):
        self.power_strike(target)

    def power_strike(self, target):
        damage = self.attack_power * 2
        print(f"{self.name}의 강력한 일격 {damage} 피해를 입힙니다.!")
        target.take_damage(damage)

        self.health -= 5
        print(f"{self.name}은(는) 반동으로 5 체력을 잃었습니다. 현재 체력: {self.health}")
