#!/usr/bin/python
# -*- coding: UTF-8 -*-


def parentheses_removal(string):

    mark = True
    out_string = ""
    for char in string:
        if char == "(":
            mark = False
            continue
        if mark is True:
            out_string += char
        if char == ")":
            mark = True

    return out_string


def get_text_three_kindom():
    file = open("Docs/sgyy.txt", encoding='utf-8')
    # print(file)
    new = ""

    for x in file:
        # print(x)
        if x == "\n":
            continue
        if x.__contains__(u"---"):
            continue
        if x[:1] == "(":
            continue
        x = parentheses_removal(x)
        new += x

    fl = open('Docs/sg.txt', 'w', encoding="utf-8")
    fl.write(new)

    start = u"玄德曰：“昔高祖之得天下，盖为能招降纳顺"

    return [new, start]


def get_text_three_body():
    file = open("Docs/santi.txt", encoding='utf-8', errors="ignore")
    # print(file)
    new = ""

    for x in file:
        # print(x)
        if x == "\n":
            continue
        if x.__contains__(u"第") and x.__contains__(u"章") and len(x) < 10:
            continue
        if x.__contains__(u"------------"):
            new = new[:-1]
            continue
        if x == "※※※\n":
            continue
        if x[:2] == "注释":
            continue
        if x[:1] in "⓪ ① ② ③ ④ ⑤ ⑥ ⑦ ⑧ ⑨ ⑩ ⑪ ⑫ ⑬ ⑭ ⑮".split(" "):
            continue
        if x.__contains__(u"分节阅读"):
            continue
        new += x

    fl = open('Docs/st.txt', 'w', encoding="utf-8")
    fl.write(new)

    start = u"罗辑抬头打量着这个他曾在电视上看到过无数次的地方，"

    return [new, start]


def get_text_pfdsj():
    file = open("Docs/31903.txt", encoding='utf-8')
    # print(file)
    new = ""

    for x in file:
        # print(x)
        if x == "\n":
            continue
        if x.__contains__(u"第") and x.__contains__(u"章") and len(x) < 10:
            continue
        if x.__contains__(u"------------"):
            new = new[:-1]
            continue
        if x.__contains__(u"分节阅读"):
            continue
        new += x

    fl = open('Docs/a.txt', 'w', encoding="utf-8")
    fl.write(new)

    start = u"孙少平在农村长大，深刻认识这黄土地上养育出来的人"

    return [new, start]
