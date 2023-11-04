users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

sum_users = len(users)
unique_users = len(set(users))
dict_visits = {"Общее количество": sum_users,
          "Уникальные посещения" : unique_users,
}
print(dict_visits)
