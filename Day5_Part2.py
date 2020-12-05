import time
def heslo():
    lst =[]
    f = open("C:\\Users\\andre\\Desktop\\VIS_course-master\\data1.txt","r")
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
    print(find_missing(lst))
    
def find_missing(lst):
    return [x for x in range(lst[0], lst[-1]+1)  
                            if x not in lst] 
start = time.time()     
heslo()
end = time.time()
print(end-start)             
