"""
Даны три стержня, на один из которых нанизаны диски, причем диски отличаются
размером и лежат меньший на большем. Задача состоит в том, чтобы перенести
пирамиду из дисков на другой стержень за наименьшее число ходов (рис. 14.1).
При этом действуют три ограничения.
1. Диски можно перемещать по одному.
2. Игрок может перекладывать диски только с верха стопки на верх другой
стопки.
3. Нельзя переложить больший диск на меньший.

"""
SOLVED_TOWER = [5, 4, 3, 2, 1]

tower_A = [5, 4, 3, 2, 1]
tower_B = []
tower_C = []

game = True

while game:

    for level in (5, 4, 3, 2, 1, 0):
        for tower in (tower_A, tower_B, tower_C):
            if level >= len(tower):
                # Вывести сегмент стержня без диска:
                width = 0
                emptySpace = " " * (5 - width)
                print(f"{emptySpace}||{emptySpace}", end="")
            else:
                # Вывести диск:
                width = tower[level]
                emptySpace = " " * (5 - width)
                disk_pic = "@" * width
                numLabel = str(width).rjust(2, "_")  # https://pythonstart.ru/string/ljust-rjust
                print(f"{emptySpace}{disk_pic}{numLabel}{disk_pic}{emptySpace}", end="")
        print()

    print(" " * 6 + "A" + " " * 5 + " " * 6 + "B" + " " * 5 + " " * 6 + "C" + " " * 5)

    if SOLVED_TOWER in (tower_B, tower_C):
        game = False
        break

    user_move = input("Введите букву стержня откуда и букву стержня куда будет перемещаться диск:")  # "AB"
    from_tower = user_move[0]
    to_tower = user_move[1]

    disk = None
    if from_tower == "A":
        disk = tower_A.pop()
    elif from_tower == "B":
        disk = tower_B.pop()
    elif from_tower == "C":
        disk = tower_C.pop()

    if to_tower == "A":
        tower_A.append(disk)
    elif to_tower == "B":
        tower_B.append(disk)
    elif to_tower == "C":
        tower_C.append(disk)

print("WIN")
