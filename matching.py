# -*- coding: utf-8 -*-

import codecs, sys

#ニコニコ大百科の目次ページの1行から単語と読みを抜き取る

def checkWord(word,dic):
    i=0
    for line in dic:
        checkword=line.split(u",")
        if checkword[0] == word[0]:
            print "check-{}".format(i)
            for w in checkword:
                if word[1] == w:
                    return False
        i+=1
    return True

if __name__ == '__main__':


    dic=""

    lines = [line.strip() for line in codecs.open('jisyo2.txt', 'r', 'utf-8')]
    neologd = [line.strip() for line in codecs.open('neologd/mecab-user-dict-seed.20160616.csv', 'r', 'utf-8')]
    i=0

    for line in lines:
        word = line.split(u"\t")
        flag = checkWord(word,neologd)
        if flag:
            dic = dic + line + "\n"
        print "{}-{}".format(i,flag)
        i += 1

    fp = open("addword.txt", "w")
    fp.write(dic)
    fp.close()
