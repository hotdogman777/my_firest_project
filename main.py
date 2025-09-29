from characters.warrior import Warrior
from characters.mage import Mage
from characters.rogue import Rogue
from battle.battle_manager import BattleManager


def choose_character(prompt):
    while True:
        print("\n캐릭터 목록: ")
        print("1. 전사 (Warrior)")
        print("2. 마법사 (Mage)")
        print("3. 도적 (Rogue)")
        choice = input(prompt)

        if choice == "1":
            return Warrior("전사")
        elif choice == "2":
            return Mage("마법사")
        elif choice == "3":
            return Rogue("도적")
        else:
            print("잘못 입력했습니다. 다시 선택하세요.")


if __name__ == "__main__":
    print("게임 시작")

    while True:  # 게임 루프
        player = choose_character("당신의 캐릭터를 선택하세요: ")
        enemy = choose_character("상대 캐릭터를 선택하세요: ")

        battle = BattleManager(player, enemy)
        winner = battle.start_battle()

        replay = input("\n게임을 다시 하시겠습니까? (y/n): ").lower()
        if replay != "y":
            print("게임을 종료합니다. 감사합니다!")
            break

# 이긴 사람이 전투를 계속 이어 나간다.
