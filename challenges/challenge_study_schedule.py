def study_schedule(permanence_period, target_time):
    if not isinstance(target_time, int) or not isinstance(
        permanence_period, list
    ):
        return None

    result = 0
    for i in permanence_period:
        if 0 > i[0] or i[0] > 23 or 0 > i[1] or i[1] > 23:
            return None
        elif i[0] <= target_time and target_time <= i[1]:
            result += 1
    return result


lista = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]
hour = 2
print(study_schedule(lista, "x"))
