# Skeleton Program code for the AQA COMP1 Summer 2015 examination
# this code should be used in conjunction with the Preliminary Material
# written by the AQA COMP1 Programmer Team
# developed in the Python 3.4 programming environment

BOARDDIMENSION = 8
def display_in_game_menu():
  print("Options")
  print("")
  print("1. Save Game")
  print("2. Quit to Menu")
  print("3. Return to Game")
  print("4. Surrender")
  print("")

def get_in_game_menu_selection():
  valid = False
  try:
    while valid == False:
      selection = int(input("Please select an option: "))
      print("")
      if 0 < selection < 5:
        valid = True
      else:
        print("Please enter a valid option")
        valid = False
  except ValueError:
    print("Please enter a valid option")
  return selection

def make_menu_selection(selection):
  if selection == 1:
    pass
  elif selection == 2:
    choice = True
  #  display_menu()
   # option = get_menu_selection()
    #make_selection(option)
  elif selection == 3:
    pass
  elif selection == 4:
    print("")
    print("Surrendering...")
    print("")
    if WhoseTurn == "w":
      print("Black surrendered. White wins!")
    else:
      print("White surrendered. Black wins!")
  return choice

def display_menu():
  print("Main Menu")
  print("")
  print("1. Start new game")
  print("2. Load exsisting game")
  print("3. Play sample game")
  print("4. View high scores")
  print("5. Settings")
  print("6. Quit program")

def get_menu_selection():
  valid = False
  try:
    while valid == False:
      option = int(input("Please select an option: "))
      if 0 < option < 7:
        valid = True
      else:
        print("Please enter a valid option")
        valid = False
  except ValueError:
    print("Please enter a valid option")
  return option

def make_selection(option):
  if option == 1:
    play_game("n")
  elif option == 2:
    print("")
  elif option == 3:
    play_game("y")
  elif option == 4:
    pass
  elif option == 5:
    pass
  elif option == 6:
    exit

  
def GetPieceName(StartRank, StartFile):
  if [StartRank][FinishRank][0] == "W":
    colour = "White"
  elif [StartRank][FinishRank][0] == "B":
    colour = "Black"
  if [StartRank][FinishRank][1] == "R":
    piece = "Redum"
  elif [StartRank][FinishRank][1] == "S":
    piece = "Sarrum"
  elif [StartRank][FinishRank][1] == "M":
    piece = "Marzaz Pani"
  elif [StartRank][FinishRank][1] == "G":
    piece = "Gisgi"
  elif [StartRank][FinishRank][1] == "N":
    piece = "Nabu"
  elif [StartRank][FinishRank][1] == "E":
    piece = "Etlu"
  return colour, piece

def ConfirmMove(StartSquare, FinishSquare):
  start0 = str(StartSquare)[0]
  start1 = str(StartSquare)[1]
  finish0= str(FinishSquare)[0]
  finish1= str(FinishSquare)[1]
  print("move from Rank {0}, File {1} to Rank {2}, File{3}?".format (start0,start1,finish0,finish1))
  move = input("Confirm Move? (y/n)")
  return move.lower()[0]
  

def CreateBoard():
  Board = []
  for Count in range(BOARDDIMENSION + 1):
    Board.append([])
    for Count2 in range(BOARDDIMENSION + 1):
      Board[Count].append("  ")
  return Board

def DisplayWhoseTurnItIs(WhoseTurn):
  if WhoseTurn == "W":
    print("It is White's turn")
  else:
    print("It is Black's turn")
  return WhoseTurn

def GetTypeOfGame():
  TypeOfGame = input("Do you want to play the sample game (enter Y for Yes)? ")
  return TypeOfGame.lower()[0]

def DisplayWinner(WhoseTurn):
  if WhoseTurn == "W":
    print("Black's Sarrum has been captured.  White wins!")
  else:
    print("White's Sarrum has been captured.  Black wins!")

def CheckIfGameWillBeWon(Board, FinishRank, FinishFile):
  if Board[FinishRank][FinishFile][1] == "S":
    return True
  else:
    return False

def DisplayBoard(Board):
  print()
  for RankNo in range(1, BOARDDIMENSION + 1):
    print("     -------------------------")
    print("R{0}".format (RankNo), end="   ")
    for FileNo in range(1, BOARDDIMENSION + 1):
      print("|" + Board[RankNo][FileNo], end="")
    print("|")
  print("     -------------------------")
  print()
  print("     F1 F2 F3 F4 F5 F6 F7 F8")
  print()
  print()    

def CheckRedumMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, ColourOfPiece):
  CheckRedumMoveIsLegal = False
  if ColourOfPiece == "W":
    if FinishRank == StartRank - 1:
      if FinishFile == StartFile and Board[FinishRank][FinishFile] == "  ":
        CheckRedumMoveIsLegal = True
      elif abs(FinishFile - StartFile) == 1 and Board[FinishRank][FinishFile][0] == "B":
        CheckRedumMoveIsLegal = True
  elif FinishRank == StartRank + 1:
    if FinishFile == StartFile and Board[FinishRank][FinishFile] == "  ":
      CheckRedumMoveIsLegal = True
    elif abs(FinishFile - StartFile) == 1 and Board[FinishRank][FinishFile][0] == "W":
      CheckRedumMoveIsLegal = True
  return CheckRedumMoveIsLegal

def CheckSarrumMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  CheckSarrumMoveIsLegal = False
  if abs(FinishFile - StartFile) <= 1 and abs(FinishRank - StartRank) <= 1:
    CheckSarrumMoveIsLegal = True

  return CheckSarrumMoveIsLegal

def CheckGisgigirMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  GisgigirMoveIsLegal = False
  RankDifference = FinishRank - StartRank
  FileDifference = FinishFile - StartFile
  if RankDifference == 0:
    if FileDifference >= 1:
      GisgigirMoveIsLegal = True
      for Count in range(1, FileDifference):
        if Board[StartRank][StartFile + Count] != "  ":
          GisgigirMoveIsLegal = False
    elif FileDifference <= -1:
      GisgigirMoveIsLegal = True
      for Count in range(-1, FileDifference, -1):
        if Board[StartRank][StartFile + Count] != "  ":
          GisgigirMoveIsLegal = False
  elif FileDifference == 0:
    if RankDifference >= 1:
      GisgigirMoveIsLegal = True
      for Count in range(1, RankDifference):
        if Board[StartRank + Count][StartFile] != "  ":
          GisgigirMoveIsLegal = False
    elif RankDifference <= -1:
      GisgigirMoveIsLegal = True
      for Count in range(-1, RankDifference, -1):
        if Board[StartRank + Count][StartFile] != "  ":
          GisgigirMoveIsLegal = False
  return GisgigirMoveIsLegal

def CheckNabuMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  CheckNabuMoveIsLegal = False
  if abs(FinishFile - StartFile) == 1 and abs(FinishRank - StartRank) == 1:
    CheckNabuMoveIsLegal = True
  return CheckNabuMoveIsLegal

def CheckMarzazPaniMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  CheckMarzazPaniMoveIsLegal = False
  if (abs(FinishFile - StartFile) == 1 and abs(FinishRank - StartRank) == 0) or (abs(FinishFile - StartFile) == 0 and abs(FinishRank - StartRank) ==1):
    CheckMarzazPaniMoveIsLegal = True
  if (abs(FinishFile - StartFile) == 1 and abs(FinishRank - StartRank) == 1):
    CheckMarzazPaniMoveIsLegal = True
  return CheckMarzazPaniMoveIsLegal

def CheckEtluMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  CheckEtluMoveIsLegal = False
  if (abs(FinishFile - StartFile) == 2 and abs(FinishRank - StartRank) == 0) or (abs(FinishFile - StartFile) == 0 and abs(FinishRank - StartRank) == 2):
    CheckEtluMoveIsLegal = True
  return CheckEtluMoveIsLegal

def CheckMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn):
  MoveIsLegal = True
  if 0 > FinishRank > BOARDDIMENSION:
    print("That is not a legal move - please try again")
    MoveIsLegal = False
  if 0 > FinishFile > BOARDDIMENSION:
    MoveIsLegal = False
    print("That is not a legal move - please try again")
  try:
    if (FinishFile == StartFile) and (FinishRank == StartRank):
      MoveIsLegal = False
    else:
      PieceType = Board[StartRank][StartFile][1]
      PieceColour = Board[StartRank][StartFile][0]
      if WhoseTurn == "W":
        if PieceColour != "W":
          MoveIsLegal = False
        if Board[FinishRank][FinishFile][0] == "W":
          MoveIsLegal = False
      else:
        if PieceColour != "B":
          MoveIsLegal = False
        if Board[FinishRank][FinishFile][0] == "B":
          MoveIsLegal = False
      if MoveIsLegal == True:
        if PieceType == "R":
          MoveIsLegal = CheckRedumMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, PieceColour)
        elif PieceType == "S":
          MoveIsLegal = CheckSarrumMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
        elif PieceType == "M":
          MoveIsLegal = CheckMarzazPaniMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
        elif PieceType == "G":
          MoveIsLegal = CheckGisgigirMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
        elif PieceType == "N":
          MoveIsLegal = CheckNabuMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
        elif PieceType == "E":
          MoveIsLegal = CheckEtluMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
  except IndexError:
    print("That is not a legal move - please try again")
  return MoveIsLegal

###def InitialiseBoard(Board, SampleGame):
##  if SampleGame == "Y":
##    for RankNo in range(1, BOARDDIMENSION + 1):
##      for FileNo in range(1, BOARDDIMENSION + 1):
##        Board[RankNo][FileNo] = "  "
##    Board[1][2] = "BG"
##    Board[1][4] = "BS"
##    Board[1][8] = "WG"
##    Board[2][1] = "WR"
##    Board[3][1] = "WS"
##    Board[3][2] = "BE"
##    Board[3][8] = "BE"
##    Board[6][8] = "BR"
##  else:
##    for RankNo in range(1, BOARDDIMENSION + 1):
##      for FileNo in range(1, BOARDDIMENSION + 1):
##        if RankNo == 2:
##          Board[RankNo][FileNo] = "BR"
##        elif RankNo == 7:
##          Board[RankNo][FileNo] = "WR"
##        elif RankNo == 1 or RankNo == 8:
##          if RankNo == 1:
##            Board[RankNo][FileNo] = "B"
##          if RankNo == 8:
##            Board[RankNo][FileNo] = "W"
##          if FileNo == 1 or FileNo == 8:
##            Board[RankNo][FileNo] = Board[RankNo][FileNo] + "G"
##          elif FileNo == 2 or FileNo == 7:
##            Board[RankNo][FileNo] = Board[RankNo][FileNo] + "E"
##          elif FileNo == 3 or FileNo == 6:
##            Board[RankNo][FileNo] = Board[RankNo][FileNo] + "N"
##          elif FileNo == 4:
##            Board[RankNo][FileNo] = Board[RankNo][FileNo] + "M"
##          elif FileNo == 5:
##            Board[RankNo][FileNo] = Board[RankNo][FileNo] + "S"
##        else:
##          Board[RankNo][FileNo] = "  "
def InitialiseBoard(Board, SampleGame):
  if SampleGame == "N":
    InitialiseNewBoard(Board)
  elif SampleGame == "Y":
    InitialiseSampleBoard(Board)

    
def InitialiseNewBoard(Board):
  for RankNo in range(1, BOARDDIMENSION + 1):
    for FileNo in range(1, BOARDDIMENSION + 1):
      if RankNo == 2:
        Board[RankNo][FileNo] = "BR"
      elif RankNo == 7:
        Board[RankNo][FileNo] = "WR"
      elif RankNo == 1 or RankNo == 8:
        if RankNo == 1:
          Board[RankNo][FileNo] = "B"
        if RankNo == 8:
          Board[RankNo][FileNo] = "W"
        if FileNo == 1 or FileNo == 8:
          Board[RankNo][FileNo] = Board[RankNo][FileNo] + "G"
        elif FileNo == 2 or FileNo == 7:
          Board[RankNo][FileNo] = Board[RankNo][FileNo] + "E"
        elif FileNo == 3 or FileNo == 6:
          Board[RankNo][FileNo] = Board[RankNo][FileNo] + "N"
        elif FileNo == 4:
          Board[RankNo][FileNo] = Board[RankNo][FileNo] + "M"
        elif FileNo == 5:
          Board[RankNo][FileNo] = Board[RankNo][FileNo] + "S"
      else:
        Board[RankNo][FileNo] = "  "

def InitialiseSampleBoard(Board):
  for RankNo in range(1, BOARDDIMENSION + 1):
      for FileNo in range(1, BOARDDIMENSION + 1):
        Board[RankNo][FileNo] = "  "
  Board[1][2] = "BG"
  Board[1][4] = "BS"
  Board[1][8] = "WG"
  Board[2][1] = "WR"
  Board[3][1] = "WS"
  Board[3][2] = "BE"
  Board[3][8] = "BE"
  Board[6][8] = "BR"

                    
def GetMove(StartSquare, FinishSquare):
  choice = 0
  valid = False
  try:
    while valid == False:
      StartSquare = int(input("Enter coordinates of square containing piece to move (file first): "))
      if StartSquare == -1:
        display_in_game_menu()
        choice = get_in_game_menu_selection()
        choice = int(choice)
        valid = True
      elif len(str(StartSquare)) == 2:
        valid = True
      else:
        print("Please enter FILE and a RANK")
  except ValueError:
    print("Please enter FILE and a RANK")
  valid = False
  if not choice == 2: 
    try:
      while valid == False:
        FinishSquare = int(input("Enter coordinates of square to move piece to (file first): "))
        if FinishSquare == -1:
          display_in_game_menu()
          choice = get_in_game_menu_selection()
          choice = int(choice)
        if len(str(FinishSquare)) == 2:
         valid = True  
        else:
         print("Please enter FILE and a RANK")
    except ValueError:
      print("Please enter FILE and a RANK")
  return StartSquare, FinishSquare, choice

def MakeMove(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn):
  if WhoseTurn == "W" and FinishRank == 1 and Board[StartRank][StartFile][1] == "R":
    Board[FinishRank][FinishFile] = "WM"
    Board[StartRank][StartFile] = "  "
    print("white redum promoted to marzaz pani.")
  elif WhoseTurn == "B" and FinishRank == 8 and Board[StartRank][StartFile][1] == "R":
    Board[FinishRank][FinishFile] = "BM"
    Board[StartRank][StartFile] = "  "
    print("black redum promoted to marzaz pani.")
  else:
    Board[FinishRank][FinishFile] = Board[StartRank][StartFile]
    Board[StartRank][StartFile] = "  "

def play_game(SampleGame):
  quit_program = False
  Board = CreateBoard() #0th index not used
  StartSquare = 0 
  FinishSquare = 0
  PlayAgain = "Y"
  while PlayAgain == "Y" and quit_program == False:
    WhoseTurn = "W"
    GameOver = False
    if ord(SampleGame) >= 97 and ord(SampleGame) <= 122:
      SampleGame = chr(ord(SampleGame) - 32)
      print(SampleGame)
    InitialiseBoard(Board, SampleGame)
    while not(GameOver) and quit_program == False:
      DisplayBoard(Board)
      DisplayWhoseTurnItIs(WhoseTurn)
      MoveIsLegal = False
      while not(MoveIsLegal) and quit_program == False:
        StartSquare, FinishSquare, choice = GetMove(StartSquare, FinishSquare)
        if choice == 2:
          quit_program = True
        else:
          move = ConfirmMove(StartSquare, FinishSquare)
          if move == "y" and quit_program == False:
            StartRank = StartSquare % 10
            StartFile = StartSquare // 10
            FinishRank = FinishSquare % 10
            FinishFile = FinishSquare // 10
            MoveIsLegal = CheckMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn)
            if not(MoveIsLegal):
              print("That is not a legal move - please try again")
            GameOver = CheckIfGameWillBeWon(Board, FinishRank, FinishFile)
            MakeMove(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn)
            if GameOver:
              DisplayWinner(WhoseTurn)
            if WhoseTurn == "W":
              WhoseTurn = "B"
            else:
              WhoseTurn = "W"
    if quit_program == False:
      PlayAgain = input("Do you want to play again (enter Y for Yes)? ")
      if ord(PlayAgain) >= 97 and ord(PlayAgain) <= 122:
        PlayAgain = chr(ord(PlayAgain) - 32)
    
if __name__ == "__main__":
  quit_program = False
  while quit_program == False:
    display_menu()
    option = get_menu_selection()
    make_selection(option)
##  Board = CreateBoard() #0th index not used
##  StartSquare = 0 
##  FinishSquare = 0
##  PlayAgain = "Y"
##  while PlayAgain == "Y":
##    WhoseTurn = "W"
##    GameOver = False
##    SampleGame = GetTypeOfGame()
##    if ord(SampleGame) >= 97 and ord(SampleGame) <= 122:
##      SampleGame = chr(ord(SampleGame) - 32)
##    InitialiseBoard(Board, SampleGame)
##    while not(GameOver):
##      DisplayBoard(Board)
##      DisplayWhoseTurnItIs(WhoseTurn)
##      MoveIsLegal = False
##      while not(MoveIsLegal):
##        StartSquare, FinishSquare = GetMove(StartSquare, FinishSquare)
##        move = ConfirmMove(StartSquare, FinishSquare)
##        if move == "y":
##          StartRank = StartSquare % 10
##          StartFile = StartSquare // 10
##          FinishRank = FinishSquare % 10
##          FinishFile = FinishSquare // 10
##          MoveIsLegal = CheckMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn)
##          if not(MoveIsLegal):
##            print("That is not a legal move - please try again")
##          GameOver = CheckIfGameWillBeWon(Board, FinishRank, FinishFile)
##          MakeMove(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn)
##          if GameOver:
##            DisplayWinner(WhoseTurn)
##          if WhoseTurn == "W":
##            WhoseTurn = "B"
##          else:
##            WhoseTurn = "W"
##    PlayAgain = input("Do you want to play again (enter Y for Yes)? ")
##    if ord(PlayAgain) >= 97 and ord(PlayAgain) <= 122:
##      PlayAgain = chr(ord(PlayAgain) - 32)
##
