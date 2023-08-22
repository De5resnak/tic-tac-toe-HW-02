import time
import os

score = [0,0]
def start():
    print('Вас приветствует игра "крестики-нолики".\nДля начала игры нажмите 1.\nДля просмотра статистики напишите 2.')
    check = input()
    if check == '1':
        print('Для хода необходимо написать координаты нужной клетки в формате 0-0\nПервыми ходят крестики\nУдачной игры!')
        time.sleep(3)
        os.system('cls')
        play()
    elif check == '2':
        print('Нолики ' + str(score[0])+' : '+str(score[1]) + ' Крестики')
    else:
        print('Введите корректную команду')
        time.sleep(3)
        os.system('cls')
        start()
def play():
    place = [['#','#','#'],['#','#','#'],['#','#','#']]
    win_flag = 0
    its_cross = True
    place_print(place)
    while win_flag == 0:
        moving(its_cross, place)
        its_cross = not its_cross
        os.system('cls')
        place_print(place)
        win_flag = win(place)
    if win_flag == -1:
        print('Нолики победили!!!')
        score[0] += 1
    elif win_flag == 1:
        print('Крестики победили!!!')
        score[1] += 1
    else:
        print('Увы, ничья')
    time.sleep(5)
    os.system('cls')
    start()
def place_print(place):
    for i in place:
        print()
        for j in i:
            print(j, end = ' ')
def moving(its_cross, place):
    print()
    move = input()
    if its_cross and place[int(move[0])][int(move[2])] == '#':
        place[int(move[0])][int(move[2])] = 'x'
    elif place[int(move[0])][int(move[2])] == '#':
        place[int(move[0])][int(move[2])] = 'o'
    else:
        print('Данная клетка занята, введите другое значение')
        moving(its_cross, place)


def win(place):
    # -1 победа o
    # 1 победа x
    # 0 игра еще идет
    # -2 ничья
    for i in place:
        if all(x == 'o' for x in i):
            return -1
        elif all(x == 'x' for x in i):
            return 1
    for i in range (0,3):
        f = []
        for j in range(0,3):
            f.append(place[j][i])
        if all(x == 'o' for x in f):
            return -1
        elif all(x == 'x' for x in f):
            return 1
    d1 = [place[0][0],place[1][1],place[2][2]]
    d2 = [place[0][2],place[1][1],place[2][0]]
    if all(x == 'o' for x in d1) or all(x == 'o' for x in d2):
        return -1
    elif all(x == 'x' for x in d1) or all(x == 'x' for x in d2):
        return 1
    if any('#' in i for i in place):
        return 0
    else:
        return -2





start()