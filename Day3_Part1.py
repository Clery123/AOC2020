f = open("data.txt","r")
d = open("data.txt","r")
counter =0
trees =0
line = f.readline()
line2 = d.readline()
while f.readline():
    line2 = d.readline()
    counter +=3
    counter= counter%31
    if(line2[counter] =='#'):
        trees+=1
    print(trees)