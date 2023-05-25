def is_palindrome_recursive(word, low_index, high_index):
    w, l, h = [word, low_index, high_index]

    if word == "":
        return False
    if w[l] == w[h] and h - l > 0:
        print(f"l: {w[l]} - r: {w[h]}")
        return is_palindrome_recursive(word, l + 1, h - 1)
    elif w[l] != w[h]:
        return False
    else:
        return True
