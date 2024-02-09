import random
import TicTacToeAIfile
from termcolor import colored

Board = ["", "","","","","","","",""]
Symbol = "O"
CurrentPlayer = 1
HumanPlayer = 1
AIPlayer = 2

#Human chooses Player
while(True):
    try:
        HumanPlayer = int(input("Which Player do you want to be (1 or 2)? "))
        break
    except(ValueError):
        print("Invalid Input.")
if(HumanPlayer == 1):
    AIPlayer = 2
elif(HumanPlayer == 2):
    AIPlayer = 1
else:
    print("Please enter a valid integer!")
print(colored(f"You are Player {HumanPlayer}!", "green"))


def DrawBoard():
    print("| " + Board[0] + " | " + Board[1] + " | " + Board[2] + " |")
    print("| " + Board[3] + " | " + Board[4] + " | " + Board[5] + " |")
    print("| " + Board[6] + " | " + Board[7] + " | " + Board[8] + " |")

def EndGame(Endstate):
    if(Endstate == 1):
        print(colored("Player 1 wins!", "green"))
    elif(Endstate == 2):
        print(colored("Player 2 wins!", "green"))
    elif(Endstate == 3):
        print(colored("It's a draw!", "grey"))
    exit()

def GetMoves(Board):
    listOfMoves = []
    DictOfMoves = {'1': "", '2': "", '3': "", '4': "", '5': "", '6': "", '7': "", '8': "", '9': ""}
    i=0
    while(i < 9):
        if(Board[i] == ""):
            listOfMoves.append(i)
        i += 1
    return listOfMoves, len(listOfMoves)

def AIMoveRandom(Board):
    PossibleMoves, AmountOfMoves = GetMoves(Board)
    RandomMove = random.randint(0, AmountOfMoves-1)
    """
    print("Amount of Moves: " + str(AmountOfMoves))
    print("PossibleMoves: " + str(PossibleMoves))
    print("ChosenMove: " + str(PossibleMoves[RandomMove]))
    """
    return PossibleMoves[RandomMove]



def PlayMove():
    if(CheckIfEnd(Board) != 0):
        EndGame(CheckIfEnd(Board))

    global CurrentPlayer
    global Symbol
    if(CurrentPlayer == 1):
        Symbol = "O"
    elif(CurrentPlayer == 2):
        Symbol = "X"

    if(CurrentPlayer == HumanPlayer):
        while(True):
            try:
                Move = int(input("Your move (1-9): "))
                Move -= 1
                break
            except (ValueError):
                print("Input must be an integer.")

    elif(CurrentPlayer == AIPlayer):
        print("AI Moves:")
        AIStrenght = 2
        if(AIStrenght == 1):
            Move = TicTacToeAIfile.AIMoveRandom(Board)
        elif(AIStrenght == 2):
            Move = TicTacToeAIfile.AIMoveEndAvoidant(Board, CurrentPlayer)

        #Check if Move is possible
    if(Move > 9 or Move < 0 or Board[Move] != ""):
        print("Move not possible")
        return
        
    #Rewrite Board
    Board[Move] = Symbol
    DrawBoard()

    #Change Player
    if(CurrentPlayer == 1):
        CurrentPlayer = 2
    elif(CurrentPlayer == 2):
        CurrentPlayer = 1
    
    if(CheckIfEnd(Board) != 0):
        EndGame(CheckIfEnd(Board))

def CheckIfEnd(TheBoard):
    #Horizontal check
    ThreeCount = ""
    i=0
    while(i < 3):
        if(TheBoard[i] == "O"):
            ThreeCount = f"{ThreeCount}O"
        elif(TheBoard[i] == "X"):
            ThreeCount = f"{ThreeCount}X"
        i += 1
        if(ThreeCount == "OOO"):
            return(1)
        if(ThreeCount == "XXX"):
            return(2)
    ThreeCount = ""
    while(i < 6):
        if(TheBoard[i] == "O"):
            ThreeCount = f"{ThreeCount}O"
        elif(TheBoard[i] == "X"):
            ThreeCount = f"{ThreeCount}X"
        i += 1
        if(ThreeCount == "OOO"):
            return(1)
        if(ThreeCount == "XXX"):
            return(2)
    ThreeCount = ""
    while(i < 9):
        if(TheBoard[i] == "O"):
            ThreeCount = f"{ThreeCount}O"
        elif(TheBoard[i] == "X"):
            ThreeCount = f"{ThreeCount}X"
        i += 1
        if(ThreeCount == "OOO"):
            return(1)
        if(ThreeCount == "XXX"):
            return(2)
    
    #VerticalCheck
    i=0
    ThreeCount = ""
    while(i < 9):
        if(TheBoard[i] == "O"):
            ThreeCount = f"{ThreeCount}O"
        elif(TheBoard[i] == "X"):
            ThreeCount = f"{ThreeCount}X"
        i += 3
        if(ThreeCount == "OOO"):
            return(1)
        if(ThreeCount == "XXX"):
            return(2)
    i=1
    ThreeCount = ""
    while(i < 10):
        if(TheBoard[i] == "O"):
            ThreeCount = f"{ThreeCount}O"
        elif(TheBoard[i] == "X"):
            ThreeCount = f"{ThreeCount}X"
        i += 3
        if(ThreeCount == "OOO"):
            return(1)
        if(ThreeCount == "XXX"):
            return(2)
    i=2
    ThreeCount = ""
    while(i < 10):
        if(TheBoard[i] == "O"):
            ThreeCount = f"{ThreeCount}O"
        elif(TheBoard[i] == "X"):
            ThreeCount = f"{ThreeCount}X"
        i += 3
        if(ThreeCount == "OOO"):
            return(1)
        if(ThreeCount == "XXX"):
            return(2)
    #Diagonal Check
    i=0
    ThreeCount = ""
    while(i<10):
        if(TheBoard[i] == "O"):
            ThreeCount = f"{ThreeCount}O"
        elif(TheBoard[i] == "X"):
            ThreeCount = f"{ThreeCount}X"
        i += 4
        if(ThreeCount == "OOO"):
            return(1)
        if(ThreeCount == "XXX"):
            return(2)
    i=2
    ThreeCount = ""
    while(i<8):
        if(TheBoard[i] == "O"):
            ThreeCount = f"{ThreeCount}O"
        elif(TheBoard[i] == "X"):
            ThreeCount = f"{ThreeCount}X"
        i += 2
        if(ThreeCount == "OOO"):
            return(1)
        if(ThreeCount == "XXX"):
            return(2)

    #Draw Check
    i=0
    NineCount = 0
    while(i < 9):
        if(TheBoard[i] != ""):
            NineCount += 1
        i += 1
    if(NineCount == 9):
        return(3)
    
    return(0)



def Main():
    while(True):
        PlayMove()

if(__name__ == "__main__"):
    Main()