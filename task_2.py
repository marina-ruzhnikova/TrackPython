def find_common_participants(group1, group2, separator = "," ):
    set_words1 = set(group1.split(separator))
    set_words2 = set(group2.split(separator))
    common_participants = set_words1.intersection(set_words2)
    common_participants = list(common_participants)
    common_participants.sort()
    return common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

find_common_participants(participants_first_group, participants_second_group, "|")
