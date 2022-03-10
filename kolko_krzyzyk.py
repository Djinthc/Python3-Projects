import random
wolnePola = []
board = [["1","2","3",],
         ["4","x","6",],
         ["7","8","9"]]


#-------------------------------------------------------------------------------#
#display_board(board)

def display_board(board):
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ",board[0][0],"  |  ",board[0][1],"  |  ",board[0][2],"  |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ",board[1][0],"  |  ",board[1][1],"  |  ",board[1][2],"  |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ",board[2][0],"  |  ",board[2][1],"  |  ",board[2][2],"  |")
    print("|       |       |       |")
    print("+-------+-------+-------+")

#-------------------------------------------------------------------------------#
# Funkcja, ktora przyjmuje parametr odzwierciedlajacy biezacy stan tablicy,
# prosi uzytkownika o wykonanie ruchu, 
# sprawdza dane wejsciowe i aktualizuje tablice zgodnie z decyzja uzytkownika.

def enter_move(board):
    mo1 = int(input("Podaj rząd: "))
    mo2 = int(input("Podaj kolumnę: "))
    if mo1 <1 or mo1>3 or mo2 <1 or mo2>3:
        print("Błędna wartość")
        mo1 = int(input("Podaj rząd: "))
        mo2 = int(input("Podaj kolumnę: "))
    board[mo1 -1][mo2 -1] = "o"

#-------------------------------------------------------------------------------#
# Funkcja, ktora przeglada tablice i tworzy liste wszystkich wolnych pol; 
# lista sklada sie z krotek, a kazda krotka zawiera pare liczb odzwierciedlajacych rzad i kolumne.

def make_list_of_free_fields(board):
    
    for pole in board:
        for i in pole:
            if i == "x" or i == "o":
                continue
            elif i == '1':
                wolnePola.append((0,0))
            elif i == '2':
                wolnePola.append((0,1))
            elif i == '3':
                wolnePola.append((0,2))
            elif i == '4':
                wolnePola.append((1,0))
            elif i == '6':
                wolnePola.append((1,2))
            elif i == '7':
                wolnePola.append((2,0))
            elif i == '8':
                wolnePola.append((2,1))
            elif i == '9':
                wolnePola.append((2,2))
            else:
                continue
            





   



#-------------------------------------------------------------------------------#
# Funkcja, ktora dokonuje analizy stanu tablicy w celu sprawdzenia
# czy uzytkownik/gracz stosujacy "O" lub "X" wygral rozgrywke.
def victory_for(board):
    if board[0][0] == "x" and board[0][1] =="x" and board[0][2] =="x"\
    or board[1][0] == "x" and board[1][1] =="x" and board[1][2] =="x"\
    or board[2][0] == "x" and board[2][1] =="x" and board[2][2] =="x"\
    or board[0][0] == "x" and board[1][0] =="x" and board[2][0] =="x"\
    or board[0][1] == "x" and board[1][1] =="x" and board[2][1] =="x"\
    or board[0][2] == "x" and board[1][2] =="x" and board[2][2] =="x"\
    or board[0][0] == "x" and board[1][1] =="x" and board[2][2] =="x"\
    or board[0][2] == "x" and board[1][1] =="x" and board[2][0] =="x":
        return True
        print("Przegrałeś")
    elif board[0][0] == "o" and board[0][1] =="o" and board[0][2] =="o"\
    or board[1][0] == "o" and board[1][1] =="o" and board[1][2] =="o"\
    or board[2][0] == "o" and board[2][1] =="o" and board[2][2] =="o"\
    or board[0][0] == "o" and board[1][0] =="o" and board[2][0] =="o"\
    or board[0][1] == "o" and board[1][1] =="o" and board[2][1] =="o"\
    or board[0][2] == "o" and board[1][2] =="o" and board[2][2] =="o"\
    or board[0][0] == "o" and board[1][1] =="o" and board[2][2] =="o"\
    or board[0][2] == "o" and board[1][1] =="o" and board[2][0] =="o":
        return True
        print("Wygrałeś! Gratulacje!")
    else:
        return False
    
 

#-------------------------------------------------------------------------------#
# Funkcja, ktora wykonuje ruch za komputer i aktualizuje tablice.
def draw_move(board):
    move = random.choice(wolnePola)
    board[move[0]][move[1]] = "x"
    

#def draw_move(board):
#    if 







#---------------------------------------------------------#
### Czas zagrać !


while victory_for(board) == False:
    display_board(board)
    enter_move(board)
    display_board(board)
    make_list_of_free_fields(board)
    draw_move(board)
    



        
   














    
