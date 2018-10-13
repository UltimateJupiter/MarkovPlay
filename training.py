
from tqdm import tqdm


def weight_calc(dic):
    new = [[], []]
    total = sum(dic.values())
    for x in dic:
        new[0].append(x)
        new[1].append(dic[x] / total)
    return new


def train(sample_length, text):
    model = dict()
    print("training text length: {}".format(len(text)))
    for i in tqdm(range(len(text) - sample_length)):
        # print(i, i + sample_length)
        target_text = text[i: i + sample_length]

        next_char = text[i + sample_length: i + sample_length + 1]
        if target_text not in model:
            model[target_text] = {}
        if next not in model[target_text]:
            model[target_text][next_char] = 0
        model[target_text][next_char] += 1

    weighted_model = {}
    for x in model:
        weighted_model[x] = weight_calc(model[x])

    # print(weighted_model)
    return weighted_model
