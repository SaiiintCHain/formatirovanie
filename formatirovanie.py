# Использование %
team1_num = 5
team2_num = 6
print('В команде Мастера кода участников: %s ' % '5')
print('В команде Мастера кода участников: %s и %d' % ('5', team2_num))

# Использование format()
score_2 = 42
team1_time = 1552.512
print("Команда Волшебники данных решила задач: {}".format(42))
print("Волшебники данных решили задачи за {} !".format(1552.512))

# Использование f-строк
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
print(f'Команды решили {score_1} и {score_2} задач.')
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = 'Победа команды Волшебники Данных!'
else:
    challenge_result = 'Ничья!'
print(f'{challenge_result}')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')