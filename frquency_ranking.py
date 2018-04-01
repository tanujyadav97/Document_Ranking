import pickle
from collections import Counter

data=pickle.load(open("bow.pkl", "rb"))

freq={}
for i in range(0,281080):
    freq[i]=Counter(data[i])

pickle.dump(freq,open("freq.pkl","wb"))
freq.clear()



#res1=fre_query(['computer','science'])