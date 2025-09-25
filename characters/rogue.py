from characters.character import Character
import random


class Rogue(Character):
    def __init__(self, name):
        super().__init__(name=name, level=1, health=90, attack_power=12)

    def attack(self, target):
        damage = self.attack_power
        print(f"{self.name}이(가) 기본 공격으로 {damage} 피해를 입힙니다!")
        target.take_damage(damage)

    def special_attack(self, target):
        self.ambush(target)

    def ambush(self, target):
        if random.random() < 0.7:
            damage = self.attack_power * 3
            print(f"{self.name}의 기습 성공! {damage} 피해를 입힙니다.!")
            target.take_damage(damage)
        else:
            print(f"{self.name}의 기습이 실패했습니다... 공겨가지 못했습니다.")
