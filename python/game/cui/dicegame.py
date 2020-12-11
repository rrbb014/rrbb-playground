import random

middle_dot = chr(0xb7)    # U+00B7 -> 16 * 11 + 7 -> 183

player_position = 1
computer_position = 1

def board():
    print(middle_dot*(player_position - 1) +
            "P" +
            middle_dot * (30 - player_position) + "GOAL"
    ) 
    print(middle_dot * (computer_position - 1) +
            "C" +
            middle_dot * (30 - computer_position) + "GOAL"
    )

if __name__ == "__main__":
    board()
    print("주사위게임 START")
    while True:
        input("Enter를 누르면 여러분의 말이 움직입니다.")
        player_position += random.randint(1, 6)
        if player_position > 30:
            player_position = 30
        board()
        if player_position == 30:
            print("여러분의 승리")
            break

        input("Enter를 누르면 컴퓨터의 말이 움직입니다.")
        computer_position += random.randint(1, 6)
        if computer_position > 30:
            computer_position = 30
        board()
        if computer_position == 30:
            print("컴퓨터의 승리")
            break
