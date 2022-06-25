from sklearn.exceptions import ConvergenceWarning
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
import pandas as pd
import numpy as np
import re
import warnings
warnings.simplefilter('ignore', FutureWarning)
warnings.simplefilter('ignore', UserWarning)
warnings.simplefilter('ignore', ConvergenceWarning,)

#読み込み
f = open('sentiment.txt', 'r')
datalist = f.readlines()
pos_neg_list = []
for i in range(len(datalist)):
    if datalist[i][0] == "-":
        pos_neg_list.append(0)
    else:
        pos_neg_list.append(1)
        


for i in range(len(datalist)):
    s =  re.sub(r"[^a-zA-Z0-9 ]", "", datalist[i][3:])
    datalist[i] = s
#Bow
cnt = CountVectorizer()
cnt.fit(datalist)
word = cnt.transform(datalist)
vector = word.toarray()
name = cnt.get_feature_names()
df = pd.DataFrame(vector, columns=name)

lr = LogisticRegression(max_iter=98)
lr.fit(df, pos_neg_list)

pred = lr.predict(vector)

print('accuracy = ', accuracy_score(y_true=pos_neg_list, y_pred=pred))
print('precision = ', precision_score(y_true=pos_neg_list, y_pred=pred))
print('recall = ', recall_score(y_true=pos_neg_list, y_pred=pred))
print('f1 score = ', f1_score(y_true=pos_neg_list, y_pred=pred))
    
f.close()