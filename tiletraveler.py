""" með tvo int: char_x og char_y sem tilgreinir hvar character er
    if( x og y) þá hvað: m.v. aðstæður á hverjum stað fyrir sig
    þegar character nær inn í 3.1 þá victory
    í hverri loopu skrifast út status update, you can travel: 
    (set upp git)
    (N)orth
    (S)outh
    (W)est
    (E)ast

    """

#FASTAR


char_x, char_y = 1, 1
path = ""


#Rooms fall
room1_1 = "(N)orth"; room1_2 = "(N)orth, (E)ast, (S)outh"; room1_3 = "(S)outh, (E)ast"
room2_1 = "(N)orth"; room2_2 = "(W)est, (S)outh"; room2_3 = "(E)ast, (W)est"
room3_1 = "(N)orth"; room3_2 = "(N)orth, (S)outh"; room3_3 = "(N)orth"

path = room1_1

while 1:
    print("You can travel: " + path)
    path = ''
    direction = input("Direction: ").lower()
    
#dir mover(direction):

    if (direction == 'n') and (char_y < 3):
        char_y += 1
    elif (direction == 's') and (char_y > 1):
        char_y -= 1
    elif (direction == 'e') and (char_x < 3):
        char_x += 1
    elif (direction == 'w') and (char_x > 1):
        char_x -= 1
    else:
        print("Not a valid direction!")
        # return char_x, char_y


    print("Current location",char_x, char_y)

    if char_x == 1 and char_y == 1: path = room1_1
    elif char_x == 1 and char_y == 2: path = room1_2
    elif char_x == 1 and char_y == 3: path = room1_3
    elif char_x == 2 and char_y == 1: path = room2_1
    elif char_x == 2 and char_y == 2: path = room2_2
    elif char_x == 2 and char_y == 3: path = room2_3
    elif char_x == 3 and char_y == 1: path = room3_1; print("Victory!"); break
    elif char_x == 3 and char_y == 2: path = room3_2
    elif char_x == 3 and char_y == 3: path = room3_3
    





