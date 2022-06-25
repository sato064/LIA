from sklearn.exceptions import ConvergenceWarning
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import cross_validate, train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
from sklearn.model_selection import cross_val_score
import pandas as pd
import numpy as np
import re
import warnings
warnings.simplefilter('ignore', FutureWarning,)
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

scoring = { 
            "acr": "accuracy",
            "pcs": "precision_micro",
            "rcl": "recall_micro",
            "f1": "f1_micro",
            "pcs_mcr": "precision_macro",
            "rcl_mcr": "recall_macro",
            "f1_mcr":"f1_macro"

        }

lr = LogisticRegression(max_iter=98)
scores = cross_validate(lr, df, pos_neg_list,scoring=scoring)
print('Average accuracy: {}'.format(np.mean(scores["test_acr"])))
print('Average precision(micro): {}'.format(np.mean(scores["test_pcs"])))
print('Average recall(micro): {}'.format(np.mean(scores["test_rcl"])))
print('Average f1(micro): {}'.format(np.mean(scores["test_f1"])))
print('Average precision(macro): {}'.format(np.mean(scores["test_pcs_mcr"])))
print('Average recall(macro): {}'.format(np.mean(scores["test_rcl_mcr"])))
print('Average f1(macro): {}'.format(np.mean(scores["test_f1_mcr"])))

f.close()