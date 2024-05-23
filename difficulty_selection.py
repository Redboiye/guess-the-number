import random


def difficulty_selections(difficulty: int):
    computer_number = None
    if difficulty == 1:
        computer_number = random.randint(1, 3)
        is_incorrect_difficulty = False
    elif difficulty == 2:
        computer_number = random.randint(1, 5)
        is_incorrect_difficulty = False
    elif difficulty == 3:
        computer_number = random.randint(1, 10)
        is_incorrect_difficulty = False
    elif difficulty == 666:
        computer_number = random.randint(1, 666)
        is_incorrect_difficulty = False
        print("YOU HAVE UNLOCKED HELL MODE!!!")
    else:
        is_incorrect_difficulty = True
        print("Wrong number,choose again!!")

    return computer_number, is_incorrect_difficulty
