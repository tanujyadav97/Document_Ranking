import string

file=open("outputacm.txt","r",encoding="utf8")
content=file.read()

doc=content.split("#*")
print(len(doc))

temp=[]
for d in doc:
    if "#!" in d:
        d=d.translate(str.maketrans(string.punctuation, ' '*len(string.punctuation)))
        temp.append(d)
print(len(temp))

docs=[]
for d in temp:
    d=' '.join(d.split())
    docs.append(d)
print(len(docs))

for i in range(0,len(docs)):
    f=open('C:/Users/15121/PycharmProjects/docs/'+str(i)+'.txt',"w+",encoding="utf8")
    f.write(docs[i])
    f.close()