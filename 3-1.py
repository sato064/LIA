from gensim.models import word2vec
import pandas as pd
from scipy.stats import spearmanr

file_name = "Vec_BCCWJ_w2v_all_win10_dim300_skipgram_ns5.txt"
model = word2vec.KeyedVectors.load_word2vec_format(file_name)
df = pd.read_csv("jwsan-1400.csv")
#print(df)
jwsan_sim_list = df['similarity'].to_list()
jwsan_asc_list = df['association'].to_list()

w2v_sim_list = []

for index,row in df.iterrows():
    w2v_sim_list.append(model.similarity(row[1], row[2]))
    
sim_correlation, pvalue = spearmanr(jwsan_sim_list, w2v_sim_list)
asc_correlation, pvalue = spearmanr(jwsan_asc_list, w2v_sim_list)
print('類似度との相関係数 = ' + str(sim_correlation))
print('関連度との相関係数 = ' + str(asc_correlation))