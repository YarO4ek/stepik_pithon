table = []
teams = {}
points = 0
match_count = 0
victories = 0
draws = 0
losses = 0

i = 0

# Ввод количества матчей

n = int(input())

# Ввод результатов матчей

while i <= n - 1:
    match = str(input())
    table.append(match)
    i += 1

#  создание списка типа ['Зенит', '3', 'Спартак', '1'] и добавление его в словарь для дальнейшей обработки

for i in range(len(table)):
    table[i] = table[i].split(';')
    teams[table[i][0]] = [match_count, victories, draws, losses, points]
    teams[table[i][2]] = [match_count, victories, draws, losses, points]

# Добавление статистики в словарь

for i in range(len(table)):
    # [['Зенит', 3, 'Спартак', 1]]
    table[i][1] = int(table[i][1])
    table[i][3] = int(table[i][3])
    if table[i][1] > table[i][3]:
        teams[table[i][0]][0] += 1
        teams[table[i][0]][1] += 1
        teams[table[i][0]][4] += 3
        teams[table[i][2]][0] += 1
        teams[table[i][2]][3] += 1
    elif table[i][1] < table[i][3]:
        teams[table[i][2]][0] += 1
        teams[table[i][2]][1] += 1
        teams[table[i][2]][4] += 3
        teams[table[i][0]][0] += 1
        teams[table[i][0]][3] += 1
    else:
        teams[table[i][2]][0] += 1
        teams[table[i][2]][2] += 1
        teams[table[i][2]][4] += 1
        teams[table[i][0]][0] += 1
        teams[table[i][0]][2] += 1
        teams[table[i][0]][4] += 1

# Вывод результатов

for fclub, stat in teams.items():
    str_stat = list(map(str, stat))
    print(fclub + ':' + ' '.join(str_stat))