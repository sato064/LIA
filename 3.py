from socketserver import ThreadingUnixDatagramServer
from telnetlib import WILL
from unittest import skip
import MeCab
from collections import defaultdict
from nltk import ngrams
import pandas as pd
import math

file = r'nekojanai.txt.mecab' #吾輩は猫ではない の読み込み
sen = []
cnts = []
words = []
with open(file) as f: #単語区切りのリスト作成
    for line in f:
        fields = line.split('\t')
        if fields[0] == 'EOS\n':
            words.append("EOS")
        else:
            words.append(fields[0])
f.close()

tgts = list(ngrams(words, 2)) #bygramsのリスト作成

file = r'list.txt' #吾輩は猫であるのbygrams,条件付き確率の読み込みと整形
bygrams = []
with open(file) as f2:
    for line in f2:
        line = line.strip()
        line = line.replace('[','')
        line = line.replace('(','')
        line = line.replace(']','')
        line = line.replace(')','')
        line = line.replace('\'','')
        line = line.split(', ')
        bygrams.append(line)
f2.close()

bygrams = pd.DataFrame(bygrams, columns=["first_word","second_word","p"])
print(bygrams)
p_list = []
for tgt in tgts: #文章の確率計算
    tgt_bygram = bygrams[(bygrams['first_word'] == tgt[0]) & (bygrams['second_word'] == tgt[1])]
    series = tgt_bygram['p']
    p_list.append(float(series.iloc[-1]))
    

print("入力された文の確率")
print(math.prod(p_list)) #piの算出