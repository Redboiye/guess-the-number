from difficulty_selection import difficulty_selections

print("Welcome the the number guessing game!!")
print("Time to guess some numbers!!!")
print("Choose difficulty!")

is_incorrect_difficulty = True

while is_incorrect_difficulty == True:
    difficulty = input("1(Easy), 2(Normal) 3(Hard)")
    if difficulty.isnumeric():
        computer_number, is_incorrect_difficulty = difficulty_selections(int(difficulty))
        print(difficulty)
        break
    else:
        continue

print("You have 3 attempts to guess the number")
print("Good luck!")

attempts = 3

while attempts != 0:
    print("You have left", attempts, "attempts")

    while True:
        players_guess = input("make your guess: ")
        if players_guess.isnumeric():
            print("you enter the currect digit!")
            break
        else:

            continue

    if int(players_guess) == computer_number:
        exit("You won")
    else:
        print("Wrong, Guess again!")
        attempts = attempts - 1
