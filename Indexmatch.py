# -*- coding: utf-8 -*-

import codecs, sys, re, os

#ニコニコ大百科の目次ページの1行から単語と読みを抜き取る

def makeDic(num,n):
    dic=""
    #保存してある単語記事タイトル表示ページのHTMLを開く
    lines = [line.strip() for line in codecs.open('IndexPage/{}/{}.html'.format(num,n), 'r', 'utf-8')]
    #1行づつ読み込み、単語ページへのリンクがあるぺーじを探す
    #re.splitを使い、単語記事のタイトル（単語）と読みをそれぞれ抜き出し、それをdicに足していく
    for i in range(len(lines)):
        if u"<li>" in lines[i] and u"<a href=\"/a/" in lines[i+1]:
            txt=re.split('[<>:]',lines[i+1])
            if len(txt) == 8:
                yomi=re.split('[()]',txt[4])
                dic = dic + "{}\t{}\n".format(txt[2], yomi[1])
    #単語と読みのペアが複数書き込まれたdicを返す。
    return dic

if __name__ == '__main__':

    num=1
    end_num=85
    dic=""

    while num <= end_num:
        n=1
        while os.path.exists("IndexPage/{}/{}.html".format(num,n)):
            dic = dic + makeDic(num,n)
            print "{}-{}".format(num,n)
            n+=1
        num+=1

    fp = open("jisyo2.txt", "w")
    fp.write(dic)
    fp.close()
