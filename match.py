# -*- coding: utf-8 -*-

import codecs, sys, re

#HTMLからページのタイトルを抜き出す
def getTitle(src):
    title=re.search('<title>.*</title>',src)
    return title

#ニコニコ大百科の単語記事ページのタイトルから単語と読みを取るなければNone
def getTango(title):
    if u'とは' in title:
        tango = title.split(u'とは')
        tango[0]=tango[0].replace(u"<title>",u"")
        tango[1]=tango[1].replace(u" (",u"")
        return tango
    else:
        return None

def makeDic(num):
    lines = [line.strip() for line in codecs.open('newtango/{}.html'.format(num), 'r', 'utf-8')]
    for line in lines:
        title=getTitle(line)
        if title:
            tango=getTango(title.group())
            break
    if tango == None:
        return ""
    else:
        return "{}\t{}\n".format(tango[0], tango[1])

if __name__ == '__main__':

    num=1
    end_num=500
    dic=""

    while num <= end_num:
        dic = dic + makeDic(num)
        num += 1

    fp = open("newWord.txt", "w")
    fp.write(dic)
    fp.close()
