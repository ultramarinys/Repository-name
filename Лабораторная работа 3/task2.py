#  функция find_common_participants
def find_common_participants(participants_first_group, participants_second_group, split_= ","):
    first_group = set(participants_first_group.split(split_))
    second_group = set(participants_second_group.split(split_))

    total_participants = list(first_group.intersection(second_group))
    total_participants.sort()
    return total_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# Работа функции с разделителем отличным от запятой

find_common_participants(participants_first_group, participants_second_group, split_="_")
