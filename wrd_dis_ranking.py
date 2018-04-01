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

pickle.dump(locs,open("locs.pkl","wb"))
locs.clear()

