#!/usr/bin/python
# -*- coding: UTF-8 -*-


def get_text():
    file = open("31903.txt", encoding='utf-8')
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

    fl = open('a.txt', 'w', encoding="utf-8")
    fl.write(new)
    return new
