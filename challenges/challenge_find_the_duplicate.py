def find_duplicate(nums):
    isvalid = isinstance(nums, list) and len(nums) > 1
    isvalid = (isvalid and isinstance(nums, str))

    if isvalid:
        return True

    return False
