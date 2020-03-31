import collections
import itertools


def gear_count(str_new_l: dict):
    k = 0
    count = 0
    for item in str_new_l:
        tmp = list(map(int, str(item).split(',')))
        num = str_new_l[item]
        g = collections.Counter(tmp)
        num_most_common_dig = g.most_common(1)[0][1]
        num_dif_dig = len(g.most_common(4))
        if num_most_common_dig == 4:  # все числа одинаковые: AAAA
            count += num
            k += 1
            continue
        if num_most_common_dig == 3:  # одно из чисел встречается трижды: AAAB
            k += 1
            continue
        if num_most_common_dig == 2 and num_dif_dig == 2:  # два числа типа AABB
            count += num
            k += 1
            continue
        if tmp[0] * tmp[1] == tmp[2] * tmp[3] or \
                tmp[0] * tmp[2] == tmp[1] * tmp[3] or \
                tmp[0] * tmp[3] == tmp[1] * tmp[2]:  # ABCD
            count += num
        k += 1
    return count


def gear_num(gears: list, n: int) -> int:
    n = [i for i in range(n)]
    k = 0
    str_new_l = {}
    for item in itertools.combinations(n, 4):  # перестановки индексов, не повторяется набор индексов
        # преобразуем индексы в соответствующие значения
        key = str([gears[item[0]], gears[item[1]], gears[item[2]], gears[item[3]]])[1:-1]

        if key in str_new_l:
            str_new_l[key] = 1 + str_new_l[key]
        else:
            str_new_l[key] = 1

    return gear_count(str_new_l)


if __name__ == '__main__':
    n = int(input().strip())
    gears = list(map(int, input().split()))
    # gears = [1, 1, 1, 1, 2, 10, 20]
    # n = len(gears)
    print(gear_num(gears, n))
