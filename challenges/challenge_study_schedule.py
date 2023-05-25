def study_schedule(permanence_period, target_time):
    if 0 > target_time or target_time > 23:
        return None

    result = 0
    for i in permanence_period:
        if 0 > i[0] or i[0] > 23 or 0 > i[1] or i[1] > 23:
            return None
        elif i[0] <= target_time and target_time <= i[1]:
            result += 1
    return result
