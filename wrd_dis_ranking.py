from normalize import normalize
import pickle

data=pickle.load(open("bow.pkl", "rb"))

locs={}
for i in range(0,281080):
    pos={}
    cou={}
    c=0
    for j in data[i]:
        c+=1
        if j not in pos.keys():
            pos[j]=c
            cou[j]=1
        else:
            pos[j]=(pos[j]*cou[j]+c)/(cou[j]+1)
            cou[j]=cou[j]+1
    locs[i]=pos 

def wrd_dis_query(query):
    res={}
    for i in range(0,281080):
        dis=0
        key=locs[i].keys()
        for j in range(0,len(query)):
            if query[j] in key:
                for k in range(j+1,len(query)):
                    if query[k] in key:
                        dis+=abs(locs[i][query[j]]-locs[i][query[k]])
                    else:
                        dis+=10000
            else:
                dis+=10000*(len(query)-j-1)
        res[i]=dis
    res=normalize(1,res)
    return res