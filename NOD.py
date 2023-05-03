def get_nod(a: int, b: int) -> int:
    """
    Поиск наибольшего общего делителя двух натуральных чисел по быстрому алгоритму Евклида
    :param a:
    :param b:
    :return:
    """
    if any((a == 0, b == 0)):
        print("Devision on zero. Exit code:", end = ' ')
        return -1
    a, b = max(a, b), min(a, b)

    while a % b != 0:
        b, a = a % b, b

    return b


# print(get_nod(100, 0))