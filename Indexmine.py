# -*- coding: utf-8 -*-

import urllib2, random, os, time, sys, codecs,re

log=""

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


def getPage(kana,n,url):
    global log
    #log収集
    log=log+url+"\n"
    html=getHTML(url)
    #ファイル名指定
    filename="IndexPage/{}/{}.html".format(kana,n)
    print "{}-{}\t{}".format(kana,n,url)
    #保存処理
    fp = open(filename,"w")
    fp.write(html)
    fp.close

    #待機処理
    time.sleep(1)

    #保存したHTMLファイルを読み込む
    lines = [line.strip() for line in codecs.open(filename, 'r', 'utf-8')]

    for line in lines:
        #次への記述がある行を見つけたらその行からURLを取得する。
        if u"次へ" in line:
            key = re.search("/m/yp/a/[^\"]*", line)
            if key:
                nexturl = "http://dic.nicovideo.jp" + key.group()
                #取得したURLでgetPageを再帰する。
                getPage(kana, n + 1, nexturl)
            break


if __name__ == '__main__':

    #ニコニコ大百科の50音順単語記事一覧のページを1行ずつ読み込む
    lines = [line.strip() for line in codecs.open("DicIndex.html", 'r', 'utf-8')]

    num=1

    #50音順単語記事タイトル表示へのリンクのURLを抜き出し、getPageに送る
    #また、このとき50音ごとにディレクトリを作成する。
    for line in lines:
        key=re.search("/m/yp/a/[^\"]*",line)
        if key:
            url="http://dic.nicovideo.jp"+key.group()
            if not os.path.exists("IndexPage/{}".format(num)):
                os.mkdir("IndexPage/{}".format(num))
            getPage(num,1,url)
            num+=1

    fp = open("log.txt", "w")
    fp.write(log)
    fp.close()
