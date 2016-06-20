# -*- coding: utf-8 -*-

import urllib2, random, os, time, sys

def getHTML(url):
    i=0
    while i<10:
        try:
            res=urllib2.urlopen(url)
            break;
        except:
            time.sleep(1)
            i+=1
    if i==10:
        sys.stderr.write("10 times time-out\n")
        sys.exit(1)
    return res.read()


if __name__ == '__main__':
    num=1
    end_num=451
    #クローリング
    while num <= end_num:
        #ニコニコ大百科最近更新された単語記事の目次ページを収集
        url="http://dic.nicovideo.jp/m/u/a/{}-".format(num)
        html = getHTML(url)
        #保存処理
        fp = open("tangoichiran/index{}-.html".format(num), "w")
        fp.write(html)
        fp.close()
        #待機処理
        time.sleep(1)
        num+=50
