#!/usr/bin/env python3
import random
import time
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


def pprint(text, t=1.5):  # pprint stands for Pause_Print
    print(text)
    time.sleep(t)


class Player:
    def __init__(self, name):
        self.name = name

    def move(self):
        self.choice = 'rock'
        return 'rock'

    def learn(self, Hu_move, Cpu_move):  # idid a little bit changes to var
        #                                  names so it's more clear
        self.Hu_move = Hu_move
        self.Cpu_move = Cpu_move


class RandomPlayer(Player):
    def __init__(self, name):
        self.name = name

    def move(self):
        self.choice = random.choice(moves)
        return self.choice


class HumanPlayer(Player):
    def __init__(self, name):
        self.name = name

    def move(self):
        while True:
            self.choice = input('what do you want to choose ? ').lower()
            if self.choice in moves:
                break
            else:
                print("sorry i didn't understand, please type again ")
        return self.choice


class ReflectPlayer(Player):
    def __init__(self, name):
        self.name = name
        self.Hu_move = random.choice(moves)  # we need this, otherwize
        #                                  ReflectPlayer wont know what to play

    def move(self):
        self.choice = self.Hu_move
        return self.choice


class CyclePlayer(Player):
    def __init__(self, name):
        self.name = name
        self.Cpu_move = random.choice(moves)  # we need this, otherwize
        #                                  CyclePlayer wont know what to play

    def move(self):
        self.choice = self.Cpu_move
        if self.choice == 'rock':
            return 'paper'
        if self.choice == 'paper':
            return 'scissors'
        else:
            return 'rock'


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


def winner(p1, p1score, p2, p2score):
    if p1score > p2score:
        pprint(f'{p1} is the Winner!')
        pprint(f'Scores: p1 {p1score} | p2{p2score}', 2)

    elif p1score < p2score:
        pprint(f'{p2} is the Winner!', 2)
        pprint(f'Scores: p1 {p1score} | p2 {p2score}', 2)
    else:
        pprint('Its a tie', 2)


def check_winner(round, p1, p1score, p2, p2score):
    if round == 1:
        p1score += 1
        pprint(f'{p1} Wins!')
        pprint(f'scores p1 {p1score} | p2 {p2score}')
        return p1score, p2score
    elif round == -1:
        p2score += 1
        pprint(f'{p2} Wins!')
        pprint(f'scores p1 {p1score} | p2 {p2score}')
        return p1score, p2score
    else:
        pprint('Draw')
        pprint(f'scores p1 {p1score} | p2 {p2score}')
        return p1score, p2score


class Game(Player):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        self.p1.learn(move1, move2)
        self.p2.learn(move1, move2)
        pprint(f"Player1: {move1}  Player2: {move2}", 2)
        if beats(move1, move2):
            return 1
        elif move1 == move2:
            return 0
        else:
            return -1

    def play_game(self):
        p1score = 0
        p2score = 0
        pprint(f'hi {self.p1.name} .')
        pprint('game Rules: who scores 3 Wins')
        pprint("Game start!")
        rounds = 1
        while p1score != 3 and p2score != 3:
            pprint(f"Round {rounds}:")
            round = self.play_round()
            p1score, p2score = check_winner(round,
                                            self.p1.name, p1score,
                                            self.p2.name, p2score)
            rounds += 1

        winner(self.p1.name, p1score, self.p2.name, p2score)
        pprint("Game over!")


if __name__ == '__main__':
    name = input('please choose your name: ')
    p1 = HumanPlayer(name)
    while True:
        p2 = input('choice your player: random, reflect, or cycle.')
        if p2.lower() == 'random':
            p2 = RandomPlayer('Cpu')
            break
        if p2.lower() == 'reflect':
            p2 = ReflectPlayer('Cpu')
            break
        if p2.lower() == 'cycle':
            p2 = CyclePlayer('Cpu')
            break
        pprint('sorry i didnt understand, try again')
    game = Game(p1, p2)
    game.play_game()
