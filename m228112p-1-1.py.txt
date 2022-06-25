import MeCab
from collections import defaultdict


file = r'neko.txt.mecab' #吾輩は猫である の形態素解析済みファイル読み込み
sens = []
cnts = []
with open(file) as f:
    for line in f:
        if line != 'EOS\n': #文末記号の例外処理
            fields = line.split('\t')
            if len(fields) != 2 or fields[0] == '': #開業記号と空白文字のエスケープ
                continue
            else:
                attr = fields[1].split(',')
                ins = {'surface': fields[0], 'base': attr[6], 'pos': attr[0], 'pos1': attr[1]} #中身の作成
                cnts.append(ins)
        else:
            sens.append(cnts)
            cnts = []
f.close()

ans = defaultdict(int)
for sentence in sens:
  for cnt in sentence:
    if cnt['pos'] == '名詞' or cnt['pos'] == '動詞': #動詞と名詞の場合
        if cnt['base'] != "*\n":
            ans[cnt['base']] += 1 #辞書型への追加
ans = sorted(ans.items(), key=lambda x: x[1], reverse=True) #出現回数順の並び替え

print(ans)