import pickle

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
pickle.dump(loc,open("doc_loc.pkl","wb"))
loc.clear()

