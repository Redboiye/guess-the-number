import random


class Match:
    def __init__(
            self,
            difficulty,
    ):

        self.difficulty = difficulty
        self.computer_number = None
        self.difficulty_selections()
        self.is_incorrect_difficulty = True
        self.attempts = 3

    def difficulty_selections(self):
        if self.difficulty == 1:
            self.computer_number = random.randint(1, 3)
            self.is_incorrect_difficulty = False
        elif self.difficulty == 2:
            self.computer_number = random.randint(1, 5)
            self.is_incorrect_difficulty = False
        elif self.difficulty == 3:
            self.computer_number = random.randint(1, 10)
            self.is_incorrect_difficulty = False
        elif self.difficulty == 666:
            self.computer_number = random.randint(1, 666)
            self.is_incorrect_difficulty = False
            print("YOU HAVE UNLOCKED HELL MODE!!!")
        else:
            self.is_incorrect_difficulty = True
            print("Wrong number,choose again!!")

    def play(self):
        print("You have 3 attempts to guess the number")
        print("Good luck!")

        while self.attempts != 0:
            print("You have left", self.attempts, "attempts")
            player_guess = self.get_player_guess()

            if player_guess == self.computer_number:
                print("You won")
                return True
            else:
                print("Wrong, Guess again!")
                self.attempts -= 1

        print("You've have run out of attempts. The correct number was:", self.computer_number)
        return False


    @staticmethod
    def get_player_guess():
        while True:
            player_guess = input("make your guess: ")
            if player_guess.isnumeric():
                print("you enter the correct digit!")
                return int(player_guess)
            else:
                print("Please enter a valid number.")


def choose_difficulty():
    is_incorrect_difficulty = True
    while is_incorrect_difficulty == True:
        difficulty = input("1(Easy), 2(Normal) 3(Hard)")
        if difficulty.isnumeric():
            is_incorrect_difficulty = False
            return int(difficulty), is_incorrect_difficulty
        else:
            print("Wrong difficulty. Choose again")


class Game:
    def __init__(self):
        print("Welcome the the number guessing game!!")
        print("Time to guess some numbers!!!")

    def start_game(self):
        difficulty, is_incorrect_difficulty = choose_difficulty()
        if not is_incorrect_difficulty:
            match = Match(difficulty)
            match.play()
            if not self.play_again():
                print("thank you for playing!")

    @staticmethod
    def play_again():
        while True:
            choice = input("Do you want to play again? 'y' or 'n'.")
            if choice is 'y':
                return True
            else:
                exit("thanks for playing")
