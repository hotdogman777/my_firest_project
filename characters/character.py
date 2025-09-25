from abc import ABC, abstractmethod


class Character(ABC):
    def __init__(self, name, level, health, attack_power):
        self.name = name
        self.level = level
        self.health = health
        self.attack_power = attack_power

    @abstractmethod  # 추상메소드 이 함수는 다른 곳에서 변경을 할수도 있다
    def attack(self, target):
        pass

    @abstractmethod
    def special_attack(self, target):
        pass

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name}이(가) {damage} 피해를 입었습니다. 체력: {self.health}")

    def is_alive(self):
        return self.health > 0

    def show_status(self):
        print(f"[{self.name}] 레벨:{self.level}, 체력:{self.health}, 공격력:{self.attack_power}")

    def reset_health(self):
        self.health = 100
        print(f"{self.name}의 체력이 {self.health}으로 초기화되었습니다.")

    def get_name(self):
        print(f"당신의 이름은{self.name}입니다.")
