import re
f = open("data.txt","r")
groupAnswers =""
answeredYes =0
for x in f.readlines():
    if(x=='' or x ==' 'or x=='\n'):
        groupAnswers = re.sub(r"[\n\t\s]*","",groupAnswers)
        answeredYes += len(set(groupAnswers))
        groupAnswers = ""
    groupAnswers+=x
        
print(answeredYes)
