import random  # random 함수를 import해서 가져온다
import time    # time 함수를 import해서 가져온다.


class BattleManager:                            # 클래스 BattleManager함수 사용
    def __init__(self, char1, char2):           # 함수 def 사용 초기화 설정 char1, char2 인스턴스 변수 지정
        self.char1 = char1                      # self 변수 사용 self.char1는 char1 변수로 지정 해준다.
        self.char2 = char2                      # self 변수 사용 self.char2는 char2 변수로 지정 해준다.

    def start_battle(self):  # def 함수 사용 start_battle이라는 것을 지정
        # 프린트 f스트링 사용해서 전투 시작을 알려주고 self.char1.name과 self.char2.name을 지정
        print(f"전투 시작 {self.char1.name} vs {self.char2.name} \n")

        # 공격자와 수비자? 변수 설정을 해서 char1 과 char2를 랜덤 함수를 사용해서 50프로 확률로 공격자와 수비자가 나눠진다.
        attacker, defender = (self.char1, self.char2) if random.random() < 0.5 else (self.char2, self.char1)
        print(f"첫 공격자는 {attacker.name}!\n")  # 위에서 지정된 첫 공격자를 알려주고

        while attacker.is_alive() and defender.is_alive():  # while문으로 공격자가 계속 살아 있거나 방어자가 계속 살아 있으면
            time.sleep(1)   # sleep 인자로 받을 secs만큼 프로그램의 실행을 일시적으로 중지 한다.

            try:    # 에러가 발생 할것 같은곳에서 try를 사용하고
                if random.random() < 0.7:   # if문을 사용해서 random모듈에서 random 함수를 불러온다.
                    print(f"{attacker.name}의 기본 공격!\n")
                    attacker.attack(defender)   # 공격자가 방어자를 공격하게 하고
                else:
                    print(f"{attacker.name}의 특수 공격!\n")
                    attacker.special_attack(defender)
            except Exception as e:  # 위에 try에서 오류가 나면 여기 e라는 변수를 예외처리 해서 넣어라
                print(f"{attacker.name}의 특수 공격 실패: {e}\n")
                attacker.attack(defender)

            if not defender.is_alive():  # 방어자가 쓰러지면 사용되는 if문인데 방어자가 살아있지 않으면이다.
                print(f"\n{defender.name}은(는) 쓰러졌다!\n{attacker.name} 승리!\n")
                break

            attacker, defender = defender, attacker  # 변수값 교환 공격자는 방어자로 방어자는 공격자로
