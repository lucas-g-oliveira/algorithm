def study_schedule(permanence_period, target_time):
    if not isinstance(target_time, int) or not isinstance(
        permanence_period, list
    ):
        return None

    result = 0
    for i in permanence_period:
        if not isinstance(i[0], int) or not isinstance(i[1], int):
            return None
        elif i[0] <= target_time and target_time <= i[1]:
            result += 1
    return result
