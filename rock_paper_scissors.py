"""
Author: Alex Snow
File name: rock_paper_scissors.py
Last modified: 10/23/26

This is a program that plays a game of rock, paper, scissors.  It takes user input of which choice
then generates a random choice by the computer.  A counter keeps track of who wins each round
to keep track of who has won more games.  To exit the program, the user can type 'quit'"""

import random

#function to allow computer to make a random choice
def computerChoice():
    choices = ["rock", "paper", "scissors"]
    compPick = random.choice(choices)
    return compPick

#function that takes user input
def userChoice():
    while True:
        userInput = input("Do you pick rock, paper or scissors? ").lower()
        if userInput in ["rock", "paper", "scissors"]:
            return userInput
        elif userInput == "quit":   #allows user to exit the game by typing "quit"
            return "quit"
        else:
            print("Please enter valid response.")

#function that determines who has won the game based on their choice
def chooseWinner(computerChoice, userChoice):
    if computerChoice == userChoice:
        return "tie"
    elif computerChoice == "rock" and userChoice == "paper":
        return "user"
    elif computerChoice == "paper" and userChoice == "rock":
        return "computer"
    elif computerChoice == "scissors" and userChoice == "paper":
        return "computer"
    elif computerChoice == "paper" and userChoice == "scissors":
        return "user"
    elif computerChoice == "rock" and userChoice == "scissors":
        return "computer"
    elif computerChoice == "scissors" and userChoice == "rock":
        return "user"

#function that compares user input to random computer generated choice
def playGame():
    userScore = 0
    computerScore = 0

    while True:  #continuous loop that asks for the user's choice unless the user quits the game
        userMove = userChoice()  
        if userMove == "quit":
            print("Thanks for playing!")
            break

        computerMove = computerChoice()

        print("The computer's choice is", computerMove, "and your move is", userMove)

        winner = chooseWinner(computerMove, userMove)

        if winner == "tie":
            print("It's a tie!")
        elif winner == "user":
            print("You won this round!")
            userScore += 1
        else:
            print("The computer won this round!")
            computerScore += 1

        print("Your score = ", userScore)  #prints the running score for user and computer
        print("The computer's score = ", computerScore)

playGame()
        
