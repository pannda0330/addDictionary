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

def getPage(num):
    lines = [line.strip() for line in codecs.open("tangoichiran/index{}-.html".format(num), 'r', 'utf-8')]
    n=0
    global log
    for i in range(len(lines)):
        if u"<div class=\"overflow-title\">" in lines[i]:
            url=re.search('/a/[^\"]*',lines[i+1])
            #log収集
            log=log + "http://dic.nicovideo.jp{}".format(url.group()) + "\n"
            html=getHTML("http://dic.nicovideo.jp{}".format(url.group()))
            #保存処理
            fp = open("newtango/{}.html".format(num+n), "w")
            fp.write(html)
            fp.close()
            #待機処理
            time.sleep(1)
            print n+num
            n+=1
            #print "http://dic.nicovideo.jp{}".format(url.group())


if __name__ == '__main__':

    num=1
    end_num=451

    while num <= end_num:
        getPage(num)
        num+=50

    fp = open("newtango/newlog.txt", "w")
    fp.write(log)
    fp.close()
