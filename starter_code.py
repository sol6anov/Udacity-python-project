#!/usr/bin/env python3

'#game of Rock, Paper, Scissors'
import random

'#A list of play options'
moves = ['rock', 'paper', 'scissors']

'#A list of game styles'
styles = ['random', 'reflect', 'cycle', 'rocker', 'q']

'#parent class'


class Player:
    def my_move(self):
        return "paper"

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.my_last_move = my_move
        self.opponent_move = their_move


class Human_player(Player):
    def my_move(self):
        my_move = input('Please enter your choice either '
                        '\033[0;34;47m[rock, paper or'
                        ' scissors]:\033[0m\n').lower()
        while my_move not in moves:
            print("\033[1;31;40m Non existing move,"
                  "please retype your move again or "
                  "\033[0;33;100m 'q' \033[1;31;40m "
                  " to Exit \033[0m\033[0m")
            my_move = input('Please enter either\033[0;34;47m'
                            '[rock, paper or scissors]'
                            '\033[0m:\n').lower()
            if my_move == 'q':
                exit()
        return my_move


class Random_player(Player):
    def their_move(self):
        return random.choice(moves)


class Rocker_player(Player):
    def their_move(self):
        return self.move()


class Cycle_player(Player):

    def __init__(self):
        self.cycle = 0

    def their_move(self):
        if self.cycle == 2:
            self.cycle = 0
        else:
            self.cycle = self.cycle + 1
        return moves[self.cycle - 1]


class Reflect_player(Player):
    def __init__(self):
        self.move2 = ""

    def their_move(self):
        if self.move2 is "":
            return random.choice(moves)

        return self.move2

    def learn(self, my_move, their_move):
        self.move2 = my_move


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game (Player):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.OPPONENT_SCORE = 0
        self.YOUR_SCORE = 0

    def play_round(self):
        move1 = self.p1.my_move()
        move2 = self.p2.their_move()
        print(f"Player 1: {move1}  Player 2: {move2}")

        if move1 == move2:
            print("\n")
            print("\033[1;33;40m Tie Round \033[0m")
        elif beats(move1, move2):
            self.YOUR_SCORE = self.YOUR_SCORE + 1
            print("\n")
            print("\033[1;32;40m You Have Won This Round \033[0m")
        elif beats(move2, move1):
            self.OPPONENT_SCORE = self.OPPONENT_SCORE + 1
            print("\n")
            print("\033[1;31;40m Opponent Has Won This round \033[0m")
        self.p2.learn(move1, move2)

    def play_game(self):
        print("-------------")
        print("\033[3;37;1mGame start!\033[0m")
        print("-------------")
        print("\n")
        for round in range(1, 4):
            print(f"\033[1;36;40m Round { round }:\033[0m")
            self.play_round()
            print(f"\033[0;32;100m Your Score[{self.YOUR_SCORE}]\033[0m")
            print(f"\033[0;33;100m Opponent Score[{self.OPPONENT_SCORE}]"
                   "\033[0m")
            print("\n")
        print("\n")
        print(f"\033[0;34;47m------------Final Score------------\033[0m")
        print("\n")
        print(f"\033[0;34;47m Your Score     [{self.YOUR_SCORE}]\033[0m")
        print(f"\033[0;34;47m Opponent Score [{self.OPPONENT_SCORE}]\033[0m")
        print("\n")
        if self.YOUR_SCORE > self.OPPONENT_SCORE:
            print("\033[1;32;40m (( You Have Won The Game )) \033[0m \n")
            print("\n")
        elif self.YOUR_SCORE < self.OPPONENT_SCORE:
            print("\033[1;31;40m (( Opponent Has Won The Game )) \033[0m\n")
            print("\n")
        else:
            print("\033[1;33;40m (( Tie Game )) \033[0m \n")
            print("\n")
        print("-------------")
        print("\033[3;37;1m Game over!\033[0m")
        print("-------------")
        print("\n")
        restart = input("\033[0;37;100m  Would you like"
                        " to play again?\033[0m \n"
                        "\033[3;37;1m Press  ' y ' to"
                        "\033[1;32;40m Continue \033[0m"
                        "\n\033[3;37;1m  Enter To "
                        "\033[1;31;40m Exit \033[0m\n\n").lower()
        if restart == "y":
            self.play_game()
        else:
            print("\033[0;35;47m Good Luck\033[0m")
            exit()
if __name__ == '__main__':
    PlayStyle = ""
    while PlayStyle not in styles:
        PlayStyle = input("Please select the game style, \033[0;31;47m"
                          "[random, reflect, cycle, rocker]:\033[0m \n "
                          "\033[0;33;100m 'q' to \033[1;31;40m Exit"
                          "\033[0m \n \n").lower()
        if PlayStyle == 'q':
            exit()
        else:
            pass
    if PlayStyle == 'random':
        game = Game(Human_player(), Random_player())
    elif PlayStyle == 'reflect':
        game = Game(Human_player(), Reflect_player())
    elif PlayStyle == 'cycle':
        game = Game(Human_player(), Cycle_player())
    elif PlayStyle == 'rocker':
        game = Game(Human_player(), Rocker_player())

    game.play_game()
