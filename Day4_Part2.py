def passport():
    f = open("data.txt","r")
    count =0
    pidCNT = 0
    password =""
    pid = ""
    eclCheck= ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    checker =0
    for line in f.readlines():
        password+=line
        if(line=="\n"):
            if("byr:"in password and "iyr:" in password and "eyr:" in password and "hgt:" in password and "hcl:" in password and "ecl:" in password and "pid:" in password):
                byr = password[password.find("byr:")+4:password.find("byr:")+10] #4 digits 1920 - 2002
                iyr = password[password.find("iyr:")+4:password.find("iyr:")+10] #2010 -2020
                eyr = password[password.find("eyr:")+4:password.find("eyr:")+10]  #2020 -2030
                hgtCm = password[password.find("hgt:")+4:password.find("hgt:")+7] # 150 - 193 or 59-76
                hgtIn = password[password.find("hgt:")+4:password.find("hgt:")+6]
                hgt2= password[password.find("hgt:")+7:password.find("hgt:")+10] #cm
                hgt3= password[password.find("hgt:")+6:password.find("hgt:")+9] #in
                hcl = password[password.find("hcl:")+4:password.find("hcl:")+15] # #0-9 or a-f
                ecl = password[password.find("ecl:")+4:password.find("ecl:")+8]# amb, blu, brn, gry, hzl, oth
                pd = password[password.find("pid:")+4:] #0000545 9 digit number
                for x in pd:
                    if(x.isnumeric()):
                        pid+=x
                    if(x==' ' or x =='' or x =='\n'):
                        break
                    pidCNT+=1
                if(len(pid)==9):
                    checker+=1
                    
                #Check one digit above 4
                if(byr[4]==' 'or byr[4]=='\n'):
                    br = byr[0]+byr[1]+byr[2]+byr[3]
                if(ecl[3]==' 'or ecl[3]=='\n'):
                    el = ecl[0]+ecl[1]+ecl[2]
                if(iyr[4]==' 'or iyr[4]=='\n'):
                    ir = iyr[0]+iyr[1]+iyr[2]+iyr[3]
                if(eyr[4]==' 'or eyr[4]=='\n'):
                    er = eyr[0]+eyr[1]+eyr[2]+eyr[3]
            
                if(int(br) <=2002 and int(br) >=1920):
                    checker+=1
                if(int(ir)>=2010 and int(ir)<=2020):
                    checker+=1
                if(int(er)>=2020 and int(er) <=2030):
                    checker+=1
                if(hgt2=="cm "or hgt2=='cm\n'):
                    if(int(hgtCm)<=193 and int(hgtCm) >=150):
                        checker+=1
                       
                elif(hgt3=="in "or hgt3=="in\n"):
                    if(int(hgtIn)<=76 and int(hgtIn) >=59):
                        checker+=1 
                        
                if(hcl.find(r'#[0-9a-f]{6}')):
                    if(hcl[0]=='#'):
                        
                        checker+=1
                if(el in eclCheck):
                    checker+=1
                if(checker ==7):
                    count+=1
                    checker=0
                elif(checker!=7):
                    checker=0
            password=""
            hgt2= ""
            br=""
            el=""
            ir=""
            er=""
            hgt3=""
            pid =""
    print(count)
            
passport()