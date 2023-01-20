# Создайте программу для игры в ""Крестики-нолики"". 
# Игра реализуется в терминале, игроки ходят поочередно, необходимо вывести 
# карту(как удобнее, можно например в виде списка, внутри которого будут 3 списка по 3 
# элемента, каждый из которого обозначает соответсвующие клетки от 1 до 9), сделать 
# проверку не занята ли клетка, на которую мы хотим поставить крестик или нолик, 
# и проверку на победу( стоят ли крестики или нолик в ряд по диагонали, вертикали, горизонтали)
import random

map = [1, 2, 3, 4, 5, 6, 7, 8, 9]

victory_options = [[0,3,6],[1,4,7],[2,5,8],[0,1,2],[3,4,5],[6,7,8],[0,4,8],[2,4,6]]

def map_output():
    for i in range(0,9):
        if i % 3 == 0:
            print(end = '\n')
        print(map[i], end=' ')
    print(end ='\n')

def victory():
    for i in victory_options:
        if map[i[0]] == map[i[1]] == map[i[2]]:
            return True
    return False
map_output()

user1 = input('Имя игрока под номером 1: ')
user2 = input('Имя игрока под ноиером 2: ')

player1 = 'X'
player2 = 'O'

who_is_first = random.choice([user1,user2])

who_play_now = who_is_first

count = 0
while True:
    print(f'Ходит {who_play_now}')
    if who_play_now == who_is_first:
        step = int(input('введите, куда хотите походить от 1 до 9\n'))
        if map[step - 1] in ['X','O']:
            print('Сюда уже ходили')
            continue
        map[step-1] = player1
    else:
        step = int(input('введите, куда хотите походить от 1 до 9\n'))
        if map[step - 1] in ['X','O']:
            print('Сюда уже ходили')
            continue
        map[step-1] = player2
    map_output()
    if victory() == True:
        print(f'Победа игрока {who_play_now}')
        break
    count += 1
    if who_play_now == user1:
        who_play_now = user2
    else:
        who_play_now = user1
    if count == 9:
        print('Ничья')
        break