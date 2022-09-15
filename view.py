table = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def draw_table():
    for row in table:
        print(' | '.join(list(map(str, row))))
        print('_'*10)
    return table
