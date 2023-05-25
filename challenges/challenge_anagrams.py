def quick_sort(word: str):
    if len(word) <= 1:
        return word
    pivo = word[len(word) // 2]
    menor, igual, maior = "", "", ""

    for i in word:
        if i < pivo:
            menor += i
        elif i == pivo:
            igual += i
        else:
            maior += i

    menor = quick_sort(menor)
    maior = quick_sort(maior)
    return menor + igual + maior


def is_anagram(first_string, second_string):
    if first_string == "" or second_string == "":
        return False
    first = quick_sort(str(first_string).lower())
    second = quick_sort(str(second_string).lower())

    return (first, second, first == second)
