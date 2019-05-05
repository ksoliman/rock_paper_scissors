# Kareem Soliman
# CSC 11300 afternoon
# 12/7/17
# exercise 6
#1)
import random
class Player:
    def __init__(self, name = "cpu"):
        self.name = name
        self.__hand = 'none'

    def set_hand(self, hand):
        self.__hand = hand

    def get_hand(self):
        return self.__hand
        
    def __str__(self):
        return "{}'s last hand was {}".format(self.name, self.get_hand())

class Cpu(Player):

    def __init__(self):
        Player.__init__(self)

    def randomize(self):
        self.set_hand(random.choice(['rock', 'paper', 'scissor']))

name = input("Enter player name: ")
hand = 'none'
while (hand not in ['r','R','p','P','s','S','q','Q']):
    hand = input("\
Enter 'r' for Rock \n\
Enter 'p' for Paper \n\
Enter 's' for Scissor \n\
Enter 'q' to Quit \n\n")

    if (hand not in ['r','R','p','P','s','S','q','Q']):
        print("Invalid Entry! Try Again...\n")

    if (hand in ['q','Q']):
        print("\n\nGoodbye!\n\n")
        exit()

if hand in ['r','R']:
    hand = 'rock'
if hand in ['p','P']:
    hand = 'paper'
if hand in ['s','S']:
    hand = 'scissor'
    
human = Player(name)
human.set_hand(hand)
cpu = Cpu()
cpu.randomize()

if (human.get_hand() == cpu.get_hand()):
    print("{}'s hand is {} and {}'s hand is {}. It's a TIE!".format(human.name, human.get_hand(), cpu.name, cpu.get_hand()))

if (human.get_hand() == 'rock'):
    if (cpu.get_hand() == 'paper'):
        print("{}'s hand is {} and {}'s hand is {}. YOU LOSE!".format(human.name, human.get_hand(), cpu.name, cpu.get_hand()))
    if (cpu.get_hand() == 'scissor'):
        print("{}'s hand is {} and {}'s hand is {}. YOU WIN!".format(human.name, human.get_hand(), cpu.name, cpu.get_hand()))

if (human.get_hand() == 'paper'):
    if (cpu.get_hand() == 'scissor'):
        print("{}'s hand is {} and {}'s hand is {}. YOU LOSE!".format(human.name, human.get_hand(), cpu.name, cpu.get_hand()))
    if (cpu.get_hand() == 'rock'):
        print("{}'s hand is {} and {}'s hand is {}. YOU WIN!".format(human.name, human.get_hand(), cpu.name, cpu.get_hand()))

if (human.get_hand() == 'scissor'):
    if (cpu.get_hand() == 'rock'):
        print("{}'s hand is {} and {}'s hand is {}. YOU LOSE!".format(human.name, human.get_hand(), cpu.name, cpu.get_hand()))
    if (cpu.get_hand() == 'paper'):
        print("{}'s hand is {} and {}'s hand is {}. YOU WIN!".format(human.name, human.get_hand(), cpu.name, cpu.get_hand()))

    
    

        


    
