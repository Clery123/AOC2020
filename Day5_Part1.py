def seat():
    lst =[]
    f = open("data1.txt","r")
    for x in f.readlines():
        start = 0
        middle = 0
        end = 128
        startL = 0
        endL = 8
        middleL =0
        for i in range(0,10):
            if(x[i]=='F'): #Front (lower half)
                middle = int((start+end)/2)
                end = middle
                
            if(x[i]=='B'): #Back (upper half)
                middle = int((start+end)/2)
                start = middle
            if(x[i]=='L'): #Front (lower half)
                middleL = int((startL+endL)/2)
                endL = middleL
                
            if(x[i]=='R'): #Back (upper half)
                middleL = int((startL+endL)/2)
                startL = middleL
        lst.append(start*8+startL)
    lst.sort()
    print(lst[-1])

seat()
          
