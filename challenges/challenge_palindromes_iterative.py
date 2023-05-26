def is_palindrome_iterative(word):
    if not isinstance(word, str) or word == '':
        return False

    w = str(word).lower()

    for i in range(len(w) // 2):
        if w[i] != w[len(w) - i - 1]:
            return False
    return True
