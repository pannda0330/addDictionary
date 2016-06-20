# -*- coding: utf-8 -*-

import codecs, sys

def checkWord(word,dic):

    low = 0
    high = len(dic)-1
    t = ( low + high ) / 2

    #二分探索で同じ読みのものがないかを探し、同じ読みのものが見つかったら単語も同じかどうかを判定する。
    while low <= high:
        if len(dic) <= t or t < 0:
            print "t={},dic={}".format(t,len(dic))
        line = dic[t]
        checkword = line.split(u",")
        #読みが同じものが見つかったらその前後の読みが同じものすべてに探索をする。
        if checkword[len(checkword)-2] == word[1]:
            print "check-{}".format(t)
            if checkword[0] == word[0]:
                return False
            td = t - 1
            cw = dic[td].split(u",")
            while td >= 0 and cw[len(cw)-2] == word[1]:
                print "check-{}".format(td)
                if cw[0] == word[0]:
                    return False
                td -= 1
                cw = dic[td].split(u",")
            tu = t + 1
            cw = dic[tu].split(u",")
            while len(dic) > tu and cw[len(cw)-2] == word[1]:
                print "check-{}".format(td)
                if cw[0] == word[0]:
                    return False
                tu += 1
                cw = dic[tu].split(u",")
            return True
        elif checkword[len(checkword)-2] < word[1]:
            low = t + 1
        elif checkword[len(checkword)-2] > word[1]:
            high = t - 1
        t = (low + high) / 2
    return True

if __name__ == '__main__':


    dic=""

    delnum=0

    lines = [line.strip() for line in codecs.open('BSjisyo7.txt', 'r', 'utf-8')]
    #neologd = [line.strip() for line in codecs.open('neologd/neologd-adverb-dict-seed.20150623.csv', 'r', 'utf-8')] #63delete
    #neologd = [line.strip() for line in codecs.open('neologd/neologd-interjection-dict-seed.20151022.csv', 'r', 'utf-8')] #17delete
    #neologd = [line.strip() for line in codecs.open('neologd/neologd-adjective-verb-dict-seed.20160324.csv', 'r', 'utf-8')]#19delete
    #neologd = [line.strip() for line in codecs.open('neologd/neologd-adjective-exp-dict-seed.20151126.csv', 'r', 'utf-8')] #0delete
    #neologd = [line.strip() for line in codecs.open('neologd/neologd-common-noun-ortho-variant-dict-seed.20150323.csv', 'r', 'utf-8')]#128delete
    #neologd = [line.strip() for line in codecs.open('neologd/neologd-adjective-std-dict-seed.20151126.csv', 'r', 'utf-8')]#5delete
    #neologd = [line.strip() for line in codecs.open('neologd/neologd-noun-sahen-conn-ortho-variant-dict-seed.20160323.csv', 'r', 'utf-8')]#23delete
    neologd = [line.strip() for line in codecs.open('neologd/mecab-user-dict-seed.20160616.csv', 'r', 'utf-8')]#176delete
    i=0

    #収集した単語を一つずつ辞書データと比較し、一致するものがなければdicに追加する。このとき一致するものがあった場合delnumに1を足す
    for line in lines:
        word = line.split(u"\t")
        flag = checkWord(word,neologd)
        if flag:
            dic = dic + line + u"\n"
        else:
            delnum += 1
        print "{}-{}".format(i,flag)
        i += 1

    fp = open("BSjisyo8.txt", "w")
    fp.write(dic)
    fp.close()

    print "{}-delete".format(delnum)
