import game_logic

counter = 0
win = False
while not win:
    game_logic.move('X') if counter % 2 == 0 else game_logic.move('O')
    counter += 1
    if counter > 4:
        if game_logic.win():
            print('Вы выиграли')
            break
    if counter == 9:
        print('Ничья')
        break

