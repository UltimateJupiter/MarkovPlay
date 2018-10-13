from pre_analysis import get_text
from training import train
import numpy as np
import sys
import time
from binary_choice import choice
from IPython import embed


def text_gen(length, basemodel):
    text_base = u"孙少平在农村长大，深刻认识这黄土地上养育出来的人"
    for x in basemodel:
        mark = len(x)
        break
    text = text_base[:mark]
    print(text, end="")
    while 1:
        # print(text)
        # print(basemodel[text])

        new_ind = "asdfghjk"
        # embed()
        while (text + new_ind)[-mark:] not in basemodel:
            new_ind = choice(basemodel[text[-mark:]][0], basemodel[text[-mark:]][1])
        print(new_ind, end='')
        time.sleep(np.random.random()/10)

        text += new_ind
        if new_ind == "\n":
            if len(text) > length:
                break
    return text


def main():
    text = get_text()
    basemodel = train(sample_length=5, text=text)
    text_gen(400, basemodel)


main()