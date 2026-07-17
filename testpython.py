def board(entries_list):
    n1,n2,n3,n4,n5,n6,n7,n8,n9 = entries_list
    print(f"""
________________
|{n1}|{n2}|{n3}|
|____|____|____|
|{n4}|{n5}|{n6}|
|____|____|____|
|{n7}|{n8}|{n9}|
|____|____|____|
""")
Game_running = True
mainarr = ['    ','    ','    ','    ','    ','    ','    ','    ','    ']
while Game_running:
    player1play = True
    while player1play:
        player1arr = ['    ','    ','    ','    ','    ','    ','    ','    ','    ']
        player1input = int(input('Enter[X](FROM 0 TO 8): '))
        if mainarr[player1input] == '    ':
            player1arr[player1input] = ' X  '
            mainarr[player1input] = ' X  '
            board(mainarr)
            player1play = False
        else:
            print('there is some value present already')
    player2play = True
    
    if (mainarr[0] == mainarr [1] == mainarr[2] == ' X  ') or (mainarr[3] == mainarr [4] == mainarr[5] == ' X  ') or (mainarr[6] == mainarr [7] == mainarr[8] == ' X  ') or (mainarr[0] == mainarr [3] == mainarr[6] == ' X  ') or (mainarr[1] == mainarr [4] == mainarr[7] == ' X  ') or (mainarr[2] == mainarr [5] == mainarr[8] == ' X  ') or (mainarr[0] == mainarr [4] == mainarr[8] == ' X  ') or (mainarr[2] == mainarr [4] == mainarr[6] == ' X  '):
        Game_running = False
        player2play = False
    while player2play:
        player2arr = ['    ','    ','    ','    ','    ','    ','    ','    ','    ']
        player2input = int(input('Enter[O](FROM 0 TO 8): '))
        if mainarr[player2input] == '    ':
            player1arr[player2input] = ' O  '
            mainarr[player2input] = ' O  '
            board(mainarr)
            player2play = False
        else:
            print('there is some value present already')
    if (mainarr[0] == mainarr [1] == mainarr[2] == ' O  ') or (mainarr[3] == mainarr [4] == mainarr[5] == ' O  ') or (mainarr[6] == mainarr [7] == mainarr[8] == ' O  ') or (mainarr[0] == mainarr [3] == mainarr[6] == ' O  ') or (mainarr[1] == mainarr [4] == mainarr[7] == ' O  ') or (mainarr[2] == mainarr [5] == mainarr[8] == ' O  ') or (mainarr[0] == mainarr [4] == mainarr[8] == ' O  ') or (mainarr[2] == mainarr [4] == mainarr[6] == ' O  '):
        print('you have won the game')
        Game_running = False
        player2play = False