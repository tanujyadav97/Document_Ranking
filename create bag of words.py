import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import *
stemmer = PorterStemmer()
import pickle

sw=stopwords.words('english')

bow={}
for i in range(0,281080):
    f=open('C:/Users/15121/PycharmProjects/docs/'+str(i)+'.txt',"r",encoding="utf8")
    data=f.read()
    f.close()
    words=[stemmer.stem(i) for i in data.split(' ') if i not in sw]
    bow[i]=words

pickle.dump( bow, open( "bow.pkl", "wb" ) )