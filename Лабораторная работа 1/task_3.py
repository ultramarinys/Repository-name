list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

players_in_team = len(list_players)//2
list1 = list_players[0:players_in_team] # участники первой команды
list2 = list_players[players_in_team:] # участники второй команды

print(list1)
print(list2)
