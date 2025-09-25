from characters.character import Character


class Mage(Character):
    def __init__(self, name):
        super().__init__(name=name, level=1, health=80, attack_power=18)
        self.mana = 100

    def attack(self, target):
        damage = self.attack_power
        print(f"{self.name}이(가) 기본 공격으로 {damage} 피해를 입힙니다!")
        target.take_damage(damage)

    def special_attack(self, target):
        self.fireball(target)

    def fireball(self, target):
        try:
            if self.mana < 20:
                raise ValueError("마나가 부족합니다!")
            damage = self.attack_power * 1.5
            print(f"{self.name}이 뜨거운 공격 {damage} 피해를 입힙니다.!")
            target.take_damage(damage)

            self.mana -= 20
            print(f"{self.name}은(는) 스킬 사용으로 인해 마나가 20 소모 하였습니다. 현재 마나: {self.mana}")

        except ValueError as e:
            print(f"[스킬 실패]", {e})
