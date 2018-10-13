import pre_analysis
from training import train
import numpy as np
import sys
import time
from binary_choice import choice
from IPython import embed


def text_gen(length, basemodel, text_base):

    for x in basemodel:
        mark = len(x)
        break
    text = text_base[:mark]
    print(text, end="")
    while 1:

        new_ind = "yffyiyfiyfi"

        while (text + new_ind)[-mark:] not in basemodel:
            new_ind = choice(basemodel[text[-mark:]][0], basemodel[text[-mark:]][1])
        print(new_ind, end='')
        # time.sleep(np.random.random()/10)

        text += new_ind
        if new_ind == "\n":
            if len(text) > length:
                break
    return text


def main():

    # text, start = pre_analysis.get_text_three_body()
    text, start = pre_analysis.get_text_three_kindom()
    basemodel = train(sample_length=3, text=text)
    text_gen(1900, basemodel, start)


main()