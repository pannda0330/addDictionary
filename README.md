# addDictionary
ニコニコ大百科のサイトからneologdへの単語追加を行うプログラムとその結果集まった単語のテキストデータ、またそれを収集したサイトのURLを保存していあります。

各ファイル説明

----単語記事一覧から収集----

Indexmine.py
ニコニコ大百科の単語記事一覧のhtmlをクローリングするプログラム

Indexmatch.py
上のプログラムで収集したページから単語と読みのペアを抜き出すプログラム

BSyomi.py
二分探索を用いて集まった単語とneologdに含まれる単語に重複がないかを調べるプログラム

addWord.txt
集まった単語の一覧。一行につき1単語、「単語\t読み」の形で記されている

matching.py
全探索を用いて重複がないかを調べるプログラム。こちらはneologdに収録されている読みと発音の両方と集めた単語の読みが一致しないかを調べることができる。

-------------------------

----最近更新された単語を収集----

getIndex.py
最近更新された記事一覧を取得する。

tangomine.py
上のプログラムで集めた記事一覧からそれぞれの単語記事を収集する。

match.py
集まった単語記事のタイトル部分から単語と読みを抜き出す。

newWord.txt
上記の過程で集めた単語と読みのペアが記されたファイル

-----------------------------
