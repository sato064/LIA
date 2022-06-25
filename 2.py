from telnetlib import WILL
from unittest import skip
from collections import defaultdict
from nltk import ngrams
import pandas as pd

file = r'neko.txt.mecab' #吾輩は猫である の形態素解析済みファイル読み込み
sen = []
cnts = []
words = []
with open(file) as f: #単語区切りのリスト作成
    for line in f:
        fields = line.split('\t')
        if fields[0] == ''or fields[0] == '\n':
            continue
        elif fields[0] == 'EOS\n':
            words.append("EOS")
        elif fields[0] == '\u3000':
            words.append("BOS")
        else:
            words.append(fields[0])
f.close()

bygrams = list(ngrams(words, 2)) #bygramのリスト作成
list = defaultdict(int)

for by in bygrams: #bygramの出現頻度計算
    list[by] += 1
list = sorted(list.items(), key=lambda x: x[1], reverse=True)

bygrams = []  #データの整形
for line in list:
    lin = ' '.join(s for s in line[0])
    lin = lin.split(' ')
    lin.append(line[1])
    bygrams.append(lin)


bygrams = pd.DataFrame(bygrams,columns=["first_word", "second_word", "c"])
print(bygrams)

ans = [] #確率の計算とリストへの格納
for idx, data in bygrams.iterrows():
    sum = 0
    first_word = data[0]
    tgt = bygrams[(bygrams['first_word'] == first_word)]
    ans.append([[data[0],data[1]],data[2] / tgt['c'].sum()])

ans = sorted(ans, key=lambda x: x[1], reverse=True)
print(ans)

#外部ファイルへの書き出し(課題3で利用)
with open('list.txt', 'w') as fw:
    for d in ans:
        fw.write("%s\n" % d)
        