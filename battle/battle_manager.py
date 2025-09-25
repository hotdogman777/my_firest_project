import random
import time


class BattleManager:
    def __init__(self, char1, char2):
        self.char1 = char1
        self.char2 = char2

    def start_battle(self):
        print(f"전투 시작 {self.char1.name} vs {self.char2.name} \n")

        attacker, defender = (self.char1, self.char2) if random.random() < 0.5 else (self.char2, self.char1)
        print(f"첫 공격자는 {attacker.name}!\n")

        while attacker.is_alive() and defender.is_alive():
            time.sleep(1)

            try:
                if random.random() < 0.7:
                    print(f"{attacker.name}의 기본 공격!\n")
                    attacker.attack(defender)
                else:
                    print(f"{attacker.name}의 특수 공격!\n")
                    attacker.special_attack(defender)
            except Exception as e:
                print(f"{attacker.name}의 특수 공격 실패: {e}\n")
                attacker.attack(defender)

            if not defender.is_alive():
                print(f"\n{defender.name}은(는) 쓰러졌다!\n{attacker.name} 승리!\n")
                break

            attacker, defender = defender, attacker
