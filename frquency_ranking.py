import pickle
from collections import Counter
from normalize import normalize

data=pickle.load(open("bow.pkl", "rb"))

freq={}
for i in range(0,281080):
    freq[i]=Counter(data[i])

def fre_query(query):
    res={}
    for i in range(0,281080):
        wrds=freq[i].keys()
        summ=0
        for j in query:
            if j in wrds:
                summ+=freq[i][j]
        res[i]=summ
    res=normalize(0,res)
    return res

#res1=fre_query(['computer','science'])