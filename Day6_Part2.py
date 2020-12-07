import re
from collections import Counter
def split(word):
    return [char for char in word]
f = open("data.txt","r")
answeredYes =0
lst=[]
dicc ={}
tempDicc={}
for x in f.readlines():
    if(x=='' or x ==' 'or x=='\n'):
        first = True
        for i in range(0,len(lst)):
            c = Counter(split(lst[i]))
            for key in c.keys():
                if key in dicc.keys():
                    dicc[str(key)]+=1
            tempDicc.update(c)
            tempDicc={**dicc}
            if(first == True):
                dicc.update(c)
            else:
                dicc={**tempDicc}
            first = False
        for key in dicc.values():
            if key == len(lst):
               answeredYes+=1
        lst =[]
        dicc={}
      
    else:
        x=re.sub(r"[\n\t\s]*","",x)
        lst.append(x)
print(answeredYes)