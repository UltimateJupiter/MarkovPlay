from numpy.random import random
import time


def choice(ls_key, ls_weight):

    assert len(ls_key) == len(ls_weight), (ls_key, ls_weight)

    if len(ls_key) == 1:
        return ls_key[0]

    ls_aw = [ls_weight[0]]
    for x in range(len(ls_weight) - 1):
        ls_aw.append(ls_aw[-1] + ls_weight[x + 1])

    for x in range(len(ls_aw)):
        ls_aw[x] /= ls_aw[-1]

    begin, end = 0, len(ls_aw)
    rand = random()

    while end - begin > 1:
        # print(end, begin)
        # time.sleep(0.05)
        mid = int((begin + end) / 2)
        if ls_aw[mid] < rand:
            begin = mid
        else:
            end = mid

    if end - rand < rand - begin:
        return ls_key[end]
    else:
        return ls_key[begin]
