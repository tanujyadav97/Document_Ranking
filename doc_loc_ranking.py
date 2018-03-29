import pickle
from normalize import normalize

data=pickle.load(open("bow.pkl", "rb"))

loc={}
for i in range(0,281080):
    pos={}
    c=0
    for j in data[i]:
        c+=1
        if j not in pos.keys():
            pos[j]=c
    loc[i]=pos

def doc_loc_query(query):
    res={}
    for i in range(0,281080):
        summ=0
        wrds=loc[i].keys()
        for j in query:
            if j in wrds:
                summ+=loc[i][j]
            else:
                summ+=100000
        res[i]=summ
    res=normalize(1,res)
    return res